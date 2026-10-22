// Inline KaTeX for the animated components (v-html), as in the reference deck's NJUAlignLoop.vue.
import katex from 'katex'
export const tex = (formula: string) => katex.renderToString(formula, { throwOnError: false, strict: 'ignore' })
// Mixed text: "$...$" fragments rendered as math, the rest kept as text.
export const mixed = (s: string) => s.split(/(\$[^$]+\$)/g).map(p => p.startsWith('$') && p.endsWith('$') ? tex(p.slice(1, -1)) : p.replace(/</g, '&lt;')).join('')
