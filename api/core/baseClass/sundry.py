from core.baseClass.character import Character


sundry_list = {}

# 名望 部位 描述
index = ("maxFrame", "position", "props")


def sundry_27000(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '', '无')"
    if mode == 0:
        pass
    if mode == 1:
        pass

# region 武器装扮 27001~27100


def sundry_27001(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '武器装扮', '40级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(40, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def sundry_27002(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '武器装扮', '45级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(45, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def sundry_27003(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '武器装扮', '60级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(60, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def sundry_27004(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '武器装扮', '70级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(70, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def sundry_27005(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '武器装扮', '75级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(75, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def sundry_27005(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '武器装扮', '80级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(80, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def sundry_27006(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '武器装扮', '80级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(80, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass

# endregion

# region 光环 27101~27300


def sundry_27101(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '光环', 'Lv1~80+1 5%三攻')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.百分比三攻加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass


def sundry_27102(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '光环', 'Lv1~80+1 5%黄字')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.伤害增加加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass


def sundry_27103(char: Character = {}, mode=0, text=False):
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

# region 宠物装备-红 27301~27400

# endregion

# region 宠物装备-绿 27401~27500

# endregion

# region 宠物装备-蓝 27501~27600

# endregion

# region 冒险团 工会属性 训练官-攻击力 训练官-四维 婚房 婚戒 晶体契约 勋章 守护珠 勋章强化 名称装扮卡 快捷装备 皮肤 27401~


def sundry_27401(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '1')"
    if mode == 0:
        char.力智固定加成(0)
        char.体精固定加成(0)
        pass
    if mode == 1:
        pass


def sundry_27402(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '2')"
    if mode == 0:
        char.力智固定加成(10)
        char.体精固定加成(10)
        pass
    if mode == 1:
        pass


def sundry_27403(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '3')"
    if mode == 0:
        char.力智固定加成(30)
        char.体精固定加成(30)
        pass
    if mode == 1:
        pass


def sundry_27404(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '4')"
    if mode == 0:
        char.力智固定加成(50)
        char.体精固定加成(50)
        pass
    if mode == 1:
        pass


def sundry_27405(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '5')"
    if mode == 0:
        char.力智固定加成(70)
        char.体精固定加成(70)
        pass
    if mode == 1:
        pass


def sundry_27406(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '6')"
    if mode == 0:
        char.力智固定加成(90)
        char.体精固定加成(90)
        pass
    if mode == 1:
        pass


def sundry_27407(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '7')"
    if mode == 0:
        char.力智固定加成(110)
        char.体精固定加成(110)
        pass
    if mode == 1:
        pass


def sundry_27408(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '8')"
    if mode == 0:
        char.力智固定加成(125)
        char.体精固定加成(125)
        pass
    if mode == 1:
        pass


def sundry_27409(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '9')"
    if mode == 0:
        char.力智固定加成(140)
        char.体精固定加成(140)
        pass
    if mode == 1:
        pass


def sundry_274010(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '10')"
    if mode == 0:
        char.力智固定加成(155)
        char.体精固定加成(155)
        pass
    if mode == 1:
        pass


def sundry_274011(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '11')"
    if mode == 0:
        char.力智固定加成(170)
        char.体精固定加成(170)
        pass
    if mode == 1:
        pass


def sundry_274012(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '12')"
    if mode == 0:
        char.力智固定加成(170)
        char.体精固定加成(170)
        pass
    if mode == 1:
        pass


def sundry_274013(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '13')"
    if mode == 0:
        char.力智固定加成(170)
        char.体精固定加成(170)
        pass
    if mode == 1:
        pass


def sundry_274014(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '14')"
    if mode == 0:
        char.力智固定加成(170)
        char.体精固定加成(170)
        pass
    if mode == 1:
        pass


def sundry_274015(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '15')"
    if mode == 0:
        char.力智固定加成(170)
        char.体精固定加成(170)
        pass
    if mode == 1:
        pass


def sundry_274016(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '16')"
    if mode == 0:
        char.力智固定加成(200)
        char.体精固定加成(200)
        pass
    if mode == 1:
        pass


def sundry_274017(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '17')"
    if mode == 0:
        char.力智固定加成(200)
        char.体精固定加成(200)
        pass
    if mode == 1:
        pass


def sundry_274018(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '18')"
    if mode == 0:
        char.力智固定加成(215)
        char.体精固定加成(215)
        pass
    if mode == 1:
        pass


def sundry_274019(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '19')"
    if mode == 0:
        char.力智固定加成(215)
        char.体精固定加成(215)
        pass
    if mode == 1:
        pass


def sundry_274020(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '20')"
    if mode == 0:
        char.力智固定加成(230)
        char.体精固定加成(230)
        pass
    if mode == 1:
        pass


def sundry_274021(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '21')"
    if mode == 0:
        char.力智固定加成(230)
        char.体精固定加成(230)
        pass
    if mode == 1:
        pass


def sundry_274022(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '22')"
    if mode == 0:
        char.力智固定加成(230)
        char.体精固定加成(230)
        pass
    if mode == 1:
        pass


def sundry_274023(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '23')"
    if mode == 0:
        char.力智固定加成(230)
        char.体精固定加成(230)
        pass
    if mode == 1:
        pass


def sundry_274024(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '24')"
    if mode == 0:
        char.力智固定加成(230)
        char.体精固定加成(230)
        pass
    if mode == 1:
        pass


def sundry_274025(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '25')"
    if mode == 0:
        char.力智固定加成(245)
        char.体精固定加成(245)
        pass
    if mode == 1:
        pass


def sundry_274026(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '26')"
    if mode == 0:
        char.力智固定加成(245)
        char.体精固定加成(245)
        pass
    if mode == 1:
        pass


def sundry_274027(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '27')"
    if mode == 0:
        char.力智固定加成(245)
        char.体精固定加成(245)
        pass
    if mode == 1:
        pass


def sundry_274028(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '28')"
    if mode == 0:
        char.力智固定加成(245)
        char.体精固定加成(245)
        pass
    if mode == 1:
        pass


def sundry_274029(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '29')"
    if mode == 0:
        char.力智固定加成(245)
        char.体精固定加成(245)
        pass
    if mode == 1:
        pass


def sundry_274030(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '30')"
    if mode == 0:
        char.力智固定加成(260)
        char.体精固定加成(260)
        pass
    if mode == 1:
        pass


def sundry_274031(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '31')"
    if mode == 0:
        char.力智固定加成(260)
        char.体精固定加成(260)
        pass
    if mode == 1:
        pass


def sundry_274032(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '32')"
    if mode == 0:
        char.力智固定加成(260)
        char.体精固定加成(260)
        pass
    if mode == 1:
        pass


def sundry_274033(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '33')"
    if mode == 0:
        char.力智固定加成(260)
        char.体精固定加成(260)
        pass
    if mode == 1:
        pass


def sundry_274034(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '34')"
    if mode == 0:
        char.力智固定加成(260)
        char.体精固定加成(260)
        pass
    if mode == 1:
        pass


def sundry_274035(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '35')"
    if mode == 0:
        char.力智固定加成(275)
        char.体精固定加成(275)
        pass
    if mode == 1:
        pass


def sundry_274036(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '36')"
    if mode == 0:
        char.力智固定加成(275)
        char.体精固定加成(275)
        pass
    if mode == 1:
        pass


def sundry_274037(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '37')"
    if mode == 0:
        char.力智固定加成(275)
        char.体精固定加成(275)
        pass
    if mode == 1:
        pass


def sundry_274038(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '38')"
    if mode == 0:
        char.力智固定加成(275)
        char.体精固定加成(275)
        pass
    if mode == 1:
        pass


def sundry_274039(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '39')"
    if mode == 0:
        char.力智固定加成(275)
        char.体精固定加成(275)
        pass
    if mode == 1:
        pass


def sundry_274040(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '40')"
    if mode == 0:
        char.力智固定加成(290)
        char.体精固定加成(290)
        pass
    if mode == 1:
        pass


# endregion


# 杂项id范围 27001~27999
for i in range(27001, 27999):
    try:
        if i not in sundry_list.keys():
            sundry_list[i] = eval('sundry_{}'.format(i))
    except:
        pass


def get_jadefunc_by_id(id):
    return sundry_list.get(id, sundry_27000)


def get_jade_setinfo():
    infolist = []
    for i in sundry_list.keys():
        data = {}
        data['id'] = i
        info = eval(sundry_list[i](text=True))
        num = 0
        for k in index:
            data[k] = info[num]
            num += 1
        infolist.append(data)
    return infolist
