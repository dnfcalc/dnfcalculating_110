jade_func_list = {}

# 名望 最小值 最大值 单位 分段 属性
index = ("maxFrame", "min", "max", "unit", "pre", "props")


def jade_26000(char={}, text=False, value=0):
    if text:
        return "(0, 1, 1, '', 0, '无')"


def jade_26001(char={}, text=False, value=0):
    if text:
        return "(56, 1, 1, '', 0, '其它')"


def jade_26002(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[附加伤害增加]增幅')"
    char.附加伤害增加增幅 += value


def jade_26003(char={}, text=False, value=0):
    if text:
        return "(76, -3, 3, '%', 0.1, '[技能伤害增加]增幅')"
    char.技能伤害增加增幅 += value


def jade_26004(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[暴击伤害增加]增幅')"
    char.暴击伤害增加增幅 += value


def jade_26005(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[伤害增加]增幅')"
    char.伤害增加增幅 += value


def jade_26006(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[最终伤害增加]增幅')"
    char.最终伤害增加增幅 += value


def jade_26007(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[物理/魔法/独立攻击力增加]增幅')"
    char.物理魔法攻击力增加增幅 += value


def jade_26008(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[力量智力增加]增幅')"
    char.力量智力增加增幅 += value


def jade_26009(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[装备属性强化增加]增幅')"
    char.所有属性强化增加 += value


def jade_26010(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[属性附加伤害增加]增幅')"
    char.属性附加伤害增加增幅 += value


def jade_26011(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv10~15技能Lv增加')"
    char.技能等级加成('所有', 10, 15, 1)


def jade_26012(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv20~25技能Lv增加')"
    char.技能等级加成('所有', 20, 25, 1)


def jade_26013(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv30~35技能Lv增加')"
    char.技能等级加成('所有', 30, 35, 1)


def jade_26014(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv40~45技能Lv增加')"
    char.技能等级加成('所有', 40, 45, 1)


def jade_26015(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv55~60技能Lv增加')"
    char.技能等级加成('所有', 55, 60, 1)


def jade_26016(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv65~70技能Lv增加')"
    char.技能等级加成('所有', 65, 70, 1)


def jade_26017(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv75~80技能Lv增加')"
    char.技能等级加成('所有', 75, 80, 1)


def jade_26018(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, '一次觉醒技能Lv增加')"
    char.技能等级加成('主动', 50, 50, 1)


def jade_26019(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, '二次觉醒技能Lv增加')"
    char.技能等级加成('主动', 85, 85, 1)


# 辟邪玉效果id范围 26001~26999
for i in range(26001, 26020):
    try:
        if i not in jade_func_list.keys():
            jade_func_list[i] = eval('jade_{}'.format(i))
    except:
        pass


def get_jadefunc_by_id(id):
    return jade_func_list.get(id, jade_26000)


def get_jade_setinfo():
    infolist = []
    for i in jade_func_list.keys():
        data = {}
        data['id'] = i
        info = eval(jade_func_list[i](text=True))
        num = 0
        for k in index:
            data[k] = info[num]
            num += 1
        infolist.append(data)
    return infolist
