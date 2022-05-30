import { defineRequest } from "../common"

export default defineRequest(axios => {
  return {
    heartbeat() {
      return axios.get("/heartbeat", { timeout: 1000 })
    }
  }
})
