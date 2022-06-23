from core.baseClass.character import Character

emblems_func_list = {}

# 名望 部位 颜色 品质 属性
index = ("maxFame", "position", "type", "rarity", "props")


def emblems_25000(char: Character = {}, text=False):
    if text:
        return "(0, '', '其它', '华丽', '无徽章')"


def emblems_25001(char: Character = {}, text=False):
    if text:
        return "(0, '戒指，腰带，皮肤，光环', '红色', '玲珑', '力智+35')"
    char.基础属性加成(力智=35)


def emblems_25002(char: Character = {}, text=False):
    if text:
        return "(0, '戒指，腰带，皮肤，光环', '红色', '灿烂', '力智+25')"
    char.基础属性加成(力智=25)


def emblems_25003(char: Character = {}, text=False):
    if text:
        return "(0, '戒指，腰带，皮肤，光环', '红色', '华丽', '力智+17')"
    char.基础属性加成(力智=17)


def emblems_25004(char: Character = {}, text=False):
    if text:
        return "(0, '上衣，下装，戒指，腰带，皮肤，光环', '红绿', '玲珑', '力智+20 暴击+2.2%')"
    char.基础属性加成(力智=20)
    char.暴击率增加(0.022)


def emblems_25005(char: Character = {}, text=False):
    if text:
        return "(0, '上衣，下装，戒指，腰带，皮肤，光环', '红绿', '玲珑', '力智+15 暴击+1.5%')"
    char.基础属性加成(力智=15)
    char.暴击率增加(0.015)


def emblems_25006(char: Character = {}, text=False):
    if text:
        return "(0, '上衣，下装，戒指，腰带，皮肤，光环', '红绿', '玲珑', '力智+10 暴击+1.1%')"
    char.基础属性加成(力智=10)
    char.暴击率增加(0.011)


def emblems_25007(char: Character = {}, text=False):
    if text:
        return "(0, '头肩，项链', '黄色', '灿烂', '力智+15')"
    char.基础属性加成(力智=15)


def emblems_25008(char: Character = {}, text=False):
    if text:
        return "(0, '头肩，项链', '黄色', '华丽', '力智+10')"
    char.基础属性加成(力智=10)


def emblems_25009(char: Character = {}, text=False):
    if text:
        return "(0, '手镯，鞋，皮肤，光环', '蓝色', '玲珑', '三攻+20')"
    char.基础属性加成(三攻=20)


def emblems_25010(char: Character = {}, text=False):
    if text:
        return "(0, '手镯，鞋，皮肤，光环', '蓝色', '灿烂', '三攻+15')"
    char.基础属性加成(三攻=15)


def emblems_25011(char: Character = {}, text=False):
    if text:
        return "(0, '手镯，鞋，皮肤，光环', '蓝色', '华丽', '三攻+10')"
    char.基础属性加成(三攻=10)


def emblems_25012(char: Character = {}, text=False):
    if text:
        return "(0, '上衣，下装，戒指，腰带，手镯，鞋，皮肤，光环', '其它', '玲珑', '其它效果')"


def emblems_25013(char: Character = {}, text=False):
    if text:
        return "(0, '上衣，下装，戒指，腰带，手镯，鞋，皮肤，光环', '其它', '灿烂', '其它效果')"


def emblems_25014(char: Character = {}, text=False):
    if text:
        return "(0, '上衣，下装，戒指，腰带，手镯，鞋，皮肤，光环', '其它', '华丽', '其它效果')"


# 徽章效果id范围 25001~25999
for i in range(25000, 25015):
    try:
        if i not in emblems_func_list.keys():
            emblems_func_list[i] = eval('emblems_{}'.format(i))
    except:
        pass


def get_embfunc_by_id(id):
    return emblems_func_list.get(id, emblems_25000)


def get_emblems_setinfo():
    infolist = []
    for i in emblems_func_list.keys():
        data = {}
        data['id'] = i
        info = eval(emblems_func_list[i](text=True))
        num = 0
        for k in index:
            data[k] = info[num]
            num += 1
        infolist.append(data)
    return infolist
