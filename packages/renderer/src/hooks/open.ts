import { useDialog } from "@/components/hooks/dialog"
import { MaybeRef } from "@vueuse/core"
import querystring from "query-string"
import { h, isRef } from "vue"
import { useRouter } from "vue-router"

interface UseOpenOption {
  /*

  */
  width?: number
  height?: number
  query?: Record<string, string | string[] | undefined>

  /**
   * 是否打开新页面
   */
  target?: "_blank" | "_self" | false
}

export function useOpenWindow(opt?: UseOpenOption & { immediate?: boolean }) {
  const { show, close, randomId } = useDialog()
  const router = useRouter()

  return async (maybeUrl: MaybeRef<string> | (() => string), { width = 0, height = 0, target = "_self", query = {} }: UseOpenOption = {}) => {
    let url = isRef(maybeUrl) ? maybeUrl.value : typeof maybeUrl === "function" ? maybeUrl() : maybeUrl
    if (!url) {
      console.log(opt, width, height, maybeUrl)
      return
    }

    if (url.startsWith("/")) {
      url = router.resolve(url).href
    }
    url = querystring.stringifyUrl({ url, query })
    try {
      let _target = target
      if (!_target) {
        const rs = await show({
          content: "请确认打开新页面的方式",
          okButton: "当前窗口",
          rejectButton: "新窗口",
          cancelButton: true,
          defaultStatus: "cancel"
        })
        if (rs.isOk) {
          _target = "_self"
        } else if (rs.isReject) {
          _target = "_blank"
        }
      }

      if (_target == "_blank" || width * height < 1) {
        window.open(url, "_blank")
      } else if (_target == "_self") {
        if (window.ipcRenderer) {
          window.ipcRenderer.invoke("open-win", {
            url,
            width,
            height
          })
          return
        }

        const id = randomId()
        const onClose = (e: MessageEvent) => {
          if (e.data == "close") {
            close(id)
          }
        }
        window.addEventListener("message", onClose)
        await show({
          id,
          header: false,
          content() {
            return h("iframe", {
              name: Math.random().toString(36).slice(2),
              referrerpolicy: "no-referrer",
              frameborder: 0,
              src: url,
              style: {
                width: `${width}px`,
                height: `${height}px`
              }
            })
          }
        })
        window.removeEventListener("message", onClose)
      }
    } catch (err) {
      // let routerURL = router?.resolve({
      //   path: url
      // })
      // window.open(routerURL?.href)
      // router.push(url)
      // 网页端打开
      router?.push(url)
      console.error(err)
    }
  }
}
