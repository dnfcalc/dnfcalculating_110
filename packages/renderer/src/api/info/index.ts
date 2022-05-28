import { IAdventureInfo, IEquipmentList, IEnchantingInfo, IJadeInfo, ITrigger } from "./type"
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
    },
    getEmblems() {
      return request.get<IEnchantingInfo[]>("/emblem")
    },
    getJade() {
      return request.get<IJadeInfo[]>("/jade")
    },
    getSundry() {
      return request.get<IEnchantingInfo[]>("/sundry")
    },
    getTriggerList() {
      return request.get<ITrigger[]>("/triggerlist")
    },
    getEntryList() {
      return request.get<Record<string, { attack: number; buff: number; props: string[] }>>("/entrylist")
    }
  }
})
