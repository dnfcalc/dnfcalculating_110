import { ICharacterInfo, IResultInfo } from "./type"
import { defineRequest } from "../common"

export default defineRequest(request => {
  return {
    getCharacter() {
      return request.get<ICharacterInfo>(`/character`).then(r => r.data)
    },
    calc(params: any, single: boolean = false) {
      if (!single) return request.post<IResultInfo>("/calc", params).then(r => r.data)
      else return request.post<IResultInfo>("/calcSingle", params).then(r => r.data)
    }
  }
})
