import { ICharacterInfo } from "./type"
import { defineRequest } from "../common"

export default defineRequest(request => {
  return {
    getCharacter() {
      return request.get<ICharacterInfo>(`/character`).then(r => r.data)
    }
  }
})
