import json
import os
from core.store import store


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
        json.dump(setInfo, fp, ensure_ascii=False, indent=4)
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
        setList.append("default")
    return setList


def get_set(alter: str, setName: str):
    """
    取存档
    """
    set_info = {}
    with open('./ResourceFiles/{}/{}/store.json'.format(alter, setName) + "/store.json", "w", encoding='utf-8') as fp:
        set_info = json.load(fp)
    return set_info
