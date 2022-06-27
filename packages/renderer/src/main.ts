import App from "@/pages/index.vue"
import { createApp } from "vue"
import router from "./router"
import { pinia } from "./store"

import "uno.css"

import "./app.scss"

createApp(App).use(pinia).use(router).mount("#app")

setTimeout(window.removeLoading, 5000)

// console.log('fs', window.fs)
// console.log('ipcRenderer', window.ipcRenderer)

// Usage of ipcRenderer.on
// window.ipcRenderer.on("main-process-message", (_event, ...args) => {
//   console.log("[Receive Main-process message]:", ...args);
// });
