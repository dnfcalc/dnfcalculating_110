import { ICharacterSet } from "@/api/info/type"
import { defineStore } from "pinia"
import api from "@/api"
import { ICharacterInfo } from "@/api/character/type"
import { useConfigStore } from "@/store/config"

export interface CharacterInfo extends ICharacterInfo, ICharacterSet {
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
      carryType: [],
      armor: "",
      armor_mastery: [],
      buff_ratio: 0,
      rune: [],
      config: "set",
      skill_set: [],
      equips_set: [],
      forge_set: {}
    }
  },
  actions: {
    async newCharacter(alter: string) {
      const configStore = useConfigStore()
      const token = await api.getToken(alter)
      configStore.$patch({ token })
      const state = await api.getCharacter()
      this.$patch(state)

      configStore.$patch({ alter, name: state.config })
      // await configStore.load()

      // this.skill_set = configStore.data["skill_set"] ?? []
      // this.equips_set = configStore.data["equips_set"] ?? []
      // this.forge_set = configStore.data["forge_set"] ?? {}
      // this.$subscribe(() => {
      //   configStore.set("skill_set", this.skill_set)
      //   configStore.set("equips_set", this.equips_set)
      //   configStore.set("forge_set", this.forge_set)
      //   configStore.save()
      // })
    },

    setForge(part: string, key: string, value: any) {
      let map = this.forge_set[part] ?? new Map<string, any>()
      map.set(key, value)
      this.forge_set[part] = map
    },
    getForge(part: string, key: string) {
      let map = this.forge_set[part] ?? new Map<string, any>()
      return map.get(key)
    }
  }
})
