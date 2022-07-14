import importlib
import traceback
from unittest import result
from uuid import uuid1
from core.util.minheap import MinHeap

import core.set as set
from core.baseClass.character import Character
from core.store import store
from fastapi import APIRouter, Body, Depends
from utils.apiTools import Return, response

from .token import AlterState, authorize, createToken
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count, freeze_support
import itertools

calcRouter = APIRouter()


def calc_single_rank(alter, equipList, setInfo):
    # print(set, alter, setName)
    module_name = "core.characters." + alter
    character: Character = importlib.import_module(
        module_name).classChange()
    try:
        temp = character.calc(equipList=list(equipList), info=setInfo)
    except Exception as ex:
        print(traceback.format_exc())
    return (temp.get("total_data"), equipList)


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
    global info
    info = {
        "token": state.token,
        "results": []
    }
    combos = list(itertools.product(*sort))
    number = len(combos)
    batch_size = 20000
    minheap = MinHeap(2 << 64)
    result = []
    freeze_support()
    with ProcessPoolExecutor(max_workers=max(cpu_count()-2, 1)) as executor:
        # 1W个处理一次
        batch_numbers = int(number/batch_size)+1
        for batch in range(0, batch_numbers):
            batch_combo = combos[batch_size*(batch):batch_size*(batch+1)]
            batch_heap = MinHeap(batch_size)
            print("批次:"+str(batch+1), batch_heap)
            result = None
            result = executor.map(calc_single_rank, [alter]*len(batch_combo),
                                  batch_combo, [setInfo]*len(batch_combo))
            for item in result:
                batch_heap.add(item)
            minheap.merge(batch_heap)
        # result = None
        # result = executor.map(calc_single_rank, [alter]*number,
        #                       combos, [setInfo]*number)
    result = {
        "rank": minheap.getTop()[:50],
        "token": state.token,
        "id": uuid1().hex
    }
    store.set("/calc/ranks/"+result.get("id"), result)
    result["setInfo"] = setInfo
    return response(data=result)


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
    print(setName)
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
