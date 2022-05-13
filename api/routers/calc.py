from fastapi import APIRouter, Body, Depends
from core.store import store

from .token import AlterState, authorize, createToken
from utils.apiTools import reponse, Return
from fastapi import APIRouter, Depends
from .response import characterInfo

calcRouter = APIRouter()


@calcRouter.post(path="/calc")
async def calc(setInfo=Body(None), setName=Body(None), state: AlterState = Depends(authorize)):
    alter = "spitfire_female"
    if(state is None or state.alter is None):
        alter = "spitfire_female"
        # raise Exception("无效token")
        # 配置信息
    characterInfo.save_set(alter, setName, setInfo)
    info = characterInfo.calc(alter, setName)
    # 先存档配置信息，再进行计算
    # 职业
    return reponse(data=info)
