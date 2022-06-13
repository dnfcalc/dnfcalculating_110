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
  open?: boolean
}

export interface IEquipmentInfo {
  groupId: number
  id: number
  type?: string
  typeName: string
  name: string
  icon: string
  state?: boolean
  features?: number[]
  alternative: number[]
}

export interface IEquipmentList {
  lv110: IEquipmentInfo[]
  myth: IEquipmentInfo[]
  weapon: IEquipmentInfo[]
  wisdom: IEquipmentInfo[]
  title: IEquipmentInfo[]
  pet: IEquipmentInfo[]
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

export interface ITrigger {
  id: number
  selectList: string[]
  "multi-select": boolean
}

export interface TriggerSet {
  id: number
  select: number | number[]
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

  // 是否有伤害
  damage: boolean
}

interface EquipSet {
  //装备名
  name: string
  // 是否选择
  active: boolean

  data: Map<string, any>
}
interface skillQue {
  name: string
  id: number
}

export interface ICharacterSet {
  skill_set: SkillSet[]
  skill_que: skillQue[]

  forge_set: Record<string, Map<string, any>>

  equip_list: number[]

  wisdom_list: number[]

  myths_list: number[]

  weapons_list: number[]

  lv110_list: number[]

  clothes_set: Record<string, Map<string, any>>

  single_set: number[]

  carry_type: string

  attack_attribute: number

  trigger_set: Record<string, number[] | number>

  customize: Record<string, number[]>

  rune_set: number[]

  talisman_set: string[]

  buff_ratio: number

  hotkey_set: string[]
}
