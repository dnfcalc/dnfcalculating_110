from fastapi import APIRouter, Body, Depends
from core.store import store

from .token import AlterState, authorize, createToken
from utils.apiTools import response, Return
from fastapi import APIRouter, Depends
from .response import characterInfo, update

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
    characterInfo.save_set(alter, setName, setInfo)
    info = characterInfo.calc(alter, setName)
    # 先存档配置信息，再进行计算
    # 职业
    return response(data=info)


@calcRouter.get(path="/calc/result/{id}")
def getResult(id):
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
    characterInfo.save_set(alter, setName, setInfo)
    info = characterInfo.calc_single(alter, setName, setInfo['single_set'])
    # 先存档配置信息，再进行计算
    # 职业
    return response(data=info)


@calcRouter.post(path="/checkUpdate")
async def checkupdate(version=Body(None)):
    return response(data=update.check_update(version))


@calcRouter.post(path="/autoUpdate")
def checkupdate():
    update.auto_update()
    return response(data=None)
