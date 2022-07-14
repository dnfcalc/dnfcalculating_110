import importlib
import traceback
from uuid import uuid1
from routers.response.multi import calc_multi
import core.set as set
from core.baseClass.character import Character
from core.store import store
from fastapi import APIRouter, Body, Depends
from utils.apiTools import response
from .token import AlterState, authorize

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

    return response(data=calc_multi(state, setInfo))


@ calcRouter.get(path="/calc/result/{id}")
def get_result(id):
    return response(data=store.get("/calc/results/"+id))


@ calcRouter.get(path="/calc/rank/{id}")
def get_rank(id):
    return response(data=store.get("/calc/ranks/"+id))


@ calcRouter.post(path="/calc/single")
async def calc_single(setInfo=Body(None), setName=Body(None), state: AlterState = Depends(authorize)):
    alter = None
    if(state is None or state.alter is None):
        raise Exception("无效token")
    else:
        alter = state.alter.split(".")[-1]
        # raise Exception("无效token")
        # 配置信息
    if setName == None:
        module_name = "core.characters." + alter
        character: Character = importlib.import_module(
            module_name).classChange()
        info = character.calc(
            equipList=setInfo['single_set'], info=setInfo, withJade=False)

    else:
        set.save(alter, setName, setInfo)
        # 先存档配置信息，再进行计算
        # 职业
        module_name = "core.characters." + alter
        character: Character = importlib.import_module(
            module_name).classChange()
        info = character.calc(setName, setInfo['single_set'], True)
    info['token'] = state.token
    store.set("/calc/results/"+info.get("id"), info)
    return response(data=info)
