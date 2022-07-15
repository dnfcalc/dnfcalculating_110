from core.baseClass.property import CharacterProperty

consumable_list = {}


def consumable_28000(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        pass
    if mode == 1:
        pass

# 斗神之吼秘药


def consumable_28001(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.斗神宠物加成(int(12*rate)/100)
        pass

# 赛丽亚的特调酷饮


def consumable_28002(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.所有属性强化加成(int(5*rate), 1, 1)
        pass

# [冒险]属性强化药水


def consumable_28003(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.所有属性强化加成(int(10*rate), 1, 1)
        pass

# 魔界战力释放秘药


def consumable_28004(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.基础属性加成(智力=int(150*rate), 力量=int(150*rate))
        pass

# 顶级力量灵药


def consumable_28005(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.基础属性加成(力量=int(175*rate))
        pass

# 顶级智力灵药


def consumable_28006(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.基础属性加成(智力=int(175*rate))
        pass

# 活力秘药


def consumable_28007(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.基础属性加成(智力=int(50*rate), 力量=int(50*rate))
        pass

# 虚祖皇家能量秘药


def consumable_28008(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.基础属性加成(智力=int(100*rate), 力量=int(100*rate))
        char.所有属性强化加成(int(5*rate), mode=1)
        pass

# 黄金羊毛


def consumable_28009(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.基础属性加成(智力=int(60*rate), 力量=int(60*rate))
        pass

# 龙之气息


def consumable_28009(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.基础属性加成(智力=int(30*rate), 力量=int(30*rate))
        pass

# 甜蜜喜糖


def consumable_28010(char: CharacterProperty = {}, mode=0, text=False, rate=1.0):
    if mode == 0:
        # char.基础属性加成(物理攻击力=25 * rate)
        pass
    if mode == 1:
        char.基础属性加成(智力=int(88*rate), 力量=int(88*rate))
        pass


# 药剂id范围 28001~29000
for i in range(28001, 29000):
    try:
        if i not in consumable_list.keys():
            consumable_list[i] = eval('consumable_{}'.format(i))
    except:
        pass


def get_sundriesfunc_by_id(id):
    return consumable_list.get(id, consumable_28000)
