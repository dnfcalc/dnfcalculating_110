import { ICharacterSet } from "@/api/info/type"
import { defineStore } from "pinia"
import api from "@/api"
import { ICharacterInfo } from "@/api/character/type"
import { useConfigStore } from "@/store/config"
import { tryOnScopeDispose } from "@vueuse/core"
import { RecordToObj } from "@/utils"

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
      carry_type_list: [],
      carry_type: "",
      attack_attribute: 0,
      armor: "",
      armor_mastery: [],
      buff_ratio: 0,
      rune: [],
      platinum: [],
      config: "set",
      skill_set: [],
      equips_set: [],
      forge_set: {},
      other_set: {},
      clothes_set: {},
      clothes: [],
      clothes_bottom: [],
      talisman: [],
      single_set: []
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
    setSkill(skill: string, key: string, value: any) {
      const index = this.skill_set.findIndex(item => item.name == skill)
      if (index < 0) {
        let temp = {
          name: skill,
          level: 0,
          tp: 0,
          direct: false,
          count: 0,
          pet: 0,
          directNumber: 0
        }
        temp[key] = value
        this.skill_set.push(temp)
      } else {
        this.skill_set[index][key] = value
      }
    },
    getSkill(skill: string) {
      return this.skill_set.find(item => item.name == skill)
    },
    setForge(part: string, key: string, value: any) {
      if (!this.forge_set[part]) {
        this.forge_set[part] = new Map<string, any>()
      }
      let map = this.forge_set[part]
      map.set(key, value)
    },
    getForge(part: string, key: string) {
      if (this.forge_set[part]) {
        let map = this.forge_set[part]
        return map.get(key)
      }
    },
    async calc() {
      api.calc({
        setInfo: {
          skill_set: this.skill_set,
          equips_set: this.equips_set,
          forge_set: RecordToObj(this.forge_set),
          other_set: RecordToObj(this.other_set),
          clothes_set: RecordToObj(this.clothes_set)
        },
        setName: "set01"
      })
    }
  }
})
