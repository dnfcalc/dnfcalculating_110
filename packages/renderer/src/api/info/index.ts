import { IAdventureInfo, IEquipmentList, IEnchantingInfo } from "./type"
import { defineRequest } from "../common"

export default defineRequest(request => {
  return {
    getAdventure() {
      return request.get<IAdventureInfo[]>("/adventure")
    },
    getEquipments() {
      return request.get<IEquipmentList>(`/equips`)
    },
    getEquipmentDetail(euqID: ID) {
      return request.get<any>(`/equip/${euqID}`)
    },
    getEnchanting() {
      return request.get<IEnchantingInfo[]>("/enchanting")
    }
  }
})
