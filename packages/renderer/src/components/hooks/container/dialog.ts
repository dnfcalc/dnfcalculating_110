import { inject, onUnmounted, h, ref, nextTick } from "vue"
import { REGISTER_DILOAG } from "./constants"
import { ElementLike, RegisterFunction } from "./types"

import DialogComponent from "@/components/calc/dialog/index.vue"

function randomId() {
  return Math.random().toString(36).slice(2, 9)
}

export function useDialog(id?: string) {
  id = id ?? randomId()
  const register = inject(REGISTER_DILOAG) as RegisterFunction
  const { unmount, open, close } = register(id)

  async function confirm(option: ShowDialogOption = {}) {
    return show({
      ...option,
      okButton: "确定",
      cancelButton: "取消"
    })
  }

  async function show(option: ShowDialogOption = {}) {
    return new Promise<DialogResult>((resolve, reject) => {
      const id = randomId()

      function returnResult(status: DialogResult["status"] = "close") {
        close(id)
        resolve({
          status
        })
      }

      const dialog = h(
        DialogComponent,
        {
          title: option.title,
          visible: true,
          okButton: option.okButton ?? false,
          cancelButton: option.cancelButton ?? false,
          onClose() {
            returnResult()
          },
          onCancel() {
            returnResult("cancel")
          },
          onOk() {
            returnResult("ok")
          }
        },
        {
          default: typeof option.content == "function" ? option.content : () => option.content,
          action: typeof option.content == "function" ? option.action : () => option.action
        }
      )

      open(id, dialog)

      if (option.timeout) {
        setTimeout(returnResult, option.timeout)
      }
    })
  }

  async function alert(option: ShowDialogOption = {}) {
    return show({
      ...option,
      okButton: "确定",
      cancelButton: false
    })
  }

  onUnmounted(unmount)

  return {
    confirm,
    alert,
    show
  }
}

export interface DialogHook {
  confirm(title: string, content: ElementLike): Promise<DialogResult>
  confirm(option: ShowDialogOption): Promise<DialogResult>
}

interface ShowDialogOption {
  title?: string
  content?: (() => ElementLike) | ElementLike
  action?: (() => ElementLike) | ElementLike
  cache?: boolean
  timeout?: number
  cancelButton?: string | false
  okButton?: string | false
}

interface DialogResult {
  status: "ok" | "cancel" | "close"
  data?: any
}
