from fastapi import APIRouter, Body, Depends
from core.store import store

from .token import AlterState, authorize, createToken
from utils.apiTools import response, Return
from fastapi import APIRouter, Depends
from core.calc import calc_set, calc_single_set
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
    return response(data=calc_set(alter, setName))


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
    info = calc_single_set(alter, setName, setInfo['single_set'])
    # 先存档配置信息，再进行计算
    # 职业
    return response(data=info)
