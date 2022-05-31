import { defineRequest } from "../common"

export default defineRequest(axios => {
  return {
    heartbeat() {
      return axios.get("/heartbeat", { timeout: 1000 })
    },
    checkUpdate(version: string) {
      return axios.post("/checkUpdate", { version: version }, { timeout: 5000 }).then(r => r.data)
    },
    autoUpdate() {
      axios.post("/autoUpdate")
    }
  }
})
