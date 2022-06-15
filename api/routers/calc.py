import importlib
from fastapi import APIRouter, Body, Depends
from core.baseClass.character import Character
from core.store import store

from .token import AlterState, authorize, createToken
from utils.apiTools import response, Return
from fastapi import APIRouter, Depends
import core.set as set

calcRouter = APIRouter()


@calcRouter.post(path="/calc")
async def calc(setInfo=Body(None), setName=Body(None), state: AlterState = Depends(authorize)):
    alter = "spitfire_female"
    if(state is None or state.alter is None):
        alter = "spitfire_female"
    else:
        alter = state.alter
        # raise Exception("无效token")
        # 配置信息
    set.save(alter, setName, setInfo)
    # 先存档配置信息，再进行计算
    # 职业
    return response(data=None)


@calcRouter.get(path="/calc/result/{id}")
def get_result(id):
    return response(data=store.get("/calc/results/"+id))


@calcRouter.post(path="/calc/single")
async def calc_single(setInfo=Body(None), setName=Body(None), state: AlterState = Depends(authorize)):
    alter = "spitfire_female"
    if(state is None or state.alter is None):
        alter = "spitfire_female"
    else:
        alter = state.alter
        # raise Exception("无效token")
        # 配置信息
    set.save(alter, setName, setInfo)
    # 先存档配置信息，再进行计算
    # 职业

    module_name = "core.characters." + alter
    character: Character = importlib.import_module(module_name).classChange()
    info = character.calc(setName, setInfo['single_set'], True)
    store.set("/calc/results/"+info.get("id"), info)
    return response(data=info)
