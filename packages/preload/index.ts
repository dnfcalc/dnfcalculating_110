import { domReady } from "./utils"
import { useLoading } from "./loading"
import { ipcRenderer } from "electron"

const { appendLoading, removeLoading } = useLoading()
window.removeLoading = removeLoading
window.ipcRenderer = ipcRenderer
domReady().then(appendLoading)
