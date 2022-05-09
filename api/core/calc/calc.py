import importlib


def calc_set(character: str, setName: str):
    module_name = "core.characters." + character
    character = importlib.import_module(module_name)
    info = character.classChange().calc(setName)
    return info
