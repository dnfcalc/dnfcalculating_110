import json
import sys
import os
from typing import Dict, List
from core.baseClass.equipment import equ
from core.baseClass.enchanting import get_enchanting_setinfo
from core.baseClass.emblems import get_emblems_setinfo

import requests


os.chdir(sys.path[0])
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
        "lv110": {},
        "myth": {},
        "weapon": [],
        "wisdom": {}
    }
    with open("./ResourceFiles/dataFiles/eq-base-data.json", encoding='utf-8') as fp:
        equipment_info["lv110"] = json.load(fp)
    with open("./ResourceFiles/dataFiles/eq-myth-base-data.json", encoding='utf-8') as fp:
        equipment_info["myth"] = json.load(fp)
    with open("./ResourceFiles/dataFiles/arm-base-data.json", encoding='utf-8') as fp:
        array: List[Dict] = json.load(fp)
        for item in array:
            if item.get("name") == alter:
                equipment_info["weapon"] = item.get("eqs")
    with open("./ResourceFiles/dataFiles/eq-wisdom-base-data.json", encoding='utf-8') as fp:
        equipment_info["wisdom"] = json.load(fp)
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
    jade_info = {}
    with open("./ResourceFiles/dataFiles/jade-data.json", encoding='utf-8') as fp:
        jade_info = json.load(fp)
    return jade_info


def get_trigger_list():
    return equ.get_chose_set()
