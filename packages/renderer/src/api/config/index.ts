import { defineRequest } from "../common"

export default defineRequest(req => {
  return {
    getConfig(alter: string, name: string) {
      return req.get<Record<string, any>>(`/config/${name}`).then(r => r.data)
    },
    switchConfig(alter: string, name: string) {
      return req.post("/config/switch", { alter, name }).then(r => r.data)
    },
    saveConfig(alter: string, name: string, data: Record<string, any>) {
      return req.post("/config/save", { alter, name, data }).then(r => r.data)
    },
    getToken(alter: string) {
      return req.get<string>(`/token/${alter}`).then(r => r.data)
    }
  }
})
