<script lang="tsx">
  import { computed, defineComponent } from "vue"

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

      function prev() {
        if (page.value > 0) {
          page.value--
          emit("prev")
          emit("change", page.value)
        }
      }

      function next() {
        if (page.value < props.totalPage) {
          page.value = page.value + 1
          emit("next")
          emit("change", page.value)
        }
      }

      return () => {
        return (
          <div class="flex space-x-1 h-10 w-full items-center justify-center">
            <calc-button icon="prev" disabled={page.value <= 1} onClick={prev}></calc-button>
            <span class="text-center w-8">
              {page.value}/{props.totalPage}
            </span>
            <calc-button icon="next" disabled={props.page >= props.totalPage} onClick={next}></calc-button>
          </div>
        )
      }
    }
  })
</script>
<style lang="scss"></style>
