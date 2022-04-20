import type { Router } from "vue-router"

export default function openURL(url: string, { width = 0, height = 0 } = {}, router?: Router) {
  try {
    if (width * height > 0) {
      window.ipcRenderer.invoke("open-win", {
        url: url,
        width,
        height
      })
    } else {
      if (router) {
        url = router.resolve({
          path: url
        }).href
      }
      console.log(url)
      window.open(url, "_blank")
    }
  } catch (err) {
    console.error(err)
    // router.push(url)
  }
}
