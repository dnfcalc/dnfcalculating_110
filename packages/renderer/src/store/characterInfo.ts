import { IStoreInfo } from "@/api/info/type"
import { defineStore } from "pinia"
import { GetCharacterInfo } from "../api/character"
import { ICharacterInfo } from "../api/character/type"
import { useStoreInfoStore } from "./storeInfo"

export interface CharacterInfo {
  // 类名
  name: string
  // 基础信息
  _basicInfo?: ICharacterInfo | undefined
  // 存档信息
  _storeInfo?: IStoreInfo
}

export const useCharacterStore = defineStore("CharacterInfo", {
  state(): CharacterInfo {
    return {
      name: "",
      _storeInfo: {
        detailInfo: {}
      }
    }
  },
  getters: {
    basic_info(state) {
      if (!state._basicInfo) {
        GetCharacterInfo(state.name).then(res => (state._basicInfo = res.data))
      }
      return state._basicInfo
    },
    store_info(state) {
      if (!state._storeInfo) {
        // 取存档
        state._storeInfo = useStoreInfoStore().store_info
      }
      return state._storeInfo
    }
  },
  actions: {
    current_char(name: string) {
      this.name = name
    },
    getDetailData(part: string, key: string) {
      const partInfo = this.store_info?.detailInfo?.[part]
      if (partInfo) {
        return partInfo.get(key)
      }
    },
    setColumnData(part: string, key: string, value: any) {}
  }
})
