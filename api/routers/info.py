from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from .token import AlterState, authorize, createToken
from utils.apiTools import reponse, Return
from .response import sundryInfo, characterInfo, equipmentInfo


infoRouter = APIRouter()


class adventureinfo(BaseModel):
    name: str
    alters: List[str]


@infoRouter.get(path='/adventure')
async def get_adventure_info():
    # print(sundryInfo.get_adventure_info())
    return reponse(data=sundryInfo.get_adventure_info())


class notice(BaseModel):
    time: str
    info: str


@infoRouter.get(path='/notice', response_model=Return[notice])
async def get_notice():
    return reponse(data=sundryInfo.get_notice())


@infoRouter.get(path='/blacklist', response_model=Return[dict])
async def get_blacklistlist():
    return reponse(data=sundryInfo.get_blacklistlist())


class characterSkillInfo(BaseModel):
    # 技能信息
    skillInfo: dict
    # 个性化设置，技能选项等
    individuation: dict
    # 护石及符文信息
    # 药剂等相关信息设置


@infoRouter.get(path='/character')
async def get_character_info(state: AlterState = Depends(authorize)):
    return reponse(data=characterInfo.get_character_info(state.alter))


@infoRouter.get(path='/equips')
async def get_equipment_info(state: AlterState = Depends(authorize)):
    return reponse(data=equipmentInfo.get_equipment_info(state.alter))


@infoRouter.get(path='/enchanting')
async def get_enchanting_info():
    return reponse(data=equipmentInfo.get_enchanting_info())


@infoRouter.get(path='/equip/{equID}')
async def get_equipment_detail_info(equID):
    return reponse(data=equipmentInfo.get_equipment_detail_info(equID))


@infoRouter.get(path='/token/{alter}', response_model=Return[str])
async def getToken(alter: str):
    token = createToken(alter)
    return reponse(data=token)


@infoRouter.get(path="/emblem")
async def get_emblem_info():
    return reponse(data=equipmentInfo.get_emblems_info())


@infoRouter.get(path="/jade")
async def get_emblem_info():
    return reponse(data=equipmentInfo.get_jade_info())


@infoRouter.get(path="/sundry")
async def get_sundry_info():
    return reponse(data=equipmentInfo.get_sundry_info())


@infoRouter.get(path="/triggerlist")
async def get_emblem_info():
    return reponse(data=equipmentInfo.get_trigger_list())


@infoRouter.get(path="/entrylist")
async def get_entry_info():
    return reponse(data=equipmentInfo.get_entry_list())


@infoRouter.get(path="/config/{name}")
async def get_config(name, state: AlterState = Depends(authorize)):
    return reponse(data=characterInfo.get_set(state.alter, name))


@infoRouter.get(path="/configs")
async def get_config(state: AlterState = Depends(authorize)):
    return reponse(data=characterInfo.get_set_list(state.alter))
