import { useDialog } from "@/components/hooks/dialog"
import { MaybeRef } from "@vueuse/core"
import { computed, h, isRef, ref } from "vue"
import { useRouter } from "vue-router"

interface UseOpenOption {
  /*
  
  */
  width?: number
  height?: number

  /**
   * 是否打开新页面
   */
  target?: "_blank" | "_self"

  /**
   * 立即打开
   */
  immediate?: boolean
}

export function useOpen(maybeUrl: MaybeRef<string> | (() => string), { width = 0, height = 0, immediate = true, target }: UseOpenOption = {}) {
  const { show, confirm, close, randomId } = useDialog()
  const router = useRouter()

  const fn = async () => {
    let url = isRef(maybeUrl) ? maybeUrl.value : typeof maybeUrl === "function" ? maybeUrl() : maybeUrl

    if (url.startsWith("/") || url.startsWith("#")) {
      url = `${location.origin}${router.resolve(url).href}`
    }
    try {
      if (window.ipcRenderer) {
        window.ipcRenderer.invoke("open-win", {
          url,
          width,
          height
        })
        return
      }

      if (!target) {
        const rs = await show({
          content: "请确认打开新页面的方式",
          okButton: "新窗口",
          rejectButton: "当前窗口",
          cancelButton: true,
          defaultStatus: "cancel"
        })
        if (rs.isOk) {
          target = "_blank"
        } else if (rs.isReject) {
          target = "_self"
        }
      }

      if (target == "_blank") {
        window.open(url, "_blank")
      } else if (target == "_self") {
        const id = randomId()
        const onClose = (e: MessageEvent) => {
          console.log(e)
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
    }
  }

  if (immediate) {
    fn()
  }

  return fn
}
