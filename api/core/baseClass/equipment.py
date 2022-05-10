from asyncio.windows_events import NULL
from decimal import Decimal
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
    名称 = ''
    等级 = 0
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
    前置条件 = []
    # Lv1的基础
    成长基础 = []
    # -1代表需要选择
    属性函数 = []
    # 可选属性列表
    可选属性 = []

    def __init__(self, info={}):
        self.名称 = info.get('name', '')
        self.等级 = info.get('lv', 0)
        self.品质 = '史诗'

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

                #武器属性待补充
                #self.物理攻击力 = 0
                #self.魔法攻击力 = 0
                #self.独立攻击力 = 0

            

    # def 城镇属性(self, 属性):
    #     pass

    # def 进图属性(self, 属性):
    #     pass

    # def 其它属性(self, 属性):
    #     pass

    # def BUFF属性(self, 属性):
    #     pass

    def 可选属性设置(self, 选择属性):
        self.属性函数 = 选择属性

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


class equ_0(equipment):
    名称 = ''
    部位 = ''
    套装 = ''
    等级 = 0
    成长基础 = []
    属性函数 = []
    可选属性 = []


def entry_0(mode=0, text=False, pro={}):
    if text:
        return '属性信息'
    # 计算站街加成
    if mode == 0:
        pass
    # 计算进图加成
    if mode == 1:
        pass


class equipment_list():
    def __init__(self):
        self.info = get_eq_info_data()
        self.load_equ()

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
        return self.equ_list.get(id, equ_0())

    def get_equ_by_name(self, name):
        return self.get_equ_by_id(self.equ_id.get(name, 0))

    def get_id_by_name(self, name):
        return self.equ_id.get(name, 0)

    def get_equ_list(self):
        return self.equ_tuple

    def get_equ_id_list(self):
        return self.equ_id_tuple


equ = equipment_list()
