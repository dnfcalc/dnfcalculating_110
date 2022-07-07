import requests

from fastapi import APIRouter, Depends
from utils.apiTools import Return, response

skycityRouter = APIRouter()

class RecommentClass(Return):
    totalCount: int = 1


@skycityRouter.get("/recommend")
async def get_recommend(page:int=1,size:int=7,keyword:str="",alter:str=""):
    data = requests.get(
        "https://dnf.skycity.top:8017/api/DCalc/LoadRecommendPage?page={}&size={}&keyword={}&alter={}".format(page,size,keyword,alter),
        timeout=5).json()
    return RecommentClass(code=200, message="", data=data.get("data",{}),totalCount=data.get("totalCount",0))
