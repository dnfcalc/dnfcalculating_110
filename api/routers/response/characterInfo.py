import importlib
from typing import List

import core.set as set
from core.baseClass.character import createCharcter


def has_set(alter: str):
    pass


def get_character_info(alter: str):
    char = createCharcter(alter)
    if char is not None:
        return char.getinfo()
    return None
