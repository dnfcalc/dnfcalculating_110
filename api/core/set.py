import importlib
import json
from math import fabs
import os
from core.store import store
from core.baseClass.equipment import equ


def save(alter: str, setName: str, setInfo):
    """
    保存存档
    """
    store.set('/{}/setinfo/{}'.format(alter, setName), setInfo)
    # 创建配置文件夹
    path = './ResourceFiles/{}/{}'.format(alter, setName)
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
    setList = os.listdir('./ResourceFiles/{}'.format(alter))
    if len(setList) == 0:
        setList.append("set")
    return setList


def get(alter: str, setName: str):
    """
    取存档
    """
    set_info = {}
    module_name = "core.characters." + alter
    character = importlib.import_module(module_name)
    skillInfo = character.classChange().getinfo()['skillInfo']
    skill_set = []
    trigger = equ.get_chose_set(mode=1)
    for item in skillInfo:
        skill_set.append({
            "name": item["name"],
            "tp": 0,
            "count": 0,
            "pet": 0,
            "direct": False,
            "level": item["current_LV"],
            "directNumber": 0,
            "damage": item["type"] == 1
        })
    if not os.path.exists('./ResourceFiles/{}/{}/store.json'.format(alter, setName)):
        set_info = {
            "skill_set": skill_set,
            "forge_set": {},
            "other_set": {},
            "clothes_set": {},
            "single_set": [],
            "equip_list": [],
            "lv110_list": [], "weapons_list": [], "myths_list": [], "wisdom_list": [],
            "trigger_set": trigger
        }
    else:
        with open('./ResourceFiles/{}/{}/store.json'.format(alter, setName), "r", encoding='utf-8') as fp:
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
