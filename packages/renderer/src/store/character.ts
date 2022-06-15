import { defineStore } from "pinia"
import { ICharacterInfo } from "@/api/character/type"
import { useConfigStore } from "@/store/config"
import api from "@/api"

export interface CharacterInfo extends ICharacterInfo {
  // 基础信息
}

export const useCharacterStore = defineStore("CharacterInfo", {
  state(): CharacterInfo {
    return {
      alter: "",
      name: "",
      skillInfo: [],
      individuation: [],
      character: "",
      characterType: "",
      classChange: "",
      weaponType: [],
      carry_type_list: [],
      armor: "",
      armor_mastery: [],
      buff_ratio: 0,
      rune: [],
      platinum: [],
      config: "set",
      clothes: [],
      clothes_pants: [],
      talisman: []
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
