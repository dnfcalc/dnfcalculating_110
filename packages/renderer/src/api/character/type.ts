import { IEquipmentInfo } from "../info/type"

export interface ICharacterInfo {
  name: string
  alter: string
  character: string
  characterType: string
  classChange: string
  weaponType: string[]
  carry_type_list: string[]
  armor?: string
  armor_mastery: string[]
  buff_ratio: number
  skillInfo: ISkillInfo[]
  rune: string[]
  talisman?: string[]
  individuation: IIndividuation[]
  config: string
  clothes: string[]
  clothes_bottom: string[]
  platinum: string[]
}

export interface ISkillInfo {
  name: string
  type: number
  need_level: number
  level_master: number
  level_max: number
  CD: number
  current_LV: number
  data: number
  TP_max: number | undefined
  TP_Lv: number | undefined
}

export interface IIndividuation {
  type: string
  value: string
  items: string[]
  row?: number
  column?: number
  key?: number
}

export interface IResultInfo {
  id: ID
  name: string
  alter: string
  token?: string
  forget_set?: Record<string, Map<string, any>>
  skills: any
  skills_passive: any
  equips: IEquipmentInfo[]
  info: any
  sumdamage: number
  jade?: {
    id: number
    name: string
    damage: number
  }[]
}
