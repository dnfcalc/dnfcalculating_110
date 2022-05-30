import { defineStore } from "pinia"
import { renderList, h } from "vue"

export type ConfirmDialogOption = Omit<ShowDialogOption, "okButton" | "cancelButton">
export type AlertDialogOption = Omit<ShowDialogOption, "okButton" | "cancelButton">
import DialogComponent from "@/components/calc/dialog/index.vue"
export type ElementLike = JSX.Element | string | ElementLike[]

function randomId() {
  return Symbol(Math.random().toString(36).slice(2, 9))
}

export interface ShowDialogOption {
  title?: string
  content?: (() => ElementLike) | ElementLike
  action?: (() => ElementLike) | ElementLike
  cache?: boolean
  timeout?: number
  cancelButton?: string | boolean
  okButton?: string | boolean
}

export interface DialogInstance {
  id?: ID
  render: () => ElementLike
}

export interface DialogResult {
  status: "ok" | "cancel" | "close"
  data?: any
}

export const useContainerStore = defineStore("container", {
  state: () => {
    return {
      dialogs: new Map<ID, DialogInstance>()
    }
  },

  actions: {
    //注册窗口
    open(dialog: DialogInstance) {
      const id = dialog.id ?? randomId()
      this.dialogs.set(id, dialog)
      return id
    },
    close(id: ID) {
      return this.dialogs.delete(id)
    },
    render() {
      return renderList(Array.from(this.dialogs.values()), e => e.render())
    },
    async show(option: ShowDialogOption = {}) {
      return new Promise<DialogResult>((resolve, reject) => {
        const id = randomId()

        const returnResult = (status: DialogResult["status"] = "close") => {
          this.close(id)
          resolve({
            status
          })
        }
        const render = () =>
          h(
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
              action: typeof option.action == "function" ? option.action : () => option.action
            }
          )

        this.open({ id, render })

        if (option.timeout) {
          setTimeout(returnResult, option.timeout)
        }
      })
    },

    async alert(option: AlertDialogOption = {}) {
      return this.show({
        ...option,
        okButton: true,
        cancelButton: false
      })
    },
    async confirm(option: ConfirmDialogOption = {}) {
      return this.show({
        ...option,
        okButton: true,
        cancelButton: true
      })
    }
  }
})
