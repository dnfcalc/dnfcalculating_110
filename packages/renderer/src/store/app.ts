import { defineStore } from "pinia"

interface AppState {
  title: string
  id?: number
}

export const useAppStore = defineStore("app", {
  state(): AppState {
    return {
      title: "DNF计算器搭配计算器 & Colg",
      id: undefined
    }
  },
  actions: {
    minimize() {
      window.ipcRenderer.invoke("minimize-win")
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
