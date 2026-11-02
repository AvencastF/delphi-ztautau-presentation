<script setup>
// Fixed chapter list of this talk, drawn by the shared ChapterRail (deck-local wrapper, as in the status deck).
import ChapterRail from 'slidev-addon-ztautau/components/ChapterRail.vue'
defineProps({ active: Number })
const chapters = ['Why spin', 'DELPHI and the data', 'Reconstruction', 'Spin fit', 'Outlook']
</script>

<template>
  <ChapterRail :chapters="chapters" :active="active" />
</template>
