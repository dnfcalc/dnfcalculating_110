import json
import requests

from fastapi import APIRouter, Depends
from utils.apiTools import Return, response
from .token import AlterState, authorize, createToken

openRouter = APIRouter()


class RecommentClass(Return):
    totalCount: int = 1


global equ_ids_skycity
equ_ids_skycity = {
    '1464': 0,
    '1465': 1,
    '1466': 2,
    '1467': 3,
    '1468': 4,
    '1469': 5,
    '1470': 6,
    '1471': 7,
    '1472': 8,
    '1473': 9,
    '1474': 10,
    '1475': 11,
    '1476': 12,
    '1477': 13,
    '1478': 14,
    '1479': 15,
    '1480': 16,
    '1481': 17,
    '1482': 18,
    '1483': 19,
    '1484': 20,
    '1485': 21,
    '1486': 22,
    '1487': 23,
    '1488': 24,
    '1489': 25,
    '1490': 26,
    '1491': 27,
    '1492': 28,
    '1493': 29,
    '1494': 30,
    '1495': 31,
    '1496': 32,
    '1497': 33,
    '1498': 34,

}


@openRouter.get("/skycity/recommend")
async def get_recommend(page: int = 1, size: int = 7, keyword: str = "",state: AlterState = Depends(authorize)):
    if(state is None or state.alter is None):
        raise Exception("无效token")
    alter = state.alter
    if alter == 'crusader_male_carry':
        alter = 'crusader_male'
    try:
        data = requests.get(
            "https://www.skycity.top:8017/api/DCalc/LoadRecommendPage?page={}&size={}&keyword={}&alter={}".format(
                page, size, keyword, alter),
            timeout=10).json()
    except:
        raise Exception("空岛水管炸了，请稍后重试")
    info = data.get("data", {})
    if info != {}:
        for item in info:
            equips = item.get("equips", [])
            for equ in equips:
                equ["id"] = equ_ids_skycity.get(str(equ["id"]), equ["id"])
    return RecommentClass(code=200, message="", data=data.get("data", {}), totalCount=data.get("totalCount", 0))


@openRouter.get("/colg/recommend")
async def get_recommend(page: int = 1, size: int = 7, keyword: str = "",state: AlterState = Depends(authorize)):
    data = {}
    if(state is None or state.alter is None):
        raise Exception("无效token")
    alter = state.alter
    try:
        data = requests.get(
                "https://bbs.colg.cn/colg_activity_new-simulator.html/getRecommendList?page={}&size={}&keyword={}&alter={}".format(
                    page, size, keyword, alter),
                timeout=10).json()
        data=data.get("data", {})
    except:
        raise Exception("请稍后重试")
    return RecommentClass(code=200, message="", data=data.get("data", {}), totalCount=data.get("totalCount", 0))