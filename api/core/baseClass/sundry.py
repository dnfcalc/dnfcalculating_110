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


def sundry_2745(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '5')"
    if mode == 0:
        char.力智固定加成(70)
        char.体精固定加成(70)
        pass
    if mode == 1:
        pass


def sundry_2746(char: Character = {}, mode=0, text=False):
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


def sundry_27410(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '10')"
    if mode == 0:
        char.力智固定加成(155)
        char.体精固定加成(155)
        pass
    if mode == 1:
        pass


def sundry_27411(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '11')"
    if mode == 0:
        char.力智固定加成(170)
        char.体精固定加成(170)
        pass
    if mode == 1:
        pass


def sundry_27412(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '12')"
    if mode == 0:
        char.力智固定加成(170)
        char.体精固定加成(170)
        pass
    if mode == 1:
        pass


def sundry_27413(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '13')"
    if mode == 0:
        char.力智固定加成(170)
        char.体精固定加成(170)
        pass
    if mode == 1:
        pass


def sundry_27414(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '14')"
    if mode == 0:
        char.力智固定加成(170)
        char.体精固定加成(170)
        pass
    if mode == 1:
        pass


def sundry_27415(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '15')"
    if mode == 0:
        char.力智固定加成(170)
        char.体精固定加成(170)
        pass
    if mode == 1:
        pass


def sundry_27416(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '16')"
    if mode == 0:
        char.力智固定加成(200)
        char.体精固定加成(200)
        pass
    if mode == 1:
        pass


def sundry_27417(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '17')"
    if mode == 0:
        char.力智固定加成(200)
        char.体精固定加成(200)
        pass
    if mode == 1:
        pass


def sundry_27418(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '18')"
    if mode == 0:
        char.力智固定加成(215)
        char.体精固定加成(215)
        pass
    if mode == 1:
        pass


def sundry_27419(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '19')"
    if mode == 0:
        char.力智固定加成(215)
        char.体精固定加成(215)
        pass
    if mode == 1:
        pass


def sundry_27420(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '20')"
    if mode == 0:
        char.力智固定加成(230)
        char.体精固定加成(230)
        pass
    if mode == 1:
        pass


def sundry_27421(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '21')"
    if mode == 0:
        char.力智固定加成(230)
        char.体精固定加成(230)
        pass
    if mode == 1:
        pass


def sundry_27422(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '22')"
    if mode == 0:
        char.力智固定加成(230)
        char.体精固定加成(230)
        pass
    if mode == 1:
        pass


def sundry_27423(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '23')"
    if mode == 0:
        char.力智固定加成(230)
        char.体精固定加成(230)
        pass
    if mode == 1:
        pass


def sundry_27424(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '24')"
    if mode == 0:
        char.力智固定加成(230)
        char.体精固定加成(230)
        pass
    if mode == 1:
        pass


def sundry_27425(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '25')"
    if mode == 0:
        char.力智固定加成(245)
        char.体精固定加成(245)
        pass
    if mode == 1:
        pass


def sundry_27426(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '26')"
    if mode == 0:
        char.力智固定加成(245)
        char.体精固定加成(245)
        pass
    if mode == 1:
        pass


def sundry_27427(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '27')"
    if mode == 0:
        char.力智固定加成(245)
        char.体精固定加成(245)
        pass
    if mode == 1:
        pass


def sundry_27428(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '28')"
    if mode == 0:
        char.力智固定加成(245)
        char.体精固定加成(245)
        pass
    if mode == 1:
        pass


def sundry_27429(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '29')"
    if mode == 0:
        char.力智固定加成(245)
        char.体精固定加成(245)
        pass
    if mode == 1:
        pass


def sundry_27430(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '30')"
    if mode == 0:
        char.力智固定加成(260)
        char.体精固定加成(260)
        pass
    if mode == 1:
        pass


def sundry_27431(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '31')"
    if mode == 0:
        char.力智固定加成(260)
        char.体精固定加成(260)
        pass
    if mode == 1:
        pass


def sundry_27432(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '32')"
    if mode == 0:
        char.力智固定加成(260)
        char.体精固定加成(260)
        pass
    if mode == 1:
        pass


def sundry_27433(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '33')"
    if mode == 0:
        char.力智固定加成(260)
        char.体精固定加成(260)
        pass
    if mode == 1:
        pass


def sundry_27434(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '34')"
    if mode == 0:
        char.力智固定加成(260)
        char.体精固定加成(260)
        pass
    if mode == 1:
        pass


def sundry_27435(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '35')"
    if mode == 0:
        char.力智固定加成(275)
        char.体精固定加成(275)
        pass
    if mode == 1:
        pass


def sundry_27436(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '36')"
    if mode == 0:
        char.力智固定加成(275)
        char.体精固定加成(275)
        pass
    if mode == 1:
        pass


def sundry_27437(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '37')"
    if mode == 0:
        char.力智固定加成(275)
        char.体精固定加成(275)
        pass
    if mode == 1:
        pass


def sundry_27438(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '38')"
    if mode == 0:
        char.力智固定加成(275)
        char.体精固定加成(275)
        pass
    if mode == 1:
        pass


def sundry_27439(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '39')"
    if mode == 0:
        char.力智固定加成(275)
        char.体精固定加成(275)
        pass
    if mode == 1:
        pass


def sundry_27440(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '冒险团', '40')"
    if mode == 0:
        char.力智固定加成(290)
        char.体精固定加成(290)
        pass
    if mode == 1:
        pass


def sundry_27441(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '工会属性', '四维 +60')"
    if mode == 0:
        char.力智固定加成(60)
        char.体精固定加成(60)
        pass
    if mode == 1:
        pass


def sundry_27442(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '工会属性', '四维 +120')"
    if mode == 0:
        char.力智固定加成(60)
        char.体精固定加成(60)
        pass
    if mode == 1:
        pass


def sundry_27443(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '工会buff-攻击力', '攻击力Lv1：25')"
    if mode == 0:
        pass
    if mode == 1:
        char.三攻固定加成(25)
        pass


def sundry_27444(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '工会buff-攻击力', '攻击力Lv2：30')"
    if mode == 0:
        pass
    if mode == 1:
        char.三攻固定加成(30)
        pass


def sundry_27445(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '工会buff-攻击力', '攻击力Lv3：35')"
    if mode == 0:
        pass
    if mode == 1:
        char.三攻固定加成(35)
        pass


def sundry_27446(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '工会buff-攻击力', '攻击力Lv4：50')"
    if mode == 0:
        pass
    if mode == 1:
        char.三攻固定加成(50)
        pass


def sundry_27447(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '工会buff-四维强化', '四维强化Lv1：40')"
    if mode == 0:
        pass
    if mode == 1:
        char.力智固定加成(40)
        char.体精固定加成(40)
        pass


def sundry_27448(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '工会buff-四维强化', '四维强化Lv2：50')"
    if mode == 0:
        pass
    if mode == 1:
        char.力智固定加成(50)
        char.体精固定加成(50)
        pass


def sundry_27449(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '工会buff-四维强化', '四维强化Lv3：60')"
    if mode == 0:
        pass
    if mode == 1:
        char.力智固定加成(60)
        char.体精固定加成(60)
        pass


def sundry_27450(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '工会buff-四维强化', '四维强化Lv4：80')"
    if mode == 0:
        pass
    if mode == 1:
        char.力智固定加成(80)
        char.体精固定加成(80)
        pass


def sundry_27451(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '婚戒', '体精 +8')"
    if mode == 0:
        char.体精固定加成(8)
        pass
    if mode == 1:
        pass


def sundry_27452(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '婚戒', '体精 +10 力智 +15')"
    if mode == 0:
        char.力智固定加成(15)
        char.体精固定加成(10)
        pass
    if mode == 1:
        pass


def sundry_27453(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '婚房', '全属强 +1')"
    if mode == 0:
        char.所有属性强化加成(1, 0)
        pass
    if mode == 1:
        pass


def sundry_27454(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '婚房', '全属强 +3')"
    if mode == 0:
        char.所有属性强化加成(3, 0)
        pass
    if mode == 1:
        pass


def sundry_27455(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '婚房', '全属强 +5 三攻 +5')"
    if mode == 0:
        char.所有属性强化加成(5, 0)
        char.三攻固定加成(5)
        pass
    if mode == 1:
        pass


def sundry_27456(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '婚房', '全属强 +8 物魔攻 +10 独立 +20')"
    if mode == 0:
        char.所有属性强化加成(8, 0)
        char.三攻固定加成(10, 10, 20)
        pass
    if mode == 1:
        pass

# 调用的时候前面的参数一个都不能少
# sundry_27455({}, 0, False, 0, 2)


def sundry_27457(char: Character = {}, mode=0, text=False, *args):
    if text:
        return "(0, '收集箱', '春节套')"
    if mode == 0:
        # 可变参数
        xy = 0
        sq = 0
        try:
            xy = args[0]
        except:
            pass
        try:
            sq = args[1]
        except:
            pass
        char.三攻固定加成(xy*10)
        char.力智固定加成(sq*10)
        char.体精固定加成(sq*10)
        char.所有属性强化加成(sq*2)
    if mode == 1:
        pass


def sundry_27458(char: Character = {}, mode=0, text=False, *args):
    if text:
        return "(0, '收集箱', '夏日套')"
    if mode == 0:
        pass
    if mode == 1:
        pass


def sundry_27459(char: Character = {}, mode=0, text=False, *args):
    if text:
        return "(0, '收集箱', '五一套')"
    if mode == 0:
        pass
    if mode == 1:
        pass

# 勋章属强 勋章强化


def sundry_27460(char: Character = {}, mode=0, text=False, *args):
    if text:
        return "(0, '勋章', '力智+48 攻击力+30')"
    if mode == 0:
        char.力智固定加成(48)
        char.三攻固定加成(30)
        try:
            char.所有属性强化加成(args[0])
        except:
            pass
        try:
            from core.equipment.基础函数 import 勋章计算
            char.力智固定加成(勋章计算(50, '传说', args[1]))
        except:
            pass
        pass
    if mode == 1:
        pass


def sundry_27461(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '晶体契约', '无色契约 三攻+40')"
    if mode == 0:
        char.三攻固定加成(40)
        pass
    if mode == 1:
        pass


def sundry_27462(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '名称装扮卡', '四维 +3 三速 +1%')"
    if mode == 0:
        pass
    if mode == 1:
        pass


def sundry_27463(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '皮肤', '全属强 +5')"
    if mode == 0:
        char.所有属性强化加成(5)
        pass
    if mode == 1:
        pass


def sundry_27464(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '皮肤', '全属强 +6')"
    if mode == 0:
        char.所有属性强化加成(6)
        pass
    if mode == 1:
        pass


def sundry_27465(char: Character = {}, mode=0, text=False):
    if text:
        return "(0, '快捷装备', '三攻 +30 附加伤害 +8% 攻击强化 +8%')"
    if mode == 0:
        pass
    if mode == 1:
        char.三攻固定加成(30)
        char.附加伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass


def sundry_27466(char: Character = {}, mode=0, text=False):
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


# 杂项id范围 27001~27999
for i in range(27001, 27999):
    try:
        if i not in sundry_list.keys():
            sundry_list[i] = eval('sundry_{}'.format(i))
    except:
        pass


def get_jadefunc_by_id(id):
    return sundry_list.get(id, sundry_27000)


def get_sundry_setinfo():
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
