<script setup lang="ts">
// Same interface as the reference deck's LaTeX component (<LaTeX formula="\tau^+\tau^-" />),
// but rendered synchronously with the bundled KaTeX so there is no flash of raw TeX and no CDN stylesheet.
import { computed } from 'vue'
import katex from 'katex'
const props = withDefaults(defineProps<{ formula: string, block?: boolean }>(), { block: false })
const html = computed(() => katex.renderToString(props.formula, { throwOnError: false, displayMode: props.block, strict: 'ignore' }))
</script>

<template>
  <div v-if="block" class="latex-block" v-html="html" />
  <span v-else class="latex-inline" v-html="html" />
</template>

<style scoped>
.latex-inline { white-space: nowrap; }
.latex-inline :deep(.katex) { font-size: 1.04em; }
</style>
