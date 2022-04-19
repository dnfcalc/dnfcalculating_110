import { useCharacterStore } from "./character"
import { defineStore } from "pinia"
import api from "@/api"
import { IAdventureInfo, IEnchantingInfo, IEquipmentList } from "../api/info/type"

interface BasicInfoState {
  // 冒险团信息
  _adventureInfo: IAdventureInfo[]
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
  // 所有附魔信息
  _enchantingInfo: IEnchantingInfo[] | undefined
}

export const useBasicInfoStore = defineStore("basicInfo", {
  state: (): BasicInfoState => {
    return {
      _adventureInfo: [],
      version: "0.0.0.0",
      UID: "西瓜",
      blacklist: [],
      noticeInfo: [],
      _equipmentInfo: undefined,
      _enchantingInfo: undefined
    }
  },
  getters: {
    equipment_info(state) {
      if (!state._equipmentInfo) {
        api.getEquipments().then(res => (state._equipmentInfo = res.data))
      }
      return state._equipmentInfo
    },
    adventure_info(state) {
      if (state._adventureInfo.length === 0) {
        api.getAdventure().then(res => (state._adventureInfo = res.data))
      }
      return state._adventureInfo
    },
    enchanting_info(state) {
      if (!state._enchantingInfo) {
        api.getEnchanting().then(res => (state._enchantingInfo = res.data))
      }
      return state._enchantingInfo
    }
  },
  actions: {
    async get_equipment_detail(equ_id: number) {
      return (await api.getEquipmentDetail(equ_id))?.data
    }
  }
})
