import importlib

import core.set as set
from core.baseClass.character import Character
from core.store import store
from fastapi import APIRouter, Body, Depends
from utils.apiTools import Return, response

from .token import AlterState, authorize, createToken

import itertools

calcRouter = APIRouter()

@calcRouter.post(path="/calc")
async def calc(setInfo=Body(None), setName=Body(None), state: AlterState = Depends(authorize)):
    alter = None
    if(state is None or state.alter is None):
        raise Exception("无效token")
    else:
        alter = state.alter
        # raise Exception("无效token")
        # 配置信息
    set.save(alter, setName, setInfo)
    # 取每个部位
    sort = setInfo["equip_list"]
    # ["称号", "宠物", "武器", "上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "辅助装备", "魔法石", "耳环"]
    info = {
        "token":state.token,
        "results":[]
    }
    for item in itertools.product(*sort):
        module_name = "core.characters." + alter
        character: Character = importlib.import_module(module_name).classChange()
        temp = character.calc(setName, list(item), False)
        store.set("/calc/results/"+temp.get("id"), temp)
        info["results"].append({
            "id":temp.get("id"),
            "total":temp.get("total_data"),
            "plan":list(item)
        })
    return response(data=info)


@calcRouter.get(path="/calc/result/{id}")
def get_result(id):
    return response(data=store.get("/calc/results/"+id))


@calcRouter.post(path="/calc/single")
async def calc_single(setInfo=Body(None), setName=Body(None), state: AlterState = Depends(authorize)):
    alter = None
    if(state is None or state.alter is None):
        raise Exception("无效token")
    else:
        alter = state.alter.split(".")[-1]
        # raise Exception("无效token")
        # 配置信息
    set.save(alter, setName, setInfo)
    # 先存档配置信息，再进行计算
    # 职业

    module_name = "core.characters." + alter
    character: Character = importlib.import_module(module_name).classChange()
    info = character.calc(setName, setInfo['single_set'], True)
    info['token'] = state.token
    store.set("/calc/results/"+info.get("id"), info)
    return response(data=info)
