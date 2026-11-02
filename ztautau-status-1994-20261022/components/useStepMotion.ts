// Shared anime.js step driver, following the reference deck's NJUAlignLoop pattern:
// animate a numeric "stage" toward the slide's click count while the slide is the
// current, visible, motion-allowed slide; otherwise jump so exports show the final state.
import { computed, onBeforeUnmount, onMounted, reactive, ref, watch, type Ref } from 'vue'
import { animate } from 'animejs'
import { useSlideContext } from '@slidev/client'

export function useStepMotion(step: () => number, max: number, duration = 900) {
  const { $nav, $page, $renderContext } = useSlideContext()
  const motion = reactive({ stage: Math.min(step(), max), cycle: 0 })
  const reduced = ref(false), hidden = ref(false)
  let media: MediaQueryList | undefined
  let transition: ReturnType<typeof animate> | undefined
  let loop: ReturnType<typeof animate> | undefined
  const running = computed(() => $nav.value.currentPage === $page.value && $renderContext.value === 'slide' && !reduced.value && !hidden.value)
  const stage = computed(() => Math.min(step(), max))
  const clamp = (n: number) => Math.max(0, Math.min(1, n))
  const reveal = (s: number) => clamp(motion.stage - s + 1)
  function update() {
    transition?.cancel()
    if (!running.value) { motion.stage = stage.value; return }
    transition = animate(motion, { stage: stage.value, duration, ease: 'inOutCubic' })
  }
  function sync() {
    loop?.cancel()
    if (running.value) loop = animate(motion, { cycle: { from: 0, to: 1 }, duration: 3000, ease: 'linear', loop: true })
    update()
  }
  const preference = () => { reduced.value = !!media?.matches }
  const visibility = () => { hidden.value = document.hidden }
  onMounted(() => {
    media = window.matchMedia('(prefers-reduced-motion: reduce)')
    media.addEventListener('change', preference)
    document.addEventListener('visibilitychange', visibility)
    preference(); visibility(); sync()
  })
  watch(step, update)
  watch(running, sync)
  onBeforeUnmount(() => { transition?.cancel(); loop?.cancel(); media?.removeEventListener('change', preference); document.removeEventListener('visibilitychange', visibility) })
  return { motion, running, stage, reveal }
}
