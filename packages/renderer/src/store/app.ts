import { defineStore } from "pinia"

interface AppState {
  title: string
  id?: number
}

export const useAppStore = defineStore("app", {
  state(): AppState {
    return {
      title: "DNF计算器 & Colg",
      id: undefined
    }
  },
  actions: {
    minimize() {
      if (window.ipcRenderer) {
        window.ipcRenderer.invoke("minimize-win")
      } else {
        window.parent.postMessage("minimize-win", location.origin)
      }
    },
    close() {
      if (window.ipcRenderer) {
        window.ipcRenderer.invoke("close-win")
      } else {
        window.parent.postMessage("close", location.origin)
      }
    }
  }
})
