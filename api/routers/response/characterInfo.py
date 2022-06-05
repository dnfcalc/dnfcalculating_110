import importlib
from typing import List
import core.set as set
from core.calc.calc import calc_set, calc_single_set


def get_character_info(character: str):
    module_name = "core.characters." + character
    character = importlib.import_module(module_name)
    classChangeInfo = character.classChange().getinfo()
    return classChangeInfo


def save_set(alter: str, setName: str, setInfo):
    return set.save(alter, setName, setInfo)


def get_set(alter: str, setName: str):
    return set.get(alter, setName)


def get_set_list(alter: str):
    return set.get_set_list(alter)


def calc(alter: str, setName: str):
    return calc_set(alter, setName)


def calc_single(alter: str, setName: str, equipList: List[int]):
    return calc_single_set(alter, setName, equipList)
