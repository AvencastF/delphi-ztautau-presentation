import { mkdirSync, writeFileSync } from 'node:fs'
import { join } from 'node:path'
import { pathToFileURL } from 'node:url'
import { repoRoot, validateName } from './lib/decks.mjs'

export function createDeck(name, root = repoRoot) {
  validateName(name)
  const directory = join(root, name)
  // Non-recursive mkdir intentionally rejects existing files and directories.
  mkdirSync(directory)
  mkdirSync(join(directory, 'slides'))
  mkdirSync(join(directory, 'public'))
  const title = name.replace(/[_-]/g, ' ')
  writeFileSync(join(directory, 'slides.md'), `---
theme: default
addons:
  - slidev-addon-ztautau
fonts:
  sans: DM Sans
  local: DM Sans
title: ${JSON.stringify(title)}
colorSchema: dark
transition: none
mdc: true
routerMode: hash
aspectRatio: 16/9
canvasWidth: 980
drawings:
  persist: false
lineNumbers: false
preload: false
class: st-cover no-page-number
---

# ${title}

<div class="st-cover-sub">Start your presentation here.</div>
`)
  writeFileSync(join(directory, 'style.ts'), [
    '../shared/brand/fonts.css',
    '../shared/styles/main.css',
    '../shared/styles/animations.css',
    '../shared/styles/base.css',
    '../shared/styles/graphite.css',
    '../shared/styles/chapters.css',
    '../shared/styles/status.css',
  ].map(path => `import '${path}'\n`).join(''))
  return directory
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    if (process.argv.length !== 3) throw new Error('Usage: npm run new -- <deck>')
    createDeck(process.argv[2])
    console.log(`Created ${process.argv[2]}. Run: npm run dev -- ${process.argv[2]}`)
  }
  catch (error) {
    console.error(error.code === 'EEXIST' ? 'That directory already exists; nothing was overwritten.' : error.message)
    process.exitCode = 1
  }
}
