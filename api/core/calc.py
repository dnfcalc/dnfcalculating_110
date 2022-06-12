import importlib
from typing import List
from core.store import store

from core.baseClass.character import Character


def calc_set(alter: str, setName: str):
    # 多套计算逻辑
    pass
    # module_name = "core.characters." + alter
    # character = importlib.import_module(module_name)
    # info = character.classChange().calc(setName)
    # return info


def calc_single_set(alter: str, setName: str, equipList: List[int]):
    module_name = "core.characters." + alter
    character: Character = importlib.import_module(module_name).classChange()
    info = character.calc(setName, equipList, True)
    store.set("/calc/results/"+info.get("id"), info)
    return info
