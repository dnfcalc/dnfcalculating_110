import api from "@/api"
import { ICharacterInfo } from "@/api/character/type"
import { useConfigStore } from "@/store/config"
import { defineStore } from "pinia"

export interface CharacterInfo extends ICharacterInfo {
  // 基础信息
}

export const useCharacterStore = defineStore("CharacterInfo", {
  state(): CharacterInfo {
    return {
      alter: "",
      name: "",
      skills: [],
      individuation: [],
      character: "",
      role: "delear",
      weapon_types: [],
      carry_type_list: [],
      armor: "",
      armor_mastery: [],
      buff_ratio: 0,
      rune: [],
      platinum: [],
      config: "set",
      clothes_coat: [],
      clothes_pants: [],
      talisman: []
    }
  },
  getters: {
    is_buffer(state) {
      return state.role === "buffer"
    }
  },
  actions: {
    async newCharacter(alter: string) {
      const configStore = useConfigStore()
      const token = await api.getToken(alter)
      configStore.$patch({ token })
      const state = await api.getCharacter()
      this.$patch(state)
      configStore.$patch({ alter, name: "set" })
      await configStore.load()
    }
  }
})
