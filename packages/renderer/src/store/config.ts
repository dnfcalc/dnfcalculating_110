import { defineStore } from "pinia"
import api from "@/api"
import {} from "electron/renderer"

interface ConfigState {
  name: string
  alter: string
  data: Record<string, any>
  token: string
}

export const useConfigStore = defineStore("config", {
  state: (): ConfigState => {
    return { name: "set", alter: "", data: {}, token: "" }
  },
  getters: {},
  actions: {
    async load() {
      this.data = api.getConfig(this.alter, this.name)
    },
    async switch(name: string) {
      await this.save()
      this.name = name
      await api.switchConfig(this.alter, this.name)
    },
    async save() {
      await api.saveConfig(this.alter, this.name, this.data)
    },
    async set(name: string, item: Record<string, any>) {
      this.data[name] = item
    }
  }
})
