import { defineRequest } from "../common"
import { IAnyResultInfo, ICharacterInfo } from "./type"

export default defineRequest(request => {
  return {
    getCharacter() {
      return request.get<ICharacterInfo>(`/character`).then(r => r.data)
    },
    calc(params: any, single: boolean = false) {
      return request.post<IAnyResultInfo>(single ? "/calc/single" : "/calc", params).then(r => r.data)
    },
    getResult(id: string) {
      return request.get<IAnyResultInfo>(`/calc/result/${id}`).then(r => r.data)
    }
  }
})
