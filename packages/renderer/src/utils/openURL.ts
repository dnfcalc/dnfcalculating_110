import { useRouter } from "vue-router"

export default function openURL(url: string, { width = 0, height = 0 } = {}) {
  try {
    if (width * height > 0) {
      if (window.ipcRenderer) {
        window.ipcRenderer.invoke("open-win", {
          url: url,
          width,
          height
        })
      } else {
        window.open("#" + url, "_blank")
      }
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
