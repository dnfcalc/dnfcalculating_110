import hyRequest from "../index"
import { IAdventureInfo, IEquipmentInfo } from "./type"
import { IDataType } from "../types"

enum InfoAPI {
  AdventureInfo = "/info/adventureinfo",
  BlackList = "/info/blacklist",
  EquipmentInfo = "/info/equipmentInfo",
  EquipmentDetailInfo = "/info/equipmentDetailInfo/"
}

export function GetAdventureInfo() {
  return hyRequest.get<IDataType<IAdventureInfo[][]>>({
    url: InfoAPI.AdventureInfo
  })
}

export function GetEquipmentInfo() {
  return hyRequest.get<IDataType<IEquipmentInfo[]>>({
    url: InfoAPI.EquipmentInfo
  })
}

export function GetEquipmentDetailInfo(euqID: Number) {
  return hyRequest.get<IDataType<any>>({
    url: InfoAPI.EquipmentDetailInfo + euqID
  })
}
