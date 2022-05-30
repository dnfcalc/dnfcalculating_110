<script lang="tsx">
  import { onClickOutside, syncRef, useDraggable, useVModel } from "@vueuse/core"
  import { computed, defineComponent, h, ref, renderSlot, Teleport, Transition } from "vue"

  import CalcButton from "@/components/calc/button/index.vue"

  function renderTeleport(to = "body", children: JSX.Element[]) {
    return h(Teleport, { to }, children)
  }

  export default defineComponent({
    name: "i-dialog",
    props: {
      visible: {
        type: Boolean,
        default: () => false
      },
      class: {
        type: String
      },
      mask: {
        type: Boolean,
        default: () => false
      },
      //模态框
      modal: {
        type: Boolean,
        default: () => false
      },
      title: {
        type: String,
        default: () => "提示"
      },
      okButton: {
        type: [String, Boolean],
        default: "确定"
      },
      cancelButton: {
        type: [String, Boolean],
        default: "取消"
      },
      closeOnYes: {
        type: Boolean,
        default: () => true
      },
      closeOnCancel: {
        type: Boolean,
        default: () => true
      },
      cache: {
        //维持窗口状态
        type: Boolean,
        default: () => true
      }
    },
    emits: ["close", "ok", "cancel", "update:visible"],
    setup(props, { emit, slots }) {
      const dialogRef = ref<HTMLElement | null>(null)

      const model = useVModel(props, "visible")

      const visible = ref(props.visible)

      syncRef(model, visible, { direction: "both" })

      onClickOutside(dialogRef, () => !props.modal && emit("update:visible", false))

      function onOkClick() {
        emit("ok")
        if (props.closeOnYes) {
          visible.value = false
        }
      }

      function onCancelClick() {
        emit("cancel")
        if (props.closeOnCancel) {
          visible.value = false
        }
      }

      function onCloseClick() {
        emit("close")
        if (props.cache) {
          visible.value = false
        }
      }

      function renderAction() {
        if (props.okButton || props.cancelButton) {
          const buttons: JSX.Element[] = []
          if (props.okButton) {
            buttons.push(
              <CalcButton class="mx-2px" type="primary" onClick={onOkClick}>
                {props.okButton === true ? "确定" : props.okButton}
              </CalcButton>
            )
          }
          if (props.cancelButton) {
            buttons.push(
              <CalcButton class="mx-2px" onClick={onCancelClick}>
                {props.cancelButton === true ? "取消" : props.cancelButton}
              </CalcButton>
            )
          }

          return <div class="flex items-center justify-center">{buttons}</div>
        }
      }

      const { x, y, style } = useDraggable(dialogRef, {
        initialValue: { x: 0, y: 0 }
      })

      const isFixed = computed(() => x.value + y.value > 0)

      return () => {
        return (
          <Teleport to="body">
            <Transition name="dialog" mode="out-in">
              {(props.cache || visible.value) && (
                <div v-show={visible.value} class={["dialog-mask w-full h-full fixed top-0 left-0 z-999 flex justify-center items-center "].concat(props.mask ? "bg-hex-000 bg-opacity-66" : "")}>
                  <div ref={dialogRef} class={["h-auto shadow-sm round-1 dialog min-w-48", isFixed.value ? "fixed" : "", props.class]} style={style.value}>
                    <div class="bg-gradient-to-t flex from-hex-273e69 to-hex-335793 h-4 px-1 leading-4  z-9999 justify-center app-title layout-title relative">
                      <div class="text-xs header">{props.title}</div>
                      <div class="flex top-0 right-0 bottom-0 items-center absolute">
                        <div onClick={onCloseClick} class="cursor-pointer flex  h-4 text-center text-hex-f0d070  text-opacity-72 w-4  items-center close-icon hover:text-opacity-100"></div>
                      </div>
                    </div>
                    <div class="bg-hex-000 bg-opacity-92 text-white text-xs py-2  px-4">
                      <div class="flex mt-2 mb-4 items-center"> {renderSlot(slots, "default")}</div>
                      {renderAction()}
                    </div>
                  </div>
                </div>
              )}
            </Transition>
          </Teleport>
        )
      }
    }
  })
</script>
<style lang="scss" scoped>
  .dialog-enter-active {
    animation: fade-in 400ms;
  }
  .dialog-leave-active {
    animation: fade-in reverse 400ms;
  }

  .dialog-enter-active > .dialog {
    animation: zoom-in 400ms;
  }
  .dialog-leave-active > .dialog {
    animation: zoom-out 400ms;
  }
</style>
