from typing import List
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from core.baseClass.equipment import equ
from .token import AlterState, authorize, createToken
from utils.apiTools import response, Return
from .response import characterInfo, equipmentInfo
from core.baseClass.enchanting import get_enchanting_setinfo
from core.baseClass.emblems import get_emblems_setinfo
from core.baseClass.jade import get_jade_setinfo
from core.baseClass.sundry import get_sundry_setinfo
import core.set as set
import json

infoRouter = APIRouter()


class adventureinfo(BaseModel):
    name: str
    alters: List[str]


@infoRouter.get(path='/adventure')
async def get_adventure_info():
    adventure_info = {}
    with open("./dataFiles/adventure-info.json", encoding='utf-8') as fp:
        adventure_info = json.load(fp)
    return response(data=adventure_info)


class notice(BaseModel):
    time: str
    info: str


class characterSkillInfo(BaseModel):
    # 技能信息
    skillInfo: dict
    # 个性化设置，技能选项等
    individuation: dict
    # 护石及符文信息
    # 药剂等相关信息设置


@infoRouter.get(path='/character')
async def get_character_info(state: AlterState = Depends(authorize)):
    return response(data=characterInfo.get_character_info(state.alter))


@infoRouter.get(path='/equips')
async def get_equipment(state: AlterState = Depends(authorize)):
    return response(data=equipmentInfo.get_equipment_info(state.alter))


@infoRouter.get(path='/enchanting')
async def get_enchanting():
    return response(data=get_enchanting_setinfo())


@infoRouter.get(path='/equip/{equID}')
async def get_equipment_detail_info(equID):
    return response(data=equipmentInfo.get_equipment_detail_info(equID))


@infoRouter.get(path='/token/{alter}', response_model=Return[str])
async def getToken(alter: str):
    token = createToken(alter)
    return response(data=token)


@infoRouter.get(path="/emblem")
async def get_emblem():
    return response(data=get_emblems_setinfo())


@infoRouter.get(path="/jade")
async def get_jade():
    return response(data=get_jade_setinfo())


@infoRouter.get(path="/sundry")
async def get_sundry():
    return response(data=get_sundry_setinfo())


@infoRouter.get(path="/triggerlist")
async def get_triggerlist():
    return response(data=equ.get_chose_set())


@infoRouter.get(path="/entrylist")
async def get_entry_info():
    return response(data=equ.entry_info)


@infoRouter.get(path="/config/{name}")
async def get_config(name, state: AlterState = Depends(authorize)):
    return response(data=set.get(state.alter, name))


@infoRouter.get(path="/configs")
async def get_config(state: AlterState = Depends(authorize)):
    return response(data=set.get_set_list(state.alter))
