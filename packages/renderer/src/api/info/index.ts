import { defineRequest } from "../common"
import { Dress, IAdventureInfo, IEnchantingInfo, IEquipmentList, IJadeInfo, IRecommendInfo, IRecommendRequest, ITrigger } from "./type"

export default defineRequest(request => {
  return {
    adventures() {
      return request.get<IAdventureInfo[]>("/adventure")
    },
    equips() {
      return request.get<IEquipmentList>(`/equips`)
    },
    equipmentDetail(equipId: ID) {
      return request.get<any>(`/equip/${String(equipId)}`)
    },
    enchantings() {
      return request.get<IEnchantingInfo[]>("/enchanting")
    },
    emblems() {
      return request.get<IEnchantingInfo[]>("/emblem")
    },
    jades() {
      return request.get<IJadeInfo[]>("/jade")
    },
    sundries() {
      return request.get<IEnchantingInfo[]>("/sundries")
    },
    triggers() {
      return request.get<ITrigger[]>("/triggers")
    },
    entries() {
      return request.get<Record<string, { attack: number; buff: number; props: string[] }>>("/entries")
    },
    dressList() {
      return request.get<Record<string, Dress[]>>("/dress")
    },
    recommends(params: IRecommendRequest) {
      return request.get<PagingData<IRecommendInfo>>("https://dnf.skycity.top:8017/api/DCalc/LoadRecommendPage", { params }).then(r => r as unknown as PagingData<IRecommendInfo>)
    }
  }
})
