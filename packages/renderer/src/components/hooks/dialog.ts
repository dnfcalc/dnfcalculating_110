import { renderList, h, reactive, readonly } from "vue"

export type ConfirmDialogOption = Omit<ShowDialogOption, "okButton" | "cancelButton">
export type AlertDialogOption = Omit<ShowDialogOption, "okButton" | "cancelButton">
import ActionDialog from "@/components/calc/action-dialog/index.vue"
import { createSharedComposable } from "@vueuse/core"
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
  rejectButton?: string | boolean

  // 默认状态
  defaultStatus?: DialogResult["status"]
}

export interface DialogInstance {
  id?: ID
  render: () => ElementLike
}

export interface DialogResult {
  status: "ok" | "reject" | "cancel" | "none"
  readonly isOk: boolean
  readonly isCancel: boolean
  readonly isReject: boolean
  data?: any
}

export const useDialog = createSharedComposable(() => {
  const dialogs = reactive(new Map<ID, DialogInstance>())

  //注册窗口
  function open(dialog: DialogInstance) {
    const id = dialog.id ?? randomId()
    dialogs.set(id, dialog)
    return id
  }

  function close(id: ID) {
    return dialogs.delete(id)
  }

  function render() {
    return renderList(Array.from(dialogs.values()), e => e.render())
  }

  async function show(option: ShowDialogOption = {}) {
    return new Promise<DialogResult>((resolve, reject) => {
      const id = randomId()
      const { content, action, defaultStatus = "none" } = option

      console.log(action)

      const onClose = (status: DialogResult["status"] = defaultStatus) => {
        close(id)
        resolve({
          status,
          get isOk() {
            return status == "ok"
          },
          get isCancel() {
            return status == "cancel"
          },
          get isReject() {
            return status == "reject"
          }
        })
      }

      open({
        id,
        render() {
          return h(
            ActionDialog,
            {
              title: option.title,
              visible: true,
              okButton: option.okButton ?? false,
              cancelButton: option.cancelButton ?? false,
              rejectButton: option.rejectButton ?? false,
              onClose
            },
            {
              default() {
                switch (typeof content) {
                  case "function":
                    return content()
                  case "string":
                    return h("div", { class: "w-full justify-center text-hex-d4d6b6 text-center" }, option.content)
                  default:
                    return content
                }
              },
              action: typeof action == "function" || !action ? action : () => action
            }
          )
        }
      })

      if (option.timeout) {
        setTimeout(onClose, option.timeout)
      }
    })
  }

  async function alert(option: AlertDialogOption = {}) {
    return show({
      ...option,
      defaultStatus: "ok",
      okButton: true,
      cancelButton: false
    })
  }

  async function confirm(option: ConfirmDialogOption = {}) {
    return show({
      ...option,
      defaultStatus: "cancel",
      okButton: true,
      cancelButton: true
    })
  }
  return {
    confirm,
    alert,
    render,
    show
  }
})
