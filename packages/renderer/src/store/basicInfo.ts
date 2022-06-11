import { useCharacterStore } from "./character"
import { defineStore } from "pinia"
import api from "@/api"
import { IAdventureInfo, IEnchantingInfo, IEquipmentList, IJadeInfo, ITrigger } from "../api/info/type"

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
  // 所有徽章信息
  _emblemInfo: IEnchantingInfo[] | undefined
  // 辟邪玉信息
  _jadeInfo: IJadeInfo[] | undefined
  // 杂项信息
  _sundryInfo: IEnchantingInfo[] | undefined
  // 触发词条选择
  _triggerList: ITrigger[] | undefined
  _entryList: Record<string, { attack: number; buff: number; props: string[] }> | undefined
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
      _enchantingInfo: undefined,
      _emblemInfo: undefined,
      _jadeInfo: undefined,
      _triggerList: undefined,
      _entryList: undefined,
      _sundryInfo: undefined
    }
  },
  getters: {
    equipment_info(state) {
      if (!state._equipmentInfo) {
        api.getEquipments().then(res => (state._equipmentInfo = res.data))
      }
      this.entry_list
      return state._equipmentInfo
    },
    equipment_list(state) {
      if (!state._equipmentInfo) {
        api.getEquipments().then(res => (state._equipmentInfo = res.data))
      }
      return [
        ...(state._equipmentInfo?.lv110 ?? []),
        ...(state._equipmentInfo?.myth ?? []),
        ...(state._equipmentInfo?.weapon ?? []),
        ...(state._equipmentInfo?.wisdom ?? []),
        ...(state._equipmentInfo?.title ?? []),
        ...(state._equipmentInfo?.pet ?? [])
      ]
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
    },
    emblem_info(state) {
      if (!state._emblemInfo) {
        api.getEmblems().then(res => {
          state._emblemInfo = res.data
          useCharacterStore().platinum.forEach(item => {
            state._emblemInfo?.push({
              id: item,
              maxFrame: 232,
              position: "辅助装备，魔法石",
              props: item + " Lv+1",
              type: "技能",
              rarity: "白金"
            })
          })
        })
      }
      return state._emblemInfo
    },
    jade_info(state) {
      if (!state._jadeInfo) {
        api.getJade().then(res => (state._jadeInfo = res.data))
      }
      return state._jadeInfo
    },
    sundry_info(state) {
      if (!state._sundryInfo) {
        api.getSundry().then(res => (state._sundryInfo = res.data))
      }
      return state._sundryInfo
    },
    trigger_list(state) {
      if (!state._triggerList) {
        api.getTriggerList().then(res => (state._triggerList = res.data))
      }
      return state._triggerList
    },
    entry_list(state) {
      if (!state._entryList) {
        api.getEntryList().then(res => (state._entryList = res.data))
      }
      return state._entryList
    }
  },
  actions: {
    async get_equipment_detail(equ_id: number) {
      return (await api.getEquipmentDetail(equ_id))?.data
    }
  }
})
