from core.baseClass.character import Character
enchanting_func_list = {}

# 名望 部位 描述
index = ("maxFrame", "position", "props")

# region 正常部位 20000~23000


def enchanting_20000(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '', '无附魔')"
    if mode == 0:
        pass
    if mode == 1:
        pass


def enchanting_20001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '火、光属性强化 +15')"
    if mode == 0:
        x = 15 * rate
        char.火属性强化加成(x)
        char.光属性强化加成(x)
    if mode == 1:
        pass


def enchanting_20002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器，上衣，下装', '三攻 +70 力智 +40')"
    if mode == 0:
        x = 70 * rate
        y = 40 * rate
        char.三攻固定加成(x)
        char.力智固定加成(y)
    if mode == 1:
        pass


def enchanting_20003(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '头肩，腰带，鞋', '力智 +100')"
    if mode == 0:
        x = 100 * rate
        char.力智固定加成(x)
    if mode == 1:
        pass


def enchanting_20004(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链，手镯，戒指', '全属强 +28')"
    if mode == 0:
        x = 28 * rate
        char.所有属性强化加成(x)
    if mode == 1:
        pass


def enchanting_20005(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '辅助装备', '三攻 +110')"
    if mode == 0:
        x = 110 * rate
        char.三攻固定加成(x)
    if mode == 1:
        pass


def enchanting_20006(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '魔法石', '全属强 +25')"
    if mode == 0:
        x = 25 * rate
        char.所有属性强化加成(x)
    if mode == 1:
        pass


def enchanting_20007(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '耳环', '四维 +150')"
    if mode == 0:
        x = 150 * rate
        char.力智固定加成(x)
        char.体精固定加成(x)
    if mode == 1:
        pass


def enchanting_20008(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', '三攻+40 全属强 +15 Lv1-50主动 +1')"
    if mode == 0:
        x = 15 * rate
        y = 40 * rate
        char.所有属性强化加成(x)
        char.三攻固定加成(y)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20009(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '火强 +16')"
    if mode == 0:
        x = 16 * rate
        char.火属性强化加成(x)
    if mode == 1:
        pass

# endregion

# region 光环 、 武器装扮 、 皮肤 23001~24999


def enchanting_23001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '皮肤', '全属强 +5')"
    if mode == 0:
        char.所有属性强化加成(5)
        pass
    if mode == 1:
        pass


def enchanting_23002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '皮肤', '全属强 +6')"
    if mode == 0:
        char.所有属性强化加成(6)
        pass
    if mode == 1:
        pass


def enchanting_23003(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '40级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(40, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_23004(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '45级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(45, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_23005(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '60级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(60, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_23006(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '70级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(70, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_23007(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '75级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(75, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_23008(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '80级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(80, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_23009(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '80级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(80, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_23010(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1 5%三攻')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.百分比三攻加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass


def enchanting_23011(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1 5%黄字')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.伤害增加加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass


def enchanting_23012(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1 5%暴伤')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.暴击伤害加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass
# endregion


# 附魔效果id范围 20001~24999
for i in range(20000, 24999):
    try:
        if i not in enchanting_func_list.keys():
            enchanting_func_list[i] = eval('enchanting_{}'.format(i))
    except:
        pass


def get_encfunc_by_id(id):
    return enchanting_func_list.get(id, enchanting_20000)


def get_enchanting_setinfo():
    infolist = []
    for i in enchanting_func_list.keys():
        data = {}
        data['id'] = i
        info = eval(enchanting_func_list[i](text=True))
        num = 0
        for k in index:
            data[k] = info[num]
            num += 1
        infolist.append(data)
    return infolist
