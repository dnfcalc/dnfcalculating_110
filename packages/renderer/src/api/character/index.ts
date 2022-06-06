import { ICharacterInfo, IResultInfo } from "./type"
import { defineRequest } from "../common"

export default defineRequest(request => {
  return {
    getCharacter() {
      return request.get<ICharacterInfo>(`/character`).then(r => r.data)
    },
    calc(params: any, single: boolean = false) {
      return request.post<IResultInfo>(single ? "/calc/single" : "/calc", params).then(r => r.data)
    },
    getResult(id: string) {
      return request.get<IResultInfo>(`/calc/result/${id}`).then(r => r.data)
    }
  }
})
