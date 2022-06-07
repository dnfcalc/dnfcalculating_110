import api from "@/api"
import { defineStore } from "pinia"

interface IDetailStore {
  part: string
  display_parts: string[]
  standard_uuid: ID
  _standard: any
}

export const useDetailsStore = defineStore("details", {
  state: (): IDetailStore => {
    return {
      part: "头肩",
      display_parts: ["头肩", "上衣", "下装", "腰带", "鞋", "武器", "称号", "手镯", "项链", "辅助装备", "戒指", "耳环", "魔法石", "宠物"],
      standard_uuid: undefined,
      _standard: undefined
    }
  },

  actions: {
    setPart(part: string) {
      this.part = part
    },
    setStandard(uuid: ID) {
      this.standard_uuid = uuid
      this._standard = undefined
    }
  },
  getters: {
    standard(state) {
      if (!state._standard && state.standard_uuid) {
        api.getResult(state.standard_uuid as string).then(res => (state._standard = res))
      }
      return state._standard
    }
  }
})
