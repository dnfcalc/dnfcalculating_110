import { defineStore } from "pinia"
import { GetAdventureInfo, GetEquipmentInfo, GetEquipmentDetailInfo } from "../api/info"
import { IAdventureInfo, IEquipmentList } from "../api/info/type"

interface BasicInfoState {
  // 冒险团信息
  _adventureInfo: IAdventureInfo[][]
  // 版本信息
  version: string
  // 用户识别码
  UID: string
  // 黑名单
  blacklist: []
  // 通知信息
  noticeInfo: []
  // 所有装备信息
  _equipmentInfo: IEquipmentList | undefined
}

export const useBasicInfoStore = defineStore("basicInfo", {
  state: (): BasicInfoState => {
    return {
      _adventureInfo: [],
      version: "0.0.0.0",
      UID: "西瓜",
      blacklist: [],
      noticeInfo: [],
      _equipmentInfo: undefined
    }
  },
  getters: {
    equipment_info(state) {
      if (!state._equipmentInfo) {
        GetEquipmentInfo().then(res => (state._equipmentInfo = res.data))
      }
      return state._equipmentInfo
    },
    adventure_info(state) {
      if (state._adventureInfo.length === 0) {
        GetAdventureInfo().then(res => (state._adventureInfo = res.data))
      }
      return state._adventureInfo
    }
  },
  actions: {
    async get_equipment_detail(equ_id: number) {
      return (await GetEquipmentDetailInfo(equ_id))?.data
    }
  }
})
