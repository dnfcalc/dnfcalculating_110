import importlib
import core.set as set
from core.calc.calc import calc_set


def get_character_info(character: str):
    module_name = "core.characters." + character
    character = importlib.import_module(module_name)
    classChangeInfo = character.classChange()
    return classChangeInfo


def save_set(alter: str, setName: str, setInfo):
    return set.save(alter, setName, setInfo)


def get_set(alter: str, setName: str):
    return set.get(alter, setName)


def calc(alter: str, setName: str):
    return calc_set(alter, setName)
