from fastapi import APIRouter, Body
from routers.info import notice
from utils.apiTools import Return
from utils.apiTools import response
from .response import update
import json
import sys
import requests
import os

appRouter = APIRouter()

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except:
    pass


@appRouter.get(path="/heartbeat")
async def heartbeat():
    return response(data=None)


@appRouter.post(path="/checkUpdate")
async def checkupdate(version=Body(None)):
    return response(data=update.check_update(version))


@appRouter.post(path="/autoUpdate")
def checkupdate():
    update.auto_update()
    return response(data=None)


@appRouter.get(path='/notice', response_model=Return[notice])
async def get_notice():
    return response(data=requests.get(
        "https://i_melon.gitee.io/dnfcalculating/notice.json",
        timeout=2).json())


@appRouter.get(path='/blacklist', response_model=Return[dict])
async def get_blacklistlist():
    blacklistlist = {
        "2190155ee92d17e8cc3b0c9892fd5ac7": {
            "reason": "https://tieba.baidu.com/p/7624625617 不好意思 是计算器配不上你"
        },
        "99a2f094ef7daa0d53525b0f2474c0ea": {
            "reason": "https://bbs.colg.cn/thread-8355814-1-1.html 带??节奏"
        },
        "1ba5ea8fa16964666f0c0a85e89c3e96": {
            "reason":
            "https://bbs.colg.cn/thread-8358088-1-1.html 带节奏能请先把龙虎啸等级和其他计算搞清楚"
        },
        "2e3d28298db82f8b23dc9fa6aac14b6d": {
            "reason":
            "https://bbs.colg.cn/thread-8358088-1-1.html 带节奏能请先把龙虎啸等级和其他计算搞清楚"
        },
        "f8b3cf5c269c97a8d6d2d97ecf769a06": {
            "reason": "屠戮直播带节奏"
        },
        "761cf5dbd2e3d07e8eaaf1dc99ebc49b": {
            "reason": "https://bbs.colg.cn/thread-8382566-1-1.html"
        }
    }
    return response(data=blacklistlist)
