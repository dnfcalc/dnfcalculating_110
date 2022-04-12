import type { Router } from "vue-router"

export default function openURL(
  router: Router,
  url: string,
  args: { width: number; height: number }
) {
  try {
    if (args.height > window.screen.height * 0.8)
      args.height = window.screen.height * 0.8
    window.ipcRenderer.invoke("open-win", {
      url: url,
      ...args
    })
  } catch (err) {
    let routerURL = router.resolve({
      path: url
    })
    window.open(routerURL.href, "_blank")
    // router.push(url)
  }
}
