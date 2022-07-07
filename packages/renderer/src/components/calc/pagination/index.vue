<script lang="tsx">
  import { onKeyStroke } from "@vueuse/core"
  import { computed, defineComponent, onUnmounted, PropType } from "vue"

  export default defineComponent({
    props: {
      page: {
        type: Number,
        default: () => 0
      },
      totalPage: {
        type: Number,
        default: () => 0
      },
      minPage: {
        type: Number,
        default: () => 1
      },
      parent: {
        type: Object as PropType<HTMLElement>,
        default: () => document
      },
      disabled: {
        type: Boolean,
        default: false
      }
    },
    setup(props, { emit }) {
      const page = computed({
        get() {
          return Math.max(Math.min(props.page, props.totalPage), props.minPage)
        },
        set(val) {
          emit("update:page", val)
        }
      })

      function prev(e: Event) {
        e.preventDefault()
        if (page.value > 1 && !props.disabled) {
          page.value--
          emit("prev")
          emit("change", page.value)
        }
      }

      function next(e: Event) {
        e.preventDefault()
        if (page.value < props.totalPage && !props.disabled) {
          page.value = page.value + 1
          emit("next")
          emit("change", page.value)
        }
      }

      const removePrev = onKeyStroke(["F1", "PageUp"], prev, { target: props.parent })
      const removeNext = onKeyStroke(["F2", "PageDown"], next, { target: props.parent })

      onUnmounted(() => {
        removePrev()
        removeNext()
      })

      return () => {
        return (
          <div class="flex space-x-1 h-10 w-full items-center justify-center">
            <calc-button icon="prev" disabled={page.value <= 1 || props.disabled} onClick={prev}></calc-button>
            <span class="text-center w-8">
              {page.value}/{props.totalPage}
            </span>
            <calc-button icon="next" disabled={props.page >= props.totalPage || props.disabled} onClick={next}></calc-button>
          </div>
        )
      }
    }
  })
</script>
<style lang="scss"></style>
