import { inject, onUnmounted, h, ref } from "vue"
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

  async function confirm(option: DialogOption = {}) {
    return new Promise<DialogResult>((resolve, reject) => {
      const dialog = h(
        DialogComponent,
        {
          onClose() {
            resolve({
              status: "close"
            })
          },
          onCancel() {
            resolve({
              status: "cancel"
            })
          },
          onYes() {
            resolve({
              status: "ok"
            })
          }
        },
        option.content ?? []
      )

      open(randomId(), dialog)

      if (option.timeout) {
        setTimeout(() => {
          resolve({
            status: "close"
          })
        }, option.timeout)
      }
    })
  }

  async function show(option: DialogOption = {}) {
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
          visible: true,
          cancelButton: false,
          onClose() {
            returnResult()
          },
          onCancel() {
            returnResult("cancel")
          },
          onYes() {
            returnResult("ok")
          }
        },
        {
          default() {
            return option.content ?? []
          }
        }
      )

      open(id, dialog)

      if (option.timeout) {
        setTimeout(returnResult, option.timeout)
      }
    })
  }

  async function alert(option: DialogOption = {}) {
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
          visible: true,
          cancelButton: false,
          onClose() {
            returnResult()
          },
          onCancel() {
            returnResult("cancel")
          },
          onYes() {
            returnResult("ok")
          }
        },
        {
          default() {
            return option.content ?? []
          }
        }
      )

      open(id, dialog)

      if (option.timeout) {
        setTimeout(returnResult, option.timeout)
      }
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
  confirm(option: DialogOption): Promise<DialogResult>
}

interface DialogOption {
  title?: string
  content?: ElementLike
  cache?: boolean
  timeout?: number
}

interface DialogResult {
  status: "ok" | "cancel" | "close"
  data?: any
}
