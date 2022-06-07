import { renderList, h, reactive, readonly, ref } from "vue"

export type ConfirmDialogOption = Omit<ShowDialogOption, "okButton" | "cancelButton">
export type AlertDialogOption = Omit<ShowDialogOption, "okButton" | "cancelButton">
import ActionDialog from "@/components/calc/action-dialog/index.vue"
import { createSharedComposable } from "@vueuse/core"
export type ElementLike = JSX.Element | string | ElementLike[]

function randomId() {
  return Symbol(Math.random().toString(36).slice(2, 9))
}

type DialogID = string | number | symbol

export interface ShowDialogOption {
  id?: DialogID
  /**
   * 标题
   */
  header?: string | boolean
  /**
   * 内容插槽
   */
  content?: (() => ElementLike) | ElementLike
  /**
   * 操作区插槽
   */
  action?: (() => ElementLike) | ElementLike

  cache?: boolean

  /**
   * 超时自动关闭
   */
  timeout?: number

  /**
   * 关闭时的延迟动画
   */
  duration?: number

  /**
   * 确定按钮文本 为false时不显示
   */
  okButton?: string | boolean
  /**
   * 取消按钮文本 为false时不显示
   */
  cancelButton?: string | boolean
  /**
   * 拒绝按钮文本 为false时不显示
   */
  rejectButton?: string | boolean

  // 默认状态
  defaultStatus?: DialogResult["status"]
}

export interface DialogInstance {
  id?: DialogID
  render: () => ElementLike
}

export interface DialogResult {
  id: DialogID
  status: "ok" | "reject" | "cancel" | "none"
  data?: any
  readonly isOk: boolean
  readonly isCancel: boolean
  readonly isReject: boolean
}

export const useDialog = createSharedComposable(() => {
  const dialogs = reactive(new Map<DialogID, DialogInstance>())

  //注册窗口
  function open(dialog: DialogInstance) {
    const id = dialog.id ?? randomId()
    dialogs.set(id, dialog)
    return id
  }

  function close(id: DialogID) {
    return dialogs.delete(id)
  }

  function render() {
    return renderList(dialogs.values(), e => e.render())
  }

  async function show(option: ShowDialogOption = {}) {
    return new Promise<DialogResult>(resolve => {
      const { id = randomId(), header = true, content, action, timeout, okButton = false, cancelButton = false, rejectButton = false, defaultStatus = "none", duration = 400 } = option

      const onClose = (status: DialogResult["status"] = defaultStatus) => {
        const fn = () => {
          close(id)
          resolve({
            id,
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
        if (duration) {
          setTimeout(fn, duration)
        } else {
          fn()
        }
      }

      open({
        id,
        render() {
          return h(
            ActionDialog,
            {
              header,
              okButton,
              cancelButton,
              rejectButton,
              visible: true,
              onClose
            },
            {
              default() {
                switch (typeof content) {
                  case "function":
                    return content()
                  case "string":
                    return h("div", { class: "w-full justify-center text-hex-d4d6b6 text-center" }, content)
                  default:
                    return content
                }
              },
              action: typeof action == "function" || !action ? action : () => action
            }
          )
        }
      })

      if (timeout) {
        setTimeout(onClose, timeout)
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
    show,
    close,
    randomId
  }
})
