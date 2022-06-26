<script lang="tsx">
  import api from "@/api"
  import { format_bytes } from "@/utils"
  import { computed, defineComponent } from "vue"

  export default defineComponent({
    props: {
      current: {
        type: Number,
        default: 0
      },
      total: {
        type: Number,
        default: 0
      },
      visible: {
        type: Boolean,
        default: false
      }
    },
    setup(props, { emit }) {
      const progress = computed(() => {
        if (props.current == 0) {
          return 0
        }
        return (props.current / props.total) * 100
      })

      function complete() {
        emit("update:visible", false)
        if (window.ipcRenderer) {
          window.ipcRenderer.invoke("restart")
        } else {
          api.restart()
        }
      }

      return () => {
        return (
          <calc-dialog title="自动更新" visible={props.visible}>
            <div class="flex flex-col py-4 px-8 items-center justify-center">
              <div class="w-60">
                <div style={progress.value == 0 ? `width:0` : `width:${progress.value.toFixed(2)}%`} class="bg-gradient-to-bl rounded-md from-green-500 to-blue-500 h-6"></div>
              </div>
              <div class="my-2 text-white">
                {format_bytes(props.current)} / {format_bytes(props.total)}
                <span class="ml-4"> {progress.value.toFixed(2)}%</span>
              </div>
              <div>
                <calc-button onClick={complete} disabled={progress.value < 100}>
                  {progress.value < 100 ? "更新中" : "完成"}
                </calc-button>
              </div>
            </div>
          </calc-dialog>
        )
      }
    }
  })
</script>
