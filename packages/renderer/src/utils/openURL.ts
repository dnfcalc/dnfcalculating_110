import querystring from "query-string"
import { useRouter } from "vue-router"

interface OpenUrlOption {
  query?: Record<string, string | string[]>
  width?: number
  height?: number
}

export default function openURL(url: string, { query = {}, width = 0, height = 0 }: OpenUrlOption = {}) {
  try {
    if (width * height > 0) {
      if (window.ipcRenderer) {
        window.ipcRenderer.invoke("open-win", {
          url: querystring.stringifyUrl({ url, query }),
          width,
          height
        })
      } else {
        window.open("#" + url, "_blank")
      }
    } else {
      window.open(url, "_blank")
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
