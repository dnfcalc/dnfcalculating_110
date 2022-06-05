<script lang="tsx">
  import { onKeyStroke, useVModel } from "@vueuse/core"
  import { defineComponent, PropType, ref, renderSlot } from "vue"

  import CalcDialog from "@/components/calc/dialog/index.vue"
  import CalcButton from "@/components/calc/button/index.vue"

  export type ActionDialogResult = "ok" | "reject" | "cancel" | "none"

  export default defineComponent({
    name: "i-action-dialog",
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
      drag: {
        type: String as PropType<"header" | "all" | "none">,
        default: () => "header"
      },
      okButton: {
        type: [String, Boolean],
        default: "确定"
      },
      rejectButton: {
        type: [String, Boolean],
        default: false
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
      closeOnReject: {
        type: Boolean,
        default: () => true
      },
      closeOnEsc: {
        type: Boolean,
        default: () => true
      },
      cache: {
        //维持窗口状态
        type: Boolean,
        default: () => true
      },
      defaultStatus: {
        type: String as PropType<ActionDialogResult>,
        default: () => "cancel"
      }
    },
    emits: ["close", "ok", "cancel", "action", "update:visible"],
    setup(props, { emit, slots }) {
      const visible = useVModel(props, "visible")

      const result = ref<ActionDialogResult>(props.defaultStatus)

      function close() {
        visible.value = false
        emit("close", result.value)
      }

      onKeyStroke("ESC", (e: Event) => {
        if (visible.value && props.closeOnEsc) {
          e.preventDefault()
          close()
        }
      })

      function onOkClick() {
        result.value = "ok"
        if (props.closeOnYes) {
          close()
        }
      }

      function onRejectClick() {
        result.value = "reject"
        if (props.closeOnReject) {
          close()
        }
      }

      function onCancelClick() {
        result.value = "cancel"
        if (props.closeOnCancel) {
          close()
        }
      }

      function onCloseClick() {
        close()
      }

      function renderAction() {
        if ((props.okButton || props.cancelButton || props.rejectButton) && !slots.action) {
          const buttons: JSX.Element[] = []
          if (props.okButton) {
            buttons.push(
              <CalcButton class="mx-2px" type="primary" onClick={onOkClick}>
                {props.okButton === true ? "确定" : props.okButton}
              </CalcButton>
            )
          }
          if (props.rejectButton) {
            buttons.push(
              <CalcButton class="mx-2px" type="primary" onClick={onRejectClick}>
                {props.rejectButton === true ? "拒绝" : props.rejectButton}
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
        return renderSlot(slots, "action")
      }

      return () => {
        return (
          <CalcDialog onClose={onCloseClick} v-model:visible={visible.value} drag={props.drag} mask={props.mask} modal={props.modal} title={props.title}>
            <div class="pt-2 pb-2">
              <div class="flex mt-2 mb-3 items-center justify-center"> {renderSlot(slots, "default")}</div>
              {renderAction()}
            </div>
          </CalcDialog>
        )
      }
    }
  })
</script>
<style lang="scss" scoped>
  .i-button {
    text-shadow: none;

    color: #a89679;
    background: linear-gradient(#12396b, #081f3c);
    border: 1px solid #554a3d;

    &:hover {
      color: #fee97d;
      background: linear-gradient(#2d4e9f, #153051);
      //  border: 1px solid #e3c18a;
      color: #d4d4b6;
      background: linear-gradient(#195cab, #0b3260);
      border: 1px solid #867760;
    }

    &:active {
      color: #e9c556;
      background: linear-gradient(#2d4e9f, #122438);
      border: 1px solid #e3c18a;
      color: #d4d4b6;
      background: linear-gradient(#195cab, #0b3260);
      border: 1px solid #918168;
    }
  }
</style>
