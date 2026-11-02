<script setup lang="ts">
import { useNav } from '@slidev/client'
import { computed } from 'vue'
const { currentSlideNo, total } = useNav()
const isTitlePage = computed(() => currentSlideNo.value === 1)
</script>

<template>
  <div v-if="!isTitlePage" class="page-number" aria-label="Page number">
    <span class="page-number-current">{{ currentSlideNo }}</span><span class="page-number-separator">/</span><span class="page-number-total">{{ total }}</span>
  </div>
</template>

<style scoped>
.page-number { position: fixed; top: 1.2rem; right: 2rem; z-index: 100; display: flex; align-items: baseline; gap: .25rem; font-family: 'DM Sans', sans-serif; font-size: .875rem; color: var(--fg-2); pointer-events: none; opacity: .85; }
.page-number-current { font-weight: 600; color: var(--fg-1); }
.page-number-separator { opacity: .6; }
</style>
