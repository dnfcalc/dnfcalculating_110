import json
import os
import sys
from decimal import Decimal
from pyclbr import Function
from typing import Dict, List
from webbrowser import get

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except:
    pass


def get_eq_info_data():
    equ_info = {}
    with open("./dataFiles/equ-data.json", encoding='utf-8') as fp:
        equ_info = json.load(fp)
    return equ_info


def get_entry_info_data():
    entry_info = {}
    with open("./dataFiles/entry-data.json", encoding='utf-8') as fp:
        entry_info = json.load(fp)
    return entry_info


class equipment:
    名称 = ''
    等级 = ''
    品质 = ''
    部位 = ''
    类型 = ''
    力量 = 0
    智力 = 0
    体力 = 0
    精神 = 0
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0
    固有属性 = []
    成长属性 = []
    可选属性 = []
    物理暴击率 = 0
    魔法暴击率 = 0

    def __init__(self, info={}):
        # 读取json获取装备属性
        self.__dict__.update(info)

        # 计算防具转甲基础
        if self.类型 in ['布甲', '皮甲', '轻甲', '重甲', '板甲']:
            设置防具基础(self)

    # def __iter__(self):
    #     yield from [getattr(self, i, 0) for i in ('物理攻击力', '魔法攻击力', '独立攻击力', '三攻', '力量', '智力', '力智', '体力', '精神', '体精', '四维', '物理暴击率', '魔法暴击率', '暴击率', '攻击速度', '施放速度', '移动速度', '三速')]


防具基础 = {
    "105-史诗-布甲-上衣": (100, 161, 100, 161),
    "105-史诗-布甲-头肩": (100, 149, 100, 149),
    "105-史诗-布甲-下装": (100, 161, 100, 161),
    "105-史诗-布甲-鞋":   (100, 136, 100, 136),
    "105-史诗-布甲-腰带": (100, 136, 100, 136),
    "105-史诗-皮甲-上衣": (151, 151, 100, 156),
    "105-史诗-皮甲-头肩": (141, 141, 100, 145),
    "105-史诗-皮甲-下装": (151, 151, 100, 156),
    "105-史诗-皮甲-鞋":   (131, 131, 100, 133),
    "105-史诗-皮甲-腰带": (131, 131, 100, 133),
    "105-史诗-轻甲-上衣": (161, 141, 100, 100),
    "105-史诗-轻甲-头肩": (149, 132, 100, 100),
    "105-史诗-轻甲-下装": (161, 141, 100, 100),
    "105-史诗-轻甲-鞋":   (136, 124, 100, 100),
    "105-史诗-轻甲-腰带": (136, 124, 100, 100),
    "105-史诗-重甲-上衣": (156, 141, 151, 100),
    "105-史诗-重甲-头肩": (145, 132, 141, 100),
    "105-史诗-重甲-下装": (156, 141, 151, 100),
    "105-史诗-重甲-鞋":   (133, 124, 131, 100),
    "105-史诗-重甲-腰带": (133, 124, 131, 100),
    "105-史诗-板甲-腰带": (131, 131, 133, 100),
    "105-史诗-板甲-上衣": (151, 151, 156, 100),
    "105-史诗-板甲-头肩": (141, 141, 145, 100),
    "105-史诗-板甲-下装": (151, 151, 156, 100),
    "105-史诗-板甲-鞋":   (131, 131, 133, 100),
    "105-神话-布甲-上衣": (100, 163, 100, 163),
    "105-神话-皮甲-上衣": (152, 152, 100, 157),
    "105-神话-轻甲-上衣": (163, 142, 100, 100),
    "105-神话-重甲-上衣": (157, 142, 152, 100),
    "105-神话-板甲-上衣": (152, 152, 157, 100),
    "100-智慧产物-板甲-上衣": (44, 44, 49, 0),
    "100-智慧产物-板甲-头肩": (35, 35, 39, 0),
    "100-智慧产物-板甲-下装": (44, 44, 49, 0),
    "100-智慧产物-板甲-鞋": (27, 27, 29, 0),
    "100-智慧产物-板甲-腰带": (27, 27, 29, 0),
    "100-智慧产物-布甲-上衣": (0, 53, 0, 53),
    "100-智慧产物-布甲-头肩": (0, 42, 0, 42),
    "100-智慧产物-布甲-下装": (0, 53, 0, 53),
    "100-智慧产物-布甲-鞋": (0, 32, 0, 32),
    "100-智慧产物-布甲-腰带": (0, 32, 0, 32),
    "100-智慧产物-皮甲-上衣": (44, 44, 0, 49),
    "100-智慧产物-皮甲-头肩": (35, 35, 0, 39),
    "100-智慧产物-皮甲-下装": (44, 44, 0, 49),
    "100-智慧产物-皮甲-鞋": (27, 27, 0, 29),
    "100-智慧产物-皮甲-腰带": (27, 27, 0, 29),
    "100-智慧产物-轻甲-上衣": (53, 35, 0, 0),
    "100-智慧产物-轻甲-头肩": (42, 28, 0, 0),
    "100-智慧产物-轻甲-下装": (53, 35, 0, 0),
    "100-智慧产物-轻甲-鞋": (32, 21, 0, 0),
    "100-智慧产物-轻甲-腰带": (32, 21, 0, 0),
    "100-智慧产物-重甲-上衣": (49, 35, 44, 0),
    "100-智慧产物-重甲-头肩": (39, 28, 35, 0),
    "100-智慧产物-重甲-下装": (49, 35, 44, 0),
    "100-智慧产物-重甲-鞋": (29, 21, 27, 0),
    "100-智慧产物-重甲-腰带": (29, 21, 27, 0),
}


def 设置防具基础(装备):
    装备.力量 = {}
    装备.智力 = {}
    装备.体力 = {}
    装备.精神 = {}

    for i in ['布甲', '皮甲', '轻甲', '重甲', '板甲']:
        b = 防具基础.get('{}-{}-{}-{}'.format(装备.等级, 装备.品质, i, 装备.部位),
                     (0, 0, 0, 0))

        装备.力量.update({i: round((b[0]) * Decimal(1.0))})
        装备.智力.update({i: round((b[1]) * Decimal(1.0))})
        装备.体力.update({i: round((b[2]) * Decimal(1.0))})
        装备.精神.update({i: round((b[3]) * Decimal(1.0))})


# 词条计算优先级，默认为100，特殊需求手动设置优先级
priority = {
    # 无色结算顺序
    1147: 1,
    878: 998,
    1102: 999,
    # MP结算顺序
    1183: 998,
    988: 999,
    # 属强结算
    1034: 999, 1035: 999, 1036: 999, 1037: 999
}


class equipment_list():
    def __init__(self) -> None:
        self.info = get_eq_info_data()
        self.entry_info = get_entry_info_data()
        self.load_equ()

    def load_equ(self) -> None:
        self.equ_list = {}
        self.equ_id = {}
        self.equ_tuple = ()
        self.equ_id_tuple = ()
        for k in self.info.keys():
            temp = equipment(self.info[k])
            i = int(k)
            self.equ_list[i] = temp
            self.equ_id[temp.名称] = i
            self.equ_tuple += (temp, )
            self.equ_id_tuple += (i, )

    def get_json(self, i):
        temp = self.info[str(i)]
        return {
            "id": int(i),
            "name": temp["名称"],
            "icon": temp["icon"],
            "typeName": temp["部位"],
            "stable": temp["固有属性"],
            "alternative": temp["可选属性"] if "可选属性" in temp else [],
            "order":  temp["order"] if "order" in temp else 0,
            "features": temp["特性"] if "特性" in temp else [],
            "type": temp["品质"]
        }

    def get_equ_by_id(self, id) -> equipment:
        return self.equ_list.get(id, equipment())

    def get_equ_by_name(self, name) -> equipment:
        return self.get_equ_by_id(self.equ_id.get(name, 0))

    def get_id_by_name(self, name) -> int:
        return self.equ_id.get(name, 0)

    def get_equ_list(self) -> List[equipment]:
        return self.equ_tuple

    def get_equ_id_list(self) -> List[int]:
        return self.equ_id_tuple

    def get_entry_atk_by_id(self, id) -> int:
        return self.entry_info.get(str(id), {}).get('attack', 0)

    def get_entry_buff_by_id(self, id) -> int:
        return self.entry_info.get(str(id), {}).get('buff', 0)

    def get_damagelist_by_idlist(self, idlist, customize: Dict[str, List[int]] = {}) -> List[tuple]:
        damagelist = []  # (部位, 序号, 基础伤害)
        for id in idlist:
            i = self.get_equ_by_id(id)
            temp = customize.get(str(id), [])
            num = 0
            for k in i.成长属性 + temp:
                damagelist.append((
                    i.部位,
                    num,
                    self.get_entry_atk_by_id(k),
                    self.get_entry_buff_by_id(k)))
                num += 1
                pass
        return damagelist

    def set_func_chose(self, choseinfo) -> None:
        from core.baseClass.entry import variable_set
        for i in choseinfo.keys():
            id = int(i)
            if id >= 20000:  # 额外选项，参数设置
                variable_set[id](choseinfo[i])
            # else:
            #    id 错误

    def get_func_by_id(self, id) -> Function:
        from core.baseClass.entry import entry_func_list
        func_list = entry_func_list.get(id, entry_func_list[0])
        return func_list

    def get_func_list_by_idlist(self, idlist, customize={}) -> List[Function]:
        temp = []
        for id in idlist:
            cus = customize.get(str(id), [])
            i = self.get_equ_by_id(id)
            index = 0
            for k in i.成长属性:
                temp.append((k, i.部位, index))  # 词条id 部位 部位序号(用于获取成长词条等级)
                index += 1
            for k in i.固有属性 + cus:
                temp.append((k, i.部位, -1))  # 词条id 部位 部位序号(非成长词条无序号)
        # 词条优先级排序
        temp.sort(key=(lambda x: priority.get(x[0], 100)))
        funclist = []
        for k, part, index in temp:
            funclist.append((
                self.get_func_by_id(k),
                part,
                index))
        return funclist

    def get_chose_set_info(self) -> List[tuple]:
        from core.baseClass.entry import entry_chose, entry_func_list
        info = []
        # for i in entry_func_list.keys():
        #     temp = entry_func_list[i]
        # if len(temp) > 1:
        #     ctext = []
        #     for k in temp:
        #         ctext.append(k(text=True))
        #     info.append((i, ctext))
        return info + entry_chose

    def get_chose_set(self, mode=0) -> List[Dict]:
        from core.baseClass.entry import multi_select
        if mode == 1:
            setinfo = {}
            for i in self.get_chose_set_info():
                setinfo[i[0]] = [0]
        else:
            setinfo = []
            for i in self.get_chose_set_info():
                setinfo.append({
                    "id": i[0],
                    "selectList": i[1],
                    "multi-select": multi_select.get(i[0], True)
                })
        return setinfo

    # def set_equ_customize(self, customize):
    #     for key in customize.keys():
    #         self.get_equ_by_id(key).成长属性 = customize[key]
    #         print(self.get_equ_by_id(key).成长属性,customize[key])


equ = equipment_list()
