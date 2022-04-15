export interface IAdventureInfo {
  职业系: string
  转职名称: string
  一次觉醒: string
  二次觉醒: string
  三次觉醒: string
  显示名称: string
  类名: string
  类名2: string
  序号: string
  作者: string
  时间: string
  备注: string
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

export interface IWeaponInfo {
  id: number
  name: string
  eqs: IEquipmentInfo[]
}

export interface IEquipmentList {
  equipment_Lv110: IEquipmentInfo[]
  equipment_myth: IEquipmentInfo[]
  equipment_weapon: IWeaponInfo[]
  equipment_wisdom: IEquipmentInfo[]
}
