import type { Router } from "vue-router"

export default function openURL(url: string, { width = 0, height = 0 } = {}, router?: Router) {
  try {
    if (width * height > 0) {
      if (window.ipcRenderer) {
        window.ipcRenderer.invoke("open-win", {
          url: url,
          width,
          height
        })
      } else {
        router?.push(url)
      }
    } else {
      if (router) {
        url = router.resolve({ path: url }).href
      }
      window.open(url, "_blank")
    }
  } catch (err) {
    // let routerURL = router?.resolve({
    //   path: url
    // })
    // window.open(routerURL?.href)
    // router.push(url)
    // 网页端打开
    router?.push(url)
  }
}
