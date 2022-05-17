import { defineStore } from "pinia"
import api from "@/api"
import { ICharacterSet } from "@/api/info/type"
import { toObj, toMap } from "@/utils"

interface ConfigState extends ICharacterSet {
  name: string
  alter: string
  token: string
  _configlist: string[] | undefined
}

export const useConfigStore = defineStore("config", {
  state: (): ConfigState => {
    return {
      name: "set",
      alter: "",
      carry_type: "",
      attack_attribute: 0,
      skill_set: [],
      forge_set: {},
      other_set: {},
      clothes_set: {},
      single_set: [],
      equip_list: [],
      wisdom_list: [],
      myths_list: [],
      lv110_list: [],
      weapons_list: [],
      trigger_set: [],
      skill_que: [],
      token: "",
      _configlist: undefined
    }
  },
  getters: {
    config_list(state) {
      if (!state._configlist) {
        api.getConfigList().then(res => (state._configlist = res))
      }
      state._configlist?.push("新建存档")
      return state._configlist
    },
    data(state) {
      return {
        equip_list: [...state.wisdom_list, ...state.myths_list, ...state.weapons_list, ...state.lv110_list],
        carry_type: state.carry_type,
        attack_attribute: state.attack_attribute,
        skill_set: state.skill_set,
        forge_set: state.forge_set,
        other_set: state.other_set,
        clothes_set: state.clothes_set,
        single_set: state.single_set,
        trigger_set: state.trigger_set,
        skill_que: state.skill_que,
        wisdom_list: state.wisdom_list,
        myths_list: state.myths_list,
        weapons_list: state.weapons_list,
        lv110_list: state.lv110_list
      }
    }
  },
  actions: {
    async load() {
      // console.log(this.name)
      await api.getConfig(this.name).then(res => {
        const data = toMap(res) as ICharacterSet
        this.$patch(data)
      })
    },
    async switch(name: string) {
      await this.save()
      this.name = name
      await api.switchConfig(this.name)
    },
    async save() {
      toObj(this.data)
      // for (let key in this.data) {
      //   console.log(typeof this.data[key])
      //   // Object.defineProperty(temp, key, {
      //   //   writable: true,
      //   //   enumerable: true,
      //   //   configurable: true
      //   // })
      // }
      // let temp = {}

      // for (let key in this.data) {
      //   Object.defineProperty(temp, key, {
      //     writable: true,
      //     enumerable: true,
      //     configurable: true
      //   })
      // }
      // await api.saveConfig(this.name, this.data)
    },
    async set(name: string, item: Record<string, any>) {
      this[name] = item
    },
    async calc() {
      console.log(this.data)
      await api.calc({
        setInfo: toObj(this.data),
        setName: this.name
      })
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
          directNumber: 0,
          damage: false
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
    }
  }
})
