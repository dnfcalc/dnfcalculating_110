import importlib
import json
from math import fabs
import os
from core.baseClass.character import Character
from core.store import store
from core.baseClass.equipment import equ


def save(alter: str, setName: str, setInfo):
    """
    保存存档
    """
    store.set('/{}/setinfo/{}'.format(alter, setName), setInfo)
    # 创建配置文件夹
    path = './Sets/{}/{}'.format(alter, setName)
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
    with open(path + "/store.json", "w", encoding='utf-8') as fp:
        json.dump(setInfo, fp, ensure_ascii=False, indent=2)
    fp.close()
    return get_set_list(alter)

# 获取存档列表


def get_set_list(alter: str):
    """
    获取存档列表
    """
    setList = []
    if not os.path.exists('./Sets/{}'.format(alter)):
        os.makedirs('./Sets/{}'.format(alter), exist_ok=True)
    setList = os.listdir('./Sets/{}'.format(alter))
    if len(setList) == 0:
        setList.append("set")
    return setList


def get(alter: str, setName: str):
    """
    取存档
    """
    set_info = {}
    module_name = "core.characters." + alter
    character: Character = importlib.import_module(module_name).classChange()
    info = character.getinfo()
    skillInfo = info['skills']
    buff = info['buff_ratio']
    skill_set = []
    trigger = equ.get_chose_set(mode=1)
    dress_set = {
        "头发": {
            "id": 0,
            "option": 0
        },
        "帽子": {
            "id": 1,
            "option": 0
        },
        "脸部": {
            "id": 2,
            "option": 0
        },
        "胸部": {
            "id": 3,
            "option": 0
        },
        "上衣": {
            "id": 4,
            "option": 0
        },
        "腰带": {
            "id": 5,
            "option": 0
        },
        "下装": {
            "id": 6,
            "option": 0
        },
        "鞋": {
            "id": 7,
            "option": 0
        },

    }
    for item in skillInfo:
        skill_set.append({
            "name": item["name"],
            "tp": 0,
            "count": 0,
            "pet": 0,
            "direct": False,
            "level": item["current_level"],
            "directNumber": 0,
            "damage": item["type"] == 1
        })
    if not os.path.exists('./Sets/{}/{}/store.json'.format(alter, setName)):
        set_info = {
            "skill_set": skill_set,
            "skill_que": [],
            "forge_set": {},
            "clothes_set": {},
            "single_set": [],
            "equip_list": [],
            "lv110_list": [],
            "weapons_list": [],
            "myths_list": [],
            "wisdom_list": [],
            "trigger_set": trigger,
            "talisman_set": ['']*3,
            "rune_set": ['']*9,
            "buff_ratio": round((buff-1)*100, 1),
            "hotkey_set": ['']*14,
            "carry_type": info["carry_type_list"][0], "dress_set": dress_set}

    else:
        with open('./Sets/{}/{}/store.json'.format(alter, setName), "r", encoding='utf-8') as fp:
            set_info = json.load(fp)
        fp.close()
        # 先简化处理，后续优化
        # todo:比较skill的技能名称
        # todo:比较trigger的id
        if not len(skillInfo) == len(set_info['skill_set']):
            set_info['skill_set'] = skill_set
        if not len(trigger) == len(set_info['trigger_set']):
            set_info['trigger_set'] = trigger

    return set_info
