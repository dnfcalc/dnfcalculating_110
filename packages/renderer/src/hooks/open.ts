import { useDialog } from "@/components/hooks/dialog"
import { MaybeRef } from "@vueuse/core"
import { h, isRef } from "vue"
import { useRouter } from "vue-router"

interface UseOpenOption {
  url?: MaybeRef<string> | (() => string)
  /*
  
  */
  width?: number
  height?: number

  /**
   * 是否打开新页面
   */
  target?: "_blank" | "_self" | false
}

export function useOpenWindow(opt?: UseOpenOption & { immediate?: boolean }) {
  const { show, close, randomId } = useDialog()
  const router = useRouter()

  const fn = async ({ width, height, target, url: maybeUrl }: UseOpenOption = {}) => {
    width = width ?? opt?.width ?? 0
    height = height ?? opt?.height ?? 0
    target = target ?? opt?.target ?? "_self"
    maybeUrl = maybeUrl ?? opt?.url

    let url = isRef(maybeUrl) ? maybeUrl.value : typeof maybeUrl === "function" ? maybeUrl() : maybeUrl
    if (!url) {
      console.log(opt, width, height, maybeUrl)
      return
    }

    if (url.startsWith("/") || url.startsWith("#")) {
      url = `${location.origin}${router.resolve(url).href}`
    }
    try {
      let _target = target
      if (!target) {
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

      console.log(target)

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
      const router = useRouter()
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

  if (opt?.immediate) {
    fn()
  }

  return fn
}
