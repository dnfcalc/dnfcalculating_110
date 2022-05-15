from decimal import Decimal
from core.baseClass.entry import entry_func_list
import json
import sys
import os

os.chdir(sys.path[0])


def get_eq_info_data():
    equ_info = {}
    with open("./ResourceFiles/dataFiles/equ-data.json", encoding='utf-8') as fp:
        equ_info = json.load(fp)
    return equ_info


def get_entry_info_data():
    entry_info = {}
    with open("./ResourceFiles/dataFiles/entry-data.json", encoding='utf-8') as fp:
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

    def __init__(self, info={}):
        # 读取json获取装备属性
        self.__dict__.update(info)
        
        # 计算防具转甲基础
        if self.类型 in ['布甲', '皮甲', '轻甲', '重甲', '板甲']:
            设置防具基础(self)


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

    for i in ['布甲', '皮甲', '轻甲', '重甲', '板甲']:
        b = 防具基础.get('{}-{}-{}-{}'.format(装备.等级, 装备.品质, i, 装备.部位),
                     (0, 0, 0, 0))

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
        self.entry_info = get_entry_info_data()
        self.load_equ()
        self.chose = {}

    def load_equ(self):
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

    def get_entry_info_by_id(self, id):
        return self.entry_info.get(str(id), [0, 0])

    def get_damagelist_by_idlist(self, idlist):
        damagelist = [] #(部位, 序号, 基础伤害)
        for id in idlist:
            i = self.get_equ_by_id(id)
            num = 0
            for k in i.成长属性:
                damagelist.append((
                    i.部位,
                    num,
                    self.get_entry_info_by_id(k)[0]))
                num += 1
                pass
        return damagelist

    def set_func_chose(self, choseinfo):
        self.chose.update(choseinfo)

    def get_func_by_id(self, id):
        func_list = entry_func_list.get(id, [entry_func_list[0]])
        return func_list[self.chose.get(id, 0)]

    def get_func_list_by_idlist(self, idlist):
        temp = []
        for id in idlist:
            i = self.get_equ_by_id(id)
            for k in i.成长属性:
                temp.append(k)
        # 词条优先级排序
        #temp.sort(key=(lambda x: priority.get(x, 100)))
        funclist = []
        for k in temp:
            funclist.append(self.get_func_by_id(k))
        return funclist

    def get_chose_set(self, mode=0):
        setinfo = []
        for i in entry_func_list.keys():
            temp = entry_func_list[i]
            if len(temp) > 1:
                ctext = []
                for k in temp:
                    ctext.append(k(text=True))
                if mode == 1:
                    setinfo.append({
                        "id": i,
                        "select": 0
                    })
                else:
                    setinfo.append({
                        "id": i,
                        "selectList": ctext
                    })
        return setinfo


equ = equipment_list()
