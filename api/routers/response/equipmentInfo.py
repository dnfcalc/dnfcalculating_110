import importlib
import json
import os
import sys
from ast import Lambda
from cProfile import label
from typing import Dict, List, Text

import requests
from core.baseClass.character import createCharcter
from core.baseClass.equipment import get_equ, equipment
from core.equipment.emblems import get_emblems_setinfo
from core.equipment.enchanting import get_enchanting_setinfo
from core.equipment.jade import get_jade_setinfo
from core.equipment.sundry import get_sundries_setinfo

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
    part: str
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
        "wisdom": [],
        "pet": [],
        "title": [],
        "consumable":[]
    }

    char = createCharcter(alter)
    if char is None:
        return equipment_info
    weapons = char.武器选项
    转职 = char.转职

    equ = get_equ()

    for i in equ.info.keys():
        temp = equ.info[i]
        if temp['部位'] == "称号":
            equipment_info["title"].append(
                {
                    "id": int(i),
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "part": temp["部位"],
                    "stable": temp["固有属性"],
                    "features": temp["类型"],
                    "alternative": temp["可选属性"],
                    "rarity": temp["品质"],
                    'type': temp['类型']
                }
            )
        if temp['部位'] == "宠物":
            equipment_info["pet"].append(
                {
                    "id": int(i),
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "part": temp["部位"],
                    "stable": temp["固有属性"],
                    "features": temp["类型"],
                    "alternative": temp["可选属性"],
                    "rarity": temp["品质"],
                    'type': temp['类型']
                }
            )
        if temp["等级"] == 105 and temp["品质"] == '史诗' and temp["部位"] != "武器":
            equipment_info["lv110"].append(
                {
                    "id": int(i),
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "order": temp["order"],
                    "part": temp["部位"],
                    "stable": temp["固有属性"],
                    "alternative": temp["可选属性"],
                    "features": temp["特性"],
                    "rarity": temp["品质"],
                    'type': temp['类型']
                }
            )
        if temp["等级"] == 105 and temp["品质"] == '史诗' and temp["类型"] in weapons and (转职 in temp["名称"] or not "胜负之役" in temp["名称"]):
            equipment_info["weapon"].append(
                {
                    "id": int(i),
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "part": temp["部位"],
                    "stable": temp["固有属性"],
                    "alternative": temp["可选属性"],
                    "rarity": temp["品质"],
                    'type': temp['类型']
                }
            )
        if temp["品质"] == '神话' and char.类型 != '辅助':
            equipment_info["myth"].append(
                {
                    "id": int(i),
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "part": temp["部位"],
                    "stable": temp["固有属性"],
                    "alternative": temp["可选属性"],
                    "rarity": temp["品质"],
                    'type': temp['类型']
                }
            )
        if temp["品质"] == '智慧产物' and char.类型 != '辅助':
            equipment_info["wisdom"].append(
                {
                    "id": int(i),
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "part": temp["部位"],
                    "stable": temp["固有属性"],
                    "alternative": temp["可选属性"],
                    "rarity": temp["品质"],
                    'type': temp['类型']
                }
            )

    equipment_info["lv110"].sort(key=lambda x: x["order"])

    consumable_info = {}
    with open("./dataFiles/consumable-data.json", encoding='utf-8') as fp:
        consumable_info = json.load(fp)
    for i in consumable_info.keys():
        temp = consumable_info[i]
        equipment_info["consumable"].append({
                    "id": int(i),
                    "name": temp["名称"],
                    "icon": temp["icon"],
                    "props": temp["props"],
        })
    return equipment_info


def get_equipment_detail_info(equID):
    equipment_detail_info = {}
    equ = get_equ()
    cur = equ.info[equID]
    growths = equ.entry_info
    # 基础属性
    equipment_detail_info['position'] = '{}({})'.format(cur['类型'], cur['部位'])
    equipment_detail_info['name'] = cur['名称']
    equipment_detail_info['icon'] = cur['icon']
    equipment_detail_info['rarity'] = cur['品质']
    # 固有属性
    base = []
    for item in ['力量', '智力', '物理攻击力', '魔法攻击力', '独立攻击力']:
        if item in cur and cur[item] != 0:
            base.append({
                "id": 6,
                "isRate": False,
                "label": item,
                "num": cur[item],
            })
    bufferProps = []
    # 移动、技攻
    effect = []
    for item in cur['固有属性']:
        if item not in [10001, 28, 1237]:
            props = equ.get_func_by_id(item)(text=True)
            for prop in props:
                effect.append({
                    "id": -1,
                    "isRate": False,
                    "label": prop,
                    "num": None
                })
    effect.sort(key=lambda x: x["id"])
    # 成长属性
    growthProps = []
    if cur['部位'] not in ['称号', '宠物']:
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
