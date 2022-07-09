import api from "@/api"
import { defineStore } from "pinia"
import { Dress, IDetailsInfo, IEnchantingInfo, IEquipmentInfo, IEquipmentList, IJadeInfo, ITrigger } from "../api/info/type"
import { useCharacterStore } from "./character"

interface BasicInfoState {
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
  _sundriesInfo: IEnchantingInfo[] | undefined
  // 触发词条选择
  _triggers: ITrigger[] | undefined
  _entries: Record<string, { attack: number; buff: number; props: string[] }> | undefined
  _dresses?: Record<string, Dress[]>
  _details: IDetailsInfo | undefined
}

export const useBasicInfoStore = defineStore("basicInfo", {
  state: (): BasicInfoState => ({
    version: "0.0.0.0",
    UID: "西瓜",
    blacklist: [],
    noticeInfo: [],
    _equipmentInfo: undefined,
    _enchantingInfo: undefined,
    _emblemInfo: undefined,
    _jadeInfo: undefined,
    _triggers: undefined,
    _entries: undefined,
    _sundriesInfo: undefined,
    _dresses: undefined,
    _details: undefined
  }),
  getters: {
    equipment_info(state) {
      if (!state._equipmentInfo) {
        api.equips().then(res => {
          state._equipmentInfo = res.data
        })
      }
      return state._equipmentInfo
    },
    equipment_list(state) {
      const info = state._equipmentInfo
      if (info) {
        return [...(info?.lv110 ?? []), ...(info?.myth ?? []), ...(info?.weapon ?? []), ...(info?.wisdom ?? []), ...(info?.title ?? []), ...(info?.pet ?? [])]
      } else {
        api.equips().then(res => {
          state._equipmentInfo = res.data
        })
      }
      return []
    },
    equiment_ids() {
      const list = this.equipment_list as IEquipmentInfo[]
      return list.map(item => item.id)
    },
    equipment_singleset(state) {
      const info = state._equipmentInfo
      if (info) {
        return [...(info?.lv110 ?? []), ...(info?.myth ?? []), ...(info?.weapon ?? []), ...(info?.wisdom ?? [])]
      } else {
        api.equips().then(res => {
          state._equipmentInfo = res.data
        })
      }
      return []
    },
    trigger_list(state) {
      if (!state._triggers) {
        api.triggers().then(res => (state._triggers = res.data))
      }
      return state._triggers
    },
    entry_list(state) {
      if (!state._entries) {
        api.entries().then(res => (state._entries = res.data))
      }
      return state._entries
    },
    details(state) {
      if (!state._details) {
        api.detailList().then(res => (state._details = res.data))
        useCharacterStore().platinum.forEach(item => {
          state._details?.emblem?.push({
            id: item,
            maxFame: 232,
            position: "辅助装备，魔法石",
            props: item + " Lv+1" + " 四维 + 8",
            type: "技能",
            rarity: "白金",
            rate: 2000
          })
        })
      }
      return state._details
    }
  },
  actions: {
    async get_equipment_detail(equ_id: ID) {
      //   console.log(equ_id)
      return (await api.equipmentDetail(equ_id))?.data
    },
    getEquip(id?: ID) {
      if (!!id) {
        return this.equipment_list.find(e => e.id == id)
      }
    }
  }
})
