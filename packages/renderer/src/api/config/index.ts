import { defineRequest } from "../common"

export default defineRequest(req => {
  return {
    getConfig(name: string) {
      return req.get<Record<string, any>>(`/config/${name}`).then(r => r.data)
    },
    getConfigList() {
      return req.get<string[]>(`/configs`).then(r => r.data)
    },
    switchConfig(name: string) {
      return req.post("/config/switch", name).then(r => r.data)
    },
    saveConfig(name: string, data: Record<string, any>) {
      return req.post("/config/save", { name, data }).then(r => r.data)
    },
    getToken(alter: string) {
      return req.get<string>(`/token/${alter}`).then(r => r.data)
    }
  }
})
