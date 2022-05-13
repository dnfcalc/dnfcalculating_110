from decimal import Decimal
from core.baseClass.entry import entry_func_list
import json
import sys
import os

os.chdir(sys.path[0])


def get_eq_info_data():
    equ_info = {}
    with open("./ResourceFiles/dataFiles/eq-info-data.json", encoding='utf-8') as fp:
        equ_info = json.load(fp)
    return equ_info


class equipment:
    def __init__(self, info={}):
        self.名称 = info.get('name', '')
        self.等级 = info.get('lv', 0)
        self.品质 = '史诗'

        self.部位 = ''
        self.类型 = ''
        self.力量 = 0
        self.智力 = 0
        self.体力 = 0
        self.精神 = 0
        self.物理攻击力 = 0
        self.魔法攻击力 = 0
        self.独立攻击力 = 0
        # 属性id (attack, buffer, entry_func_id)
        self.属性信息 = []
        # 可选属性列表
        self.可选属性 = []

        # 获取部位 类型 信息
        position = info.get('position', '')
        if position != '':
            if '甲' in position:
                self.部位 = position[3:-1]
                self.类型 = position[:2]
                设置防具基础(self)
            else:
                if position in ['手镯', '项链', '戒指']:
                    self.类型 = '首饰'
                elif position in ['耳环', '辅助装备', '魔法石']:
                    self.类型 = '特殊'
                else:
                    self.类型 = '武器'
                self.部位 = position

                for i in info.get('prop', {}).get('base', []):
                    if i['label'] in ['力量', '智力', '体力', '精神']:
                        self.__dict__[i['label']] = i['num']
                # 武器属性待补充
                #self.物理攻击力 = 0
                #self.魔法攻击力 = 0
                #self.独立攻击力 = 0

        # 获取成长词条信息
        growthProps = info.get('prop', {}).get('growthProps', [])
        for i in growthProps:
            self.属性信息.append((
                i.get('attack', 0),
                i.get('buffer', 0),
                i.get('id', 0)))

    # def 城镇属性(self, 属性):
    #     pass

    # def 进图属性(self, 属性):
    #     pass

    # def 其它属性(self, 属性):
    #     pass

    # def BUFF属性(self, 属性):
    #     pass

    def 可选属性设置(self, 选择属性):
        self.属性信息 = 选择属性

    # 城镇属性
    def 城镇属性(self, 属性):
        for item in self.成长属性:
            eval("entry_{}(属性)")


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
    "105-史诗-板甲-鞋":   (131, 131, 133, 100)
}


def 设置防具基础(装备):
    装备.力量 = {}
    装备.智力 = {}
    装备.体力 = {}
    装备.精神 = {}
    # a = 防具额外.get(装备.名称, (0, 0, 0, 0))
    for i in ['布甲', '皮甲', '轻甲', '重甲', '板甲']:
        b = 防具基础.get('{}-{}-{}-{}'.format(装备.等级, 装备.品质, i, 装备.部位),
                     (0, 0, 0, 0))
        # 装备.力量.update({i: round((a[0] + b[0]) * Decimal(1.1))})
        # 装备.智力.update({i: round((a[1] + b[1]) * Decimal(1.1))})
        # 装备.体力.update({i: round((a[2] + b[2]) * Decimal(1.1))})
        # 装备.精神.update({i: round((a[3] + b[3]) * Decimal(1.1))})

        装备.力量.update({i: round((b[0]) * Decimal(1.0))})
        装备.智力.update({i: round((b[1]) * Decimal(1.0))})
        装备.体力.update({i: round((b[2]) * Decimal(1.0))})
        装备.精神.update({i: round((b[3]) * Decimal(1.0))})

# 词条计算优先级，默认为100，特殊需求手动设置优先级
# priority = {
#    1: 150,
# }


class equipment_list():
    def __init__(self):
        self.info = get_eq_info_data()
        self.load_equ()
        self.chose = {}

    def load_equ(self):
        self.equ_list = {}
        self.equ_id = {}
        self.equ_tuple = ()
        self.equ_id_tuple = ()
        i = 0
        for k in self.info:
            temp = equipment(k)
            self.equ_list[i] = temp
            self.equ_id[temp.名称] = i
            self.equ_tuple += (temp, )
            self.equ_id_tuple += (i, )
            i += 1

    def get_equ_by_id(self, id):
        return self.equ_list.get(id, equipment())

    def get_equ_by_name(self, name):
        return self.get_equ_by_id(self.equ_id.get(name, 0))

    def get_id_by_name(self, name):
        return self.equ_id.get(name, 0)

    def get_equ_list(self):
        return self.equ_tuple

    def get_equ_id_list(self):
        return self.equ_id_tuple

    def set_func_chose(self, choseinfo):
        self.chose = choseinfo

    def get_func_by_id(self, id):
        func_list = entry_func_list.get(id, entry_func_list[0])
        return func_list[self.chose.get(id, 0)]

    def get_func_list_by_namelist(self, namelist):
        temp = []
        for name in namelist:
            i = self.get_equ_by_name(name)
            for k in i.属性信息:
                temp.append(k[2])
        # 词条优先级排序
        #temp.sort(key=(lambda x: priority.get(x, 100)))
        funclist = []
        for k in temp:
            funclist.append(self.get_func_by_id(k))
        return funclist

    def get_chose_set(self):
        setinfo = {}
        for i in entry_func_list.keys():
            temp = entry_func_list[i]
            if len(temp) > 1:
                ctext = []
                for k in temp:
                    ctext.append(k(text=True))
                setinfo[i] = ctext
        return setinfo


# 词条id 选择id 默认为0
chose = {
    0: 1,
}


equ = equipment_list()
