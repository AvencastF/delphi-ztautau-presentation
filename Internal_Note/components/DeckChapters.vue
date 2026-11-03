<script setup>
import ChapterRail from 'slidev-addon-ztautau/components/ChapterRail.vue'
defineProps({ active: Number })
const chapters = ['Inputs', 'Selection', 'Cutflows', 'Data / MC', 'Machine learning', 'Spin fit', 'Photon calibration', 'Status']
</script>

<template>
  <ChapterRail :chapters="chapters" :active="active" />
</template>
