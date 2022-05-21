from ast import Lambda
from cProfile import label
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
    cur = equ.info[equID]
    growths = equ.entry_info
    # 基础属性
    equipment_detail_info['position'] = '{}({})'.format(cur['类型'], cur['部位'])
    equipment_detail_info['name'] = cur['名称']
    equipment_detail_info['icon'] = cur['icon']
    # 固有属性
    base = []
    base.append({
        "id": 6,
        "isRate": False,
        "label": "力量",
        "num": cur['力量'],
    })
    base.append({
        "id": 7,
        "isRate": False,
        "label": "智力",
        "num": cur['智力'],
    })
    base.append({
        "id": 8,
        "isRate": False,
        "label": "体力",
        "num": cur['体力'],
    })
    base.append({
        "id": 9,
        "isRate": False,
        "label": "精神",
        "num": cur['精神'],
    })
    bufferProps = []
    # 移动、技攻
    effect = []
    for item in cur['固有属性']:
        # if item == 10001:
        #     effect.append({
        #         "id": 10,
        #         "label": "该装备的成长属性等级之和达到240，增加1%的技能攻击力\n该装备的成长属性等级之和每增加40级，额外增加1%的技能攻击力"
        #     })
        if item == 10006:
            effect.append({
                "id": 16,
                "isRate": True,
                "label": "移动速度",
                "num": 0.04
            })
            effect.append({
                "id": 22,
                "isRate": True,
                "label": "技能攻击力",
                "num": 0.29
            })
        if item in [10002, 10003, 10005, 10007, 10008, 10009, 10010, 10011, 10012]:
            effect.append({
                "id": 22,
                "isRate": True,
                "label": "技能攻击力",
                "num": 0.12
            })
        if item in [10004]:
            effect.append({
                "id": 22,
                "isRate": True,
                "label": "技能攻击力",
                "num": 0.34
            })
        if item in [10013]:
            effect.append({
                "id": 22,
                "isRate": True,
                "label": "技能攻击力",
                "num": 0.5
            })
        if item in [10014]:
            effect.append({
                "id": 22,
                "isRate": True,
                "label": "技能攻击力",
                "num": 0.35
            })
    effect.sort(key=lambda x: x["id"])
    # 成长属性
    growthProps = []
    for index in range(0, len(cur['成长属性'])):
        growth = growths.get(str(cur['成长属性'][index]))
        growthProps.append({
            "id": cur['成长属性'][index],
            "index": index,
            "buffer": growth['buff'],
            "attack": growth['attack'],
            "props": growth['props']})
        pass
    equipment_detail_info["prop"] = {
        "base": base,
        "bufferProps": bufferProps,
        "effect": effect,
        "growthProps": growthProps
    }
    return equipment_detail_info


def get_enchanting_info():
    return get_enchanting_setinfo()


def get_emblems_info():
    return get_emblems_setinfo()


def get_jade_info():
    return get_jade_setinfo()


def get_trigger_list():
    return equ.get_chose_set()
