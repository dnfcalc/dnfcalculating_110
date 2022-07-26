import { defineRequest } from "../common"
import { Dress, IAdventureInfo, IDetailsInfo, IEnchantingInfo, IEquipmentList, IJadeInfo, IRecommendInfo, IRecommendRequest, ITrigger } from "./type"

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
    triggers() {
      return request.get<ITrigger[]>("/triggers")
    },
    entries() {
      return request.get<Record<string, { attack: number; buff: number; props: string[] }>>("/entries")
    },
    recommends(params: IRecommendRequest, source: string = "skycity") {
      if (source == "colg") {
        return request.get<PagingData<IRecommendInfo>>("/colg/recommend", { params }).then(r => r as unknown as PagingData<IRecommendInfo>)
      }
      return request.get<PagingData<IRecommendInfo>>("/skycity/recommend", { params }).then(r => r as unknown as PagingData<IRecommendInfo>)
    },
    detailList() {
      return request.get<IDetailsInfo>("/details")
    }
  }
})
