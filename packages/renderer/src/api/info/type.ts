export interface IAdventureInfo {
  name: string
  children: IAlterInfo[]
}

export interface IAlterInfo {
  name: string
  url?: string
  title: string
  default_value: string
  class: string[]
  options: string[]
}

export interface IEquipmentInfo {
  groupId: number
  id: number
  type: number
  typeName: string
  name: string
  icon: string
  state?: boolean
  features?: number[]
}

export interface IEquipmentList {
  lv110: IEquipmentInfo[]
  myth: IEquipmentInfo[]
  weapon: IEquipmentInfo[]
  wisdom: IEquipmentInfo[]
}

export interface IEnchantingInfo {
  id: string | number
  maxFrame: number | undefined
  position: string
  props: string
  type: string | undefined
  rarity: string | undefined
}

export interface IJadeInfo {
  id: string | number
  min: string | number
  max: string | number
  props: string
  pre: number
  maxFrame: string | number
  unit: string
}

export interface KTV<T> {
  [key: number | string]: T
}

export interface SkillSet {
  //技能名
  name: string

  // 技能等级
  level: number

  // tp
  tp: number

  // 是否手搓
  direct: boolean

  // 方向键数目
  directNumber: number

  // 技能次数
  count: number | string

  // 宠物次数
  pet: number | string
}

interface EquipSet {
  //装备名
  name: string
  // 是否选择
  active: boolean

  data: Map<string, any>
}

export interface ICharacterSet {
  skill_set: SkillSet[]

  forge_set: Record<string, Map<string, any>>

  equips_set: EquipSet[]

  clothes_set: Record<string, Map<string, any>>

  other_set: Record<string, Map<string, any>>

  single_set: IEquipmentInfo[]

  carry_type: string

  attack_attribute: number
}
