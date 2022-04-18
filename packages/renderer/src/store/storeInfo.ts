import { IStoreInfo } from "@/api/info/type"
import { defineStore } from "pinia"
import { useCharacterStore } from "./characterInfo"

interface StoreInfo {
  storeName: string
  _storeInfo: IStoreInfo | undefined
}

export const useStoreInfoStore = defineStore("StoreInfo", {
  state(): StoreInfo {
    return { storeName: "set", _storeInfo: undefined }
  },
  getters: {
    store_info(state) {
      if (!state._storeInfo) {
        // 取存档
      }
      return state._storeInfo
    }
  },
  actions: {
    async changeStore(storeName: string) {
      if (this.storeName !== storeName) {
        // 先保存当前存档
        await this.saveStore()
        //取新的存档
        this.storeName = storeName
        this._storeInfo = undefined
      }
      useCharacterStore()._storeInfo = this.store_info
    },
    saveStore() {
      const tempStore = useCharacterStore().store_info
      // 提交到后端
    }
  }
})
