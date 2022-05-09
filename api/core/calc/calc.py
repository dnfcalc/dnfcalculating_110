import importlib


def calc_set(alter: str, setName: str):
    module_name = "core.characters." + alter
    character = importlib.import_module(module_name)
    info = character.classChange().calc(setName)
    return info
