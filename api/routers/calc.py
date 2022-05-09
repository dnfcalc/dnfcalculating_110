from fastapi import APIRouter, Body, Depends
from .token import authorize, createToken
from utils.apiTools import reponse, Return
from fastapi import APIRouter, Depends
from .response import characterInfo

calcRouter = APIRouter()


@calcRouter.post(path="/calc")
async def calc(setInfo=Body(None), setName=Body(None), alter: str = Depends(authorize)):
    if(alter == None):
        alter = "spitfire_female"
        # raise Exception("无效token")
        # 配置信息
    characterInfo.save_set(alter, setName, setInfo)
    info = characterInfo.calc(alter, setName)
    # 先存档配置信息，再进行计算
    # 职业
    return reponse(data=info)
