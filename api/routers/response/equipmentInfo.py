from ast import Lambda
import importlib
import json
import sys
import os
from typing import Dict, List
from core.baseClass.equipment import equ
from core.baseClass.enchanting import get_enchanting_setinfo
from core.baseClass.emblems import get_emblems_setinfo
from core.baseClass.jade import get_jade_setinfo

import requests


try:
    os.chdir(os.path.dirname(sys.argv[0]))
except:
    pass
equ_details = dict()


class WeaponEquip:
    id: int
    groupId: int
    id: int
    type: int
    typeName: str
    icon: str


class WeaponInfo:
    id: int
    name: str
    eqs: List[WeaponEquip]


def get_equipment_info(alter: str):
    equipment_info = {
        "lv110": [],
        "myth": [],
        "weapon": [],
        "wisdom": []
    }

    module_name = "core.characters." + alter
    character = importlib.import_module(module_name)
    char = character.classChange()
    weapons = char.武器选项
    转职 = char.转职

    for i in equ.info.keys():
        temp = equ.info[i]
        if temp["等级"] == 105 and temp["品质"] == '史诗' and temp["部位"] != "武器":
            equipment_info["lv110"].append(
                {
                    "id": i,
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "order": temp["order"],
                    "typeName": temp["部位"],
                    "customize": temp["可选属性"],
                    "stable": temp["固有属性"]
                }
            )
        if temp["等级"] == 105 and temp["品质"] == '史诗' and temp["类型"] in weapons and (转职 in temp["名称"] or not "胜负之役" in temp["名称"]):
            equipment_info["weapon"].append(
                {
                    "id": i,
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "typeName": temp["部位"],
                    "customize": temp["可选属性"],
                    "stable": temp["固有属性"]
                }
            )
        if temp["品质"] == '神话':
            equipment_info["myth"].append(
                {
                    "id": i,
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "typeName": temp["部位"],
                    "customize": temp["可选属性"],
                    "stable": temp["固有属性"]
                }
            )
        if temp["品质"] == '智慧产物':
            equipment_info["wisdom"].append(
                {
                    "id": i,
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "typeName": temp["部位"],
                    "customize": temp["可选属性"],
                    "stable": temp["固有属性"]
                }
            )

    equipment_info["lv110"].sort(key=lambda x: x["order"])

    return equipment_info


def get_equipment_detail_info(equID):
    equipment_detail_info = {}
    global equ_details
    if len(equ_details) == 0:
        with open("./ResourceFiles/dataFiles/eq-info-data.json", encoding='utf-8') as fp:
            equ_details = dict()
            for item in json.load(fp):
                equ_details[str(item["id"])] = item
    try:
        equipment_detail_info = equ_details[str(equID)]
    except:
        equipment_detail_info = requests.get(
            "https://www.skycity.top:8019/api/equipment/"+equID+"?simple=false",
            timeout=2).json()["data"]
    return equipment_detail_info


def get_enchanting_info():
    return get_enchanting_setinfo()


def get_emblems_info():
    return get_emblems_setinfo()


def get_jade_info():
    return get_jade_setinfo()


def get_trigger_list():
    return equ.get_chose_set()
