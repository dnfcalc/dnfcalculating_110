export interface IAdventureInfo {
  name: string
  alters: IAlterInfo[]
}

export interface IAlterInfo {
  alter: string
  showName: string
  defaultLabel: string
  class: string[]
  label: string[]
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
  id: number
  maxFrame: number
  position: string
  props: string
}

export interface KTV<T> {
  [key: number | string]: T
}

interface SkillSet {
  //技能名
  name: string

  // 技能等级
  level: number

  // tp
  extra: number
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
}
