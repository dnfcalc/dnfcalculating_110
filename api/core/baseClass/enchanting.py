from core.baseClass.character import Character
enchanting_func_list = {}

# 名望 部位 描述
index = ("maxFame", "position", "props")

# region 正常部位 20000~21000


def enchanting_20000(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '', '无附魔')"
    if mode == 0:
        pass
    if mode == 1:
        pass


def enchanting_20001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '武器', '三攻 +50 力智 +50 全属强 +16 属性攻击')"
    if mode == 0:
        char.所有属性强化加成(16*rate)
        char.三攻固定加成(50*rate)
        char.力智固定加成(50*rate)
    if mode == 1:
        pass


def enchanting_20002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '武器', '三攻 +30 全属强 +15')"
    if mode == 0:
        char.所有属性强化加成(15*rate)
        char.三攻固定加成(30*rate)
    if mode == 1:
        pass


def enchanting_20003(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', '三攻 +40 全属强 +15  技攻 +3%')"
    if mode == 0:
        char.三攻固定加成(40*rate)
        char.所有属性强化加成(15*rate)
        char.技能攻击力加成(0.03*rate)
    if mode == 1:
        pass


def enchanting_20004(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', '三攻 +40 全属强 +15 Lv1~50 主动+1')"
    if mode == 0:
        char.三攻固定加成(40*rate)
        char.所有属性强化加成(15*rate)
        char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20005(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器，上衣，下装', '三攻 +70 力智 +40')"
    if mode == 0:
        x = 70 * rate
        y = 40 * rate
        char.三攻固定加成(x)
        char.力智固定加成(y)
    if mode == 1:
        pass


def enchanting_20007(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带，鞋', '三攻 +36 技攻 +3%')"
    if mode == 0:
        char.三攻固定加成(16*rate)
        char.技能攻击力加成(0.03*rate)
    if mode == 1:
        pass


def enchanting_20008(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带，鞋', '三攻 +36 Lv1~50 主动+1')"
    if mode == 0:
        char.三攻固定加成(16*rate)
        char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20009(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '全属强 +33')"
    if mode == 0:
        char.所有属性强化加成(33*rate)
    if mode == 1:
        pass


def enchanting_20010(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '火、冰 +35')"
    if mode == 0:
        char.火属性强化加成(35*rate)
        char.冰属性强化加成(35*rate)
    if mode == 1:
        pass


def enchanting_20011(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '光、暗 +35')"
    if mode == 0:
        char.光属性强化加成(35*rate)
        char.暗属性强化加成(35*rate)
    if mode == 1:
        pass


def enchanting_20012(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '冰、暗 +35')"
    if mode == 0:
        char.冰属性强化加成(35*rate)
        char.暗属性强化加成(35*rate)
    if mode == 1:
        pass


def enchanting_20013(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '火、光 +35')"
    if mode == 0:
        char.火属性强化加成(35*rate)
        char.光属性强化加成(35*rate)
    if mode == 1:
        pass


def enchanting_20014(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '辅助装备', '全属强 +12 暴击 +3% 最终 +3% 攻击强化 +3%')"
    if mode == 0:
        char.所有属性强化加成(12*rate)
        char.最终伤害加成(0.03*rate)
        char.百分比攻击强化加成(0.03*rate)
        char.暴击率增加(0.03)
    if mode == 1:
        pass


def enchanting_20015(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '魔法石', '全属强 +30')"
    if mode == 0:
        char.所有属性强化加成(30*rate)
    if mode == 1:
        pass


def enchanting_20016(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '魔法石', '全属强 +25')"
    if mode == 0:
        char.所有属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20017(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '耳环', '四维 +150')"
    if mode == 0:
        x = 150 * rate
        char.力智固定加成(x)
        char.体精固定加成(x)
    if mode == 1:
        pass


def enchanting_20018(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '力智 +75 三攻 +20 技攻 +3%')"
    if mode == 0:
        char.三攻固定加成(20*rate)
        char.力智固定加成(75*rate)
        char.技能攻击力加成(0.03*rate)
    if mode == 1:
        pass


def enchanting_20019(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '火强 +16')"
    if mode == 0:
        x = 16 * rate
        char.火属性强化加成(x)
    if mode == 1:
        pass


def enchanting_20020(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '光强 +16')"
    if mode == 0:
        x = 16 * rate
        char.光属性强化加成(x)
    if mode == 1:
        pass


def enchanting_20021(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '暗强 +16')"
    if mode == 0:
        x = 16 * rate
        char.暗属性强化加成(x)
    if mode == 1:
        pass


def enchanting_20022(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '冰强 +16')"
    if mode == 0:
        x = 16 * rate
        char.冰属性强化加成(x)
    if mode == 1:
        pass


def enchanting_20023(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '全属强 +14')"
    if mode == 0:
        x = 14 * rate
        char.所有属性强化加成(x)
    if mode == 1:
        pass


def enchanting_20025(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '力智 +75 三攻 +20  Lv1~50 主动+1')"
    if mode == 0:
        char.三攻固定加成(20*rate)
        char.力智固定加成(75*rate)
        char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


# endregion

# region 光环 21001~21500


def enchanting_21001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1 5%三攻')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.百分比三攻加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass


def enchanting_21002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1 5%黄字')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.伤害增加加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass


def enchanting_21003(char: Character = {}, mode=0, text=False, rate=1.0):
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

# region 武器装扮 21501~22000


def enchanting_21501(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '40级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(40, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21502(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '45级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(45, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21503(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '60级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(60, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21504(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '70级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(70, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21505(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '75级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(75, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21506(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '80级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(80, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21506(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '80级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(80, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass

# endregion

# region 皮肤 22001~22500


def enchanting_22001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '皮肤', '全属强 +5')"
    if mode == 0:
        char.所有属性强化加成(5)
        pass
    if mode == 1:
        pass


def enchanting_22002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '皮肤', '全属强 +6')"
    if mode == 0:
        char.所有属性强化加成(6)
        pass
    if mode == 1:
        pass

# endregion

# region 宠物装备-红 22501~23000


def enchanting_22501(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '三攻 +8% 攻击强化 +8%')"
    if mode == 0:
        char.百分比三攻加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass


def enchanting_22502(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '力智 +8% 攻击强化 +8%')"
    if mode == 0:
        char.百分比力智加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass


def enchanting_22503(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '最终 +8% 攻击强化 +8%')"
    if mode == 0:
        char.最终伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass


def enchanting_22504(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '附加伤害 +8% 攻击强化 +8%')"
    if mode == 0:
        char.附加伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass
# endregion

# region 宠物装备-绿 23001~23500


def enchanting_23001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-绿', '三攻 +40 属强 +20')"
    if mode == 0:
        char.三攻固定加成(40)
        char.所有属性强化加成(20)
        pass
    if mode == 1:
        pass

# endregion

# region 宠物装备-蓝 23501~24000


def enchanting_23501(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-蓝', '三攻 +30')"
    if mode == 0:
        char.三攻固定加成(30)
        pass
    if mode == 1:
        pass

# endregion

# region 快捷装备 24001~24999


def enchanting_24001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '快捷装备', '三攻 +30 附加伤害 +8% 攻击强化 +8%')"
    if mode == 0:
        pass
    if mode == 1:
        char.三攻固定加成(30)
        char.附加伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass


def enchanting_24002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '快捷装备', '四维 +8 附加伤害 +8% 攻击强化 +8%')"
    if mode == 0:
        char.力智固定加成(8)
        char.体精固定加成(8)
        pass
    if mode == 1:
        char.附加伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
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
