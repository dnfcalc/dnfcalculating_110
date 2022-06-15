import { IAdventureInfo, IEquipmentList, IEnchantingInfo, IJadeInfo, ITrigger, Dress } from "./type"
import { defineRequest } from "../common"

export default defineRequest(request => {
  return {
    getAdventure() {
      return request.get<IAdventureInfo[]>("/adventure")
    },
    getEquipments() {
      return request.get<IEquipmentList>(`/equips`)
    },
    getEquipmentDetail(equipId: ID) {
      return request.get<any>(`/equip/${String(equipId)}`)
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
    getsundries() {
      return request.get<IEnchantingInfo[]>("/sundries")
    },
    gettriggers() {
      return request.get<ITrigger[]>("/triggers")
    },
    getentries() {
      return request.get<Record<string, { attack: number; buff: number; props: string[] }>>("/entries")
    },
    getDressList() {
      return request.get<Record<string, Dress[]>>("/dress")
    }
  }
})
