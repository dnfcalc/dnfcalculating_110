entry_func_list = {}  # id : [enteyfunc] 词条函数(数组)列表
entry_id_bind = {}  # id: (id, chose) 关联选项，参考37敌人类型选择
entry_chose = []  # (20000 + id, [chose1, 2, 3...]) 额外选项设置，参考20074消灭敌人词条
multi_select = {}  # id : True/False 设置选项是否支持多选
variable_set = {}  # id : setfunc  参数返回设置函数
priority = {}  # id : num  词条计算优先级，默认为100

# region 无效果词条


def entry_0(char={}, mode=0, text=False, part=''):
    if text:
        return "空词条"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1(char={}, mode=0, text=False, part=''):
    if text:
        return "HP MAX +600"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_2(char={}, mode=0, text=False, part=''):
    if text:
        return "HP MAX +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_3(char={}, mode=0, text=False, part=''):
    if text:
        return "MP MAX +945"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_4(char={}, mode=0, text=False, part=''):
    if text:
        return "MP MAX +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_5(char={}, mode=0, text=False, part=''):
    if text:
        return "物理防御力 +7000, 魔法防御力 +7000"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_6(char={}, mode=0, text=False, part=''):
    if text:
        return "物理防御力 +5%, 魔法防御力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_12(char={}, mode=0, text=False, part=''):
    if text:
        return "每分钟恢复角色460.2的HP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_13(char={}, mode=0, text=False, part=''):
    if text:
        return "每分钟恢复角色348的MP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_14(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃力 +20, 跳跃时移动速度 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_24(char={}, mode=0, text=False, part=''):
    if text:
        return "物品栏负重上限 +5kg"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_35(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +10%, 自身触发的束缚状态持续时间 +1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_59(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入灼烧状态(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_60(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入中毒状态(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_61(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入出血状态(冷却时间8秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_62(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入感电状态(冷却时间15秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_63(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入冰冻状态(冷却时间25秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_64(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入减速状态(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_65(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入眩晕状态(冷却时间20秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_66(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入诅咒状态(冷却时间25秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_67(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入失明状态(冷却时间25秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_68(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入石化状态(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_69(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入睡眠状态(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_70(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入混乱状态(冷却时间25秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_71(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率使敌人进入束缚状态(冷却时间25秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_72(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有20%的几率进入霸体状态，持续5秒(冷却时间8秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_73(char={}, mode=0, text=False, part=''):
    if text:
        return "施放时，有20%的几率进入霸体状态，持续5秒(冷却时间8秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_76(char={}, mode=0, text=False, part=''):
    if text:
        return "出血抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_77(char={}, mode=0, text=False, part=''):
    if text:
        return "中毒抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_78(char={}, mode=0, text=False, part=''):
    if text:
        return "灼烧抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_79(char={}, mode=0, text=False, part=''):
    if text:
        return "感电抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_80(char={}, mode=0, text=False, part=''):
    if text:
        return "冰冻抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_81(char={}, mode=0, text=False, part=''):
    if text:
        return "减速抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_82(char={}, mode=0, text=False, part=''):
    if text:
        return "眩晕抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_83(char={}, mode=0, text=False, part=''):
    if text:
        return "诅咒抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_84(char={}, mode=0, text=False, part=''):
    if text:
        return "失明抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_85(char={}, mode=0, text=False, part=''):
    if text:
        return "石化抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_86(char={}, mode=0, text=False, part=''):
    if text:
        return "睡眠抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_87(char={}, mode=0, text=False, part=''):
    if text:
        return "混乱抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_88(char={}, mode=0, text=False, part=''):
    if text:
        return "束缚抗性 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_89(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的出血状态持续时间 -10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_90(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的中毒状态持续时间 -10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_91(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的灼烧状态持续时间 -10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_92(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的感电状态持续时间 -10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_93(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的冰冻状态持续时间 +2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_94(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的减速状态持续时间 +2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_95(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的眩晕状态持续时间 +2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_96(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的诅咒状态持续时间 +2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_97(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的失明状态持续时间 +2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_98(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的石化状态持续时间 +2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_99(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的睡眠状态持续时间 +2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_100(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的混乱状态持续时间 +2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_101(char={}, mode=0, text=False, part=''):
    if text:
        return "自身触发的束缚状态持续时间 +2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_111(char={}, mode=0, text=False, part=''):
    if text:
        return "前冲时，有20%的几率进入霸体状态，效果持续3秒(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_112(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃时，有50%的几率进入霸体状态，效果持续3秒(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_115(char={}, mode=0, text=False, part=''):
    if text:
        return "受到超过最大HP的20%以上的伤害时，生成相当于最大HP30%的保护罩，持续3秒(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_128(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv15技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_129(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv20技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_130(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv25技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_131(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv30技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_132(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv35技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_133(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv40技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_134(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv45技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_135(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv60技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_136(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv70技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_137(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv75技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_138(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv80技能范围 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_158(char={}, mode=0, text=False, part=''):
    if text:
        return "受到正面攻击时，所受伤害 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_159(char={}, mode=0, text=False, part=''):
    if text:
        return "受到背面攻击时，所受伤害 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_160(char={}, mode=0, text=False, part=''):
    if text:
        return "受到破招攻击时，所受伤害 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_161(char={}, mode=0, text=False, part=''):
    if text:
        return "受到非破招攻击时，所受伤害 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_162(char={}, mode=0, text=False, part=''):
    if text:
        return "每次攻击，恢复2200的HP(冷却时间1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_163(char={}, mode=0, text=False, part=''):
    if text:
        return "每次攻击，恢复3500的MP(冷却时间1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_164(char={}, mode=0, text=False, part=''):
    if text:
        return "被攻击时，有50%的几率，进入霸体状态(冷却时间8秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_190(char={}, mode=0, text=False, part=''):
    if text:
        return "自身与敌人的所有异常状态持续时间 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion

# region 常规词条


def entry_7(char={}, mode=0, text=False, part=''):
    if text:
        return "物理暴击率 +5%, 魔法暴击率 +5%"
    if mode == 0:
        char.物理暴击率增加(0.05)
        char.魔法暴击率增加(0.05)
    if mode == 1:
        pass


def entry_8(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击速度 +8%, 施放速度 +12%"
    if mode == 0:
        char.攻击速度增加(0.08)
        char.施放速度增加(0.12)
    if mode == 1:
        pass


def entry_9(char={}, mode=0, text=False, part=''):
    if text:
        return "移动速度 +8%"
    if mode == 0:
        char.移动速度增加(0.08)
    if mode == 1:
        pass


def entry_10(char={}, mode=0, text=False, part=''):
    if text:
        return "命中率 +10%"
    if mode == 0:
        char.命中率增加(0.1)
    if mode == 1:
        pass


def entry_11(char={}, mode=0, text=False, part=''):
    if text:
        return "回避率 +8%"
    if mode == 0:
        char.回避率增加(0.08)
    if mode == 1:
        pass


def entry_15(char={}, mode=0, text=False, part=''):
    if text:
        return "冰属性强化 +15"
    if mode == 0:
        char.冰属性强化加成(15)
    if mode == 1:
        pass


def entry_16(char={}, mode=0, text=False, part=''):
    if text:
        return "光属性强化 +15"
    if mode == 0:
        char.光属性强化加成(15)
    if mode == 1:
        pass


def entry_17(char={}, mode=0, text=False, part=''):
    if text:
        return "火属性强化 +15"
    if mode == 0:
        char.火属性强化加成(15)
    if mode == 1:
        pass


def entry_18(char={}, mode=0, text=False, part=''):
    if text:
        return "暗属性强化 +15"
    if mode == 0:
        char.暗属性强化加成(15)
    if mode == 1:
        pass


def entry_19(char={}, mode=0, text=False, part=''):
    if text:
        return "所有属性强化 +10"
    if mode == 0:
        char.所有属性强化加成(10)
    if mode == 1:
        pass


def entry_20(char={}, mode=0, text=False, part=''):
    if text:
        return "火属性抗性 +10"
    if mode == 0:
        char.火属性抗性加成(10)
    if mode == 1:
        pass


def entry_21(char={}, mode=0, text=False, part=''):
    if text:
        return "冰属性抗性 +10"
    if mode == 0:
        char.冰属性抗性加成(10)
    if mode == 1:
        pass


def entry_22(char={}, mode=0, text=False, part=''):
    if text:
        return "光属性抗性 +10"
    if mode == 0:
        char.光属性抗性加成(10)
    if mode == 1:
        pass


def entry_23(char={}, mode=0, text=False, part=''):
    if text:
        return "暗属性抗性 +10"
    if mode == 0:
        char.暗属性抗性加成(10)
    if mode == 1:
        pass


def entry_25(char={}, mode=0, text=False, part=''):
    if text:
        return "所有属性抗性 +8"
    if mode == 0:
        char.所有属性抗性加成(8)
    if mode == 1:
        pass


def entry_26(char={}, mode=0, text=False, part=''):
    if text:
        return "所有属性强化 +15, 所有属性抗性 -10"
    if mode == 0:
        char.所有属性强化(15)
        char.所有属性抗性加成(-10)
    if mode == 1:
        pass


def entry_27(char={}, mode=0, text=False, part=''):
    if text:
        return "物理暴击率 +7%, 魔法暴击率 +7%, 所有异常状态抗性 -10%"
    if mode == 0:
        char.物理暴击率增加(0.07)
        char.魔法暴击率增加(0.07)
    if mode == 1:
        pass


def entry_28(char={}, mode=0, text=False, part=''):
    if text:
        return "该装备的成长属性等级之和每达到40，增加3%的技能攻击力,  - 穿戴神话装备时不适用,  - 仅适用上衣、手镯、耳环中最高的1个"
    if mode == 0:
        if not char.已穿戴神话():  # 判断是否穿戴神话装备
            x = sum(char.词条等级.get(part, [0]))
            temp = []
            for i in ['上衣', '手镯', '耳环']:  # 计算3个部位最高值
                temp.append(sum(char.词条等级.get(i, [0])))
            temp.sort(reverse=True)
            if x == temp[0]:
                if x > temp[1] or part == '上衣':  # 若存在两个最高则只在上衣生效
                    char.技能攻击力加成(0.03 * int(x / 40))
    if mode == 1:
        pass


def entry_29(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv30 buff技能Lv+1, Lv50 主动技能Lv+1"
    if mode == 0:
        char.buff技能等级加成(30, 1)
        char.技能等级加成('主动', 50, 50, 1)
    if mode == 1:
        pass


def entry_30(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv30 buff技能Lv+3, Lv50 主动技能Lv+4"
    if mode == 0:
        char.buff技能等级加成(30, 3)
        char.技能等级加成('主动', 50, 50, 4)
    if mode == 1:
        pass


def entry_31(char={}, mode=0, text=False, part=''):
    if text:
        return "该装备的附魔效果 +70%"
    if mode == 0:
        pass
    if mode == 1:
        char.部位附魔[part](char, rate=0.7)


def entry_32(char={}, mode=0, text=False, part=''):
    if text:
        return "该装备的附魔效果 +70%"
    if mode == 0:
        pass
    if mode == 1:
        char.部位附魔[part](char, rate=0.7)


def entry_33(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，该装备的附魔效果 +30%"
    if mode == 0:
        pass
    if mode == 1:
        char.部位附魔[part](char, rate=0.3)


def entry_34(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，该装备的附魔效果 +30%"
    if mode == 0:
        pass
    if mode == 1:
        char.部位附魔[part](char, rate=0.3)


def entry_36(char={}, mode=0, text=False, part=''):
    if text:
        return "控制敌人时，所有属性强化 +20，效果持续20秒"
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(20)


def entry_102(char={}, mode=0, text=False, part=''):
    if text:
        return "中毒伤害 +10%"
    if mode == 0:
        char.异常增伤('中毒', 0.1)
    if mode == 1:
        pass


def entry_103(char={}, mode=0, text=False, part=''):
    if text:
        return "灼烧伤害 +10%"
    if mode == 0:
        char.异常增伤('灼烧', 0.1)
    if mode == 1:
        pass


def entry_104(char={}, mode=0, text=False, part=''):
    if text:
        return "感电伤害 +10%"
    if mode == 0:
        char.异常增伤('感电', 0.1)
    if mode == 1:
        pass


def entry_105(char={}, mode=0, text=False, part=''):
    if text:
        return "出血伤害 +10%"
    if mode == 0:
        char.异常增伤('出血', 0.1)
    if mode == 1:
        pass


def entry_114(char={}, mode=0, text=False, part=''):
    if text:
        return "受身蹲伏结束后60秒内，攻击速度+40%，移动速度+40%，施放速度+60%(冷却时间10秒，最多叠加1次), 每3次攻击，回避率 +3%(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度加成(0.4)
        char.移动速度加成(0.4)
        char.释放速度加成(0.6)


def entry_123(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，消耗1个红色小晶块，火属性强化 +25，效果持续30秒(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(25)


def entry_124(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，消耗1个蓝色小晶块，冰属性强化 +25，效果持续30秒(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(25)


def entry_125(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，消耗1个白色小晶块，光属性强化 +25，效果持续30秒(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(25)


def entry_126(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，消耗1个黑色小晶块，暗属性强化 +25，效果持续30秒(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(25)


def entry_127(char={}, mode=0, text=False, part=''):
    if text:
        return "使用消耗品时，攻击速度、移动速度、施放速度 +20%，效果持续30秒(冷却时间10秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度加成(0.2)
        char.移动速度加成(0.2)
        char.释放速度加成(0.2)


def entry_152(char={}, mode=0, text=False, part=''):
    if text:
        return "技能MP消耗量 -7%"
    if mode == 0:
        pass
    if mode == 1:
        char.MP消耗量加成(-0.07)


def entry_154(char={}, mode=0, text=False, part=''):
    if text:
        return "受到火属性攻击时，火属性抗性 +20，效果持续10秒(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        char.火属性抗性加成(20)


def entry_155(char={}, mode=0, text=False, part=''):
    if text:
        return "受到冰属性攻击时，冰属性抗性 +20，效果持续10秒(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性抗性加成(20)


def entry_156(char={}, mode=0, text=False, part=''):
    if text:
        return "受到光属性攻击时，光属性抗性 +20，效果持续10秒(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        char.光属性抗性加成(20)


def entry_157(char={}, mode=0, text=False, part=''):
    if text:
        return "受到暗属性攻击时，暗属性抗性 +20，效果持续10秒(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性抗性加成(20)


def entry_167(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击速度 +30%, 物理防御力 -20000, 魔法防御力 -20000"
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.3)


def entry_168(char={}, mode=0, text=False, part=''):
    if text:
        return "施放速度 +45%, 物理防御力 -20000, 魔法防御力 -20000"
    if mode == 0:
        pass
    if mode == 1:
        char.释放速度增加(0.45)


def entry_170(char={}, mode=0, text=False, part=''):
    if text:
        return "被击伤害 -25%, 移动速度 -20%"
    if mode == 0:
        char.移动速度增加(-0.2)
    if mode == 1:
        pass


def entry_171(char={}, mode=0, text=False, part=''):
    if text:
        return "HP MAX +1200, 攻击速度 -15%, 施放速度 -22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_172(char={}, mode=0, text=False, part=''):
    if text:
        return "HP MAX +1890, 移动速度 -20%"
    if mode == 0:
        char.移动速度增加(-0.2)
    if mode == 1:
        pass


def entry_173(char={}, mode=0, text=False, part=''):
    if text:
        return "火属性强化 +30, 所有异常状态抗性 -10%"
    if mode == 0:
        char.火属性强化加成(30)
    if mode == 1:
        pass


def entry_174(char={}, mode=0, text=False, part=''):
    if text:
        return "冰属性强化 +30, 所有异常状态抗性 -10%"
    if mode == 0:
        char.冰属性强化加成(30)
    if mode == 1:
        pass


def entry_175(char={}, mode=0, text=False, part=''):
    if text:
        return "光属性强化 +30, 所有异常状态抗性 -10%"
    if mode == 0:
        char.光属性强化加成(30)
    if mode == 1:
        pass


def entry_176(char={}, mode=0, text=False, part=''):
    if text:
        return "暗属性强化 +30, 所有异常状态抗性 -10%"
    if mode == 0:
        char.暗属性强化加成(30)
    if mode == 1:
        pass


def entry_177(char={}, mode=0, text=False, part=''):
    if text:
        return "角色伤害的10%转化为中毒伤害"
    if mode == 0:
        char.伤害类型转化('直接', '中毒', 0.1)
    if mode == 1:
        pass


def entry_178(char={}, mode=0, text=False, part=''):
    if text:
        return "角色伤害的10%转化为灼烧伤害"
    if mode == 0:
        char.伤害类型转化('直接', '灼烧', 0.1)
    if mode == 1:
        pass


def entry_179(char={}, mode=0, text=False, part=''):
    if text:
        return "角色伤害的10%转化为感电伤害"
    if mode == 0:
        char.伤害类型转化('直接', '感电', 0.1)
    if mode == 1:
        pass


def entry_180(char={}, mode=0, text=False, part=''):
    if text:
        return "角色伤害的10%转化为出血伤害"
    if mode == 0:
        char.伤害类型转化('直接', '出血', 0.1)
    if mode == 1:
        pass


def entry_181(char={}, mode=0, text=False, part=''):
    if text:
        return "剩余HP超过50%以上时，伤害增加 N"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_182(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有属性抗性之和超过250以上时，中毒伤害 +15%"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('中毒', 0.15)


priority[192] = 200


def entry_192(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有属性强化之和超过850以上时，移动速度 +40%"
    if mode == 0:
        pass
    if mode == 1:
        # 判断暂未实现
        char.移动速度增加(0.4)


def entry_197(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有属性强化之和超过850以上时，所有异常状态抗性 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_198(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有异常状态抗性之和超过50%以上时，攻击速度 +20%，施放速度 +30%"
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.2)
        char.释放速度增加(0.3)
        pass

# endregion

# region 敌人类型词条


def entry_enemy_type(char={}, mode=0, text=False, part=''):
    if text:
        return "选择敌人类型"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_37(char={}, mode=0, text=False, part=''):
    if text:
        return "机械(7%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.07)
    if mode == 1:
        pass


def entry_38(char={}, mode=0, text=False, part=''):
    if text:
        return "恶魔(7%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.07)
    if mode == 1:
        pass


def entry_39(char={}, mode=0, text=False, part=''):
    if text:
        return "精灵(7%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.07)
    if mode == 1:
        pass


def entry_40(char={}, mode=0, text=False, part=''):
    if text:
        return "天使(7%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.07)
    if mode == 1:
        pass


def entry_41(char={}, mode=0, text=False, part=''):
    if text:
        return "龙族(7%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.07)
    if mode == 1:
        pass


def entry_106(char={}, mode=0, text=False, part=''):
    if text:
        return "人型(7%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.07)
    if mode == 1:
        pass


def entry_107(char={}, mode=0, text=False, part=''):
    if text:
        return "野兽(7%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.07)
    if mode == 1:
        pass


def entry_108(char={}, mode=0, text=False, part=''):
    if text:
        return "植物(7%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.07)
    if mode == 1:
        pass


def entry_109(char={}, mode=0, text=False, part=''):
    if text:
        return "不死(7%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.07)
    if mode == 1:
        pass


def entry_110(char={}, mode=0, text=False, part=''):
    if text:
        return "昆虫(7%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.07)
    if mode == 1:
        pass


entry_func_list[37] = [entry_enemy_type,
                       entry_37,
                       entry_38,
                       entry_39,
                       entry_40,
                       entry_41,
                       entry_106,
                       entry_107,
                       entry_108,
                       entry_109,
                       entry_110]

entry_id_bind[37] = (37, 1)
entry_id_bind[38] = (37, 2)
entry_id_bind[39] = (37, 3)
entry_id_bind[40] = (37, 4)
entry_id_bind[41] = (37, 5)
entry_id_bind[106] = (37, 6)
entry_id_bind[107] = (37, 7)
entry_id_bind[108] = (37, 8)
entry_id_bind[109] = (37, 9)
entry_id_bind[110] = (37, 10)
# endregion

# region 敌人状态词条


def entry_state_type(char={}, mode=0, text=False, part=''):
    if text:
        return "选择敌人状态"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_42(char={}, mode=0, text=False, part=''):
    if text:
        return "出血(5%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.05)
    if mode == 1:
        pass


def entry_43(char={}, mode=0, text=False, part=''):
    if text:
        return "中毒(5%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.05)
    if mode == 1:
        pass


def entry_44(char={}, mode=0, text=False, part=''):
    if text:
        return "灼烧(5%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.05)
    if mode == 1:
        pass


def entry_45(char={}, mode=0, text=False, part=''):
    if text:
        return "感电(5%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.05)
    if mode == 1:
        pass


def entry_46(char={}, mode=0, text=False, part=''):
    if text:
        return "眩晕(15%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.15)
    if mode == 1:
        pass


def entry_47(char={}, mode=0, text=False, part=''):
    if text:
        return "诅咒(10%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.10)
    if mode == 1:
        pass


def entry_48(char={}, mode=0, text=False, part=''):
    if text:
        return "睡眠(15%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.15)
    if mode == 1:
        pass


def entry_49(char={}, mode=0, text=False, part=''):
    if text:
        return "束缚(10%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.10)
    if mode == 1:
        pass


def entry_50(char={}, mode=0, text=False, part=''):
    if text:
        return "冰冻(15%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.15)
    if mode == 1:
        pass


def entry_51(char={}, mode=0, text=False, part=''):
    if text:
        return "减速(10%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.10)
    if mode == 1:
        pass


def entry_52(char={}, mode=0, text=False, part=''):
    if text:
        return "失明(10%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.10)
    if mode == 1:
        pass


def entry_53(char={}, mode=0, text=False, part=''):
    if text:
        return "石化(15%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.15)
    if mode == 1:
        pass


def entry_54(char={}, mode=0, text=False, part=''):
    if text:
        return "混乱(10%技攻)"
    if mode == 0:
        char.技能攻击力加成(0.10)
    if mode == 1:
        pass


entry_func_list[42] = [entry_state_type,
                       entry_42,
                       entry_43,
                       entry_44,
                       entry_45,
                       entry_46,
                       entry_47,
                       entry_48,
                       entry_49,
                       entry_50,
                       entry_51,
                       entry_52,
                       entry_53,
                       entry_54]

entry_id_bind[42] = (42, 1)
entry_id_bind[43] = (43, 2)
entry_id_bind[44] = (44, 3)
entry_id_bind[45] = (45, 4)
entry_id_bind[46] = (46, 5)
entry_id_bind[47] = (47, 6)
entry_id_bind[48] = (48, 7)
entry_id_bind[49] = (49, 8)
entry_id_bind[50] = (50, 9)
entry_id_bind[51] = (51, 10)
entry_id_bind[52] = (52, 11)
entry_id_bind[53] = (53, 12)
entry_id_bind[54] = (54, 13)


def entry_55(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击无力化状态下的敌人时，出血伤害 +15%"
    if mode == 0:
        char.异常增伤('出血', 0.15)
    if mode == 1:
        pass


def entry_56(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击无力化状态下的敌人时，中毒伤害 +15%"
    if mode == 0:
        char.异常增伤('中毒', 0.15)
    if mode == 1:
        pass


def entry_57(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击无力化状态下的敌人时，灼烧伤害 +15%"
    if mode == 0:
        char.异常增伤('灼烧', 0.15)
    if mode == 1:
        pass


def entry_58(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击无力化状态下的敌人时，感电伤害 +15%"
    if mode == 0:
        char.异常增伤('感电', 0.15)
    if mode == 1:
        pass


def entry_139(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个出血状态的敌人，伤害增加 356(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(356 * 10)


def entry_140(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个中毒状态的敌人，伤害增加 356(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(356 * 10)


def entry_141(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个灼烧状态的敌人，伤害增加 356(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(356 * 10)


def entry_142(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个感电状态的敌人，伤害增加 356(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(356 * 10)


def entry_143(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个冰冻状态的敌人，伤害增加 385(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(385 * 10)


def entry_144(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个减速状态的敌人，伤害增加  385(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(385 * 10)


def entry_145(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个眩晕状态的敌人，伤害增加 385(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(385 * 10)


def entry_146(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个诅咒状态的敌人，伤害增加 385(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(385 * 10)


def entry_147(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个失明状态的敌人，伤害增加 385(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(385 * 10)


def entry_148(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个石化状态的敌人，伤害增加 385(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(385 * 10)


def entry_149(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个睡眠状态的敌人，伤害增加 385(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(385 * 10)


def entry_150(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个混乱状态的敌人，伤害增加 385(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(385 * 10)


def entry_151(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个束缚状态的敌人，伤害增加 385(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(385 * 10)


# endregion

# region 攻击领主相关
def entry_216(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，中毒伤害 +20%，效果持续20秒, 20秒后，中毒伤害 -10%，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_217(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，暗属性强化 +35，效果持续20秒, 20秒后，暗属性强化 -10，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_376(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，伤害增加 N，效果持续20秒, 20秒后，攻击强化 -N，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_377(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，攻击速度 +25%，施放速度 +37.5%，效果持续20秒, 20秒后，攻击速度 -10%，施放速度 -15%，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_378(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，出血伤害 +20%，效果持续20秒, 20秒后，出血伤害 -10%，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_379(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，冰属性强化 +35，效果持续20秒, 20秒后，冰属性强化 -10，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_382(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，灼烧伤害 +20%，效果持续20秒, 20秒后，灼烧伤害 -10%，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_383(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，火属性强化 +35，效果持续20秒, 20秒后，火属性强化 -10，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_389(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，感电伤害 +20%，效果持续20秒, 20秒后，感电伤害 -10%，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_390(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，光属性强化 +35，效果持续20秒, 20秒后，光属性强化 -10，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_405(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击领主敌人时，技能攻击力 +6%"
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion


# region 消灭敌人词条
kill_num = 0
kill_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def set_kill_num(x):
    global kill_num
    kill_num = kill_num_list[x[0]]


entry_chose.append((20074, ['选择消灭敌人层数'] + ['消灭敌人：{}个'.format(i)
                                           for i in kill_num_list[1:]]))
multi_select[20074] = False
variable_set[20074] = set_kill_num


def entry_74(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，物理、魔法暴击率+2%，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.02 * kill_num)


def entry_187(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，中毒伤害 +3%，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('中毒', 0.03 * kill_num)


def entry_191(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，出血伤害 +3%，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.03 * kill_num)


def entry_196(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，灼烧伤害 +3%，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('灼烧', 0.03 * kill_num)


def entry_231(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，冰属性强化 +4，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(4 * kill_num)


def entry_232(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，火属性强化 +4，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(4 * kill_num)


def entry_233(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，光属性强化 +4，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(4 * kill_num)


def entry_234(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，暗属性强化 +4，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(4 * kill_num)


def entry_295(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，Lv80~95技能Lv+1，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.技能等级加成('所有', 80, 95, kill_num)


def entry_300(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，Lv70~75技能Lv+1，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.技能等级加成('所有', 70, 75, kill_num)


def entry_308(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，Lv35~40技能Lv+1，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.技能等级加成('所有', 35, 40, kill_num)


def entry_322(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，Lv45~60技能Lv+1，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.技能等级加成('所有', 45, 60, kill_num)


def entry_329(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，技能攻击力 +2%(觉醒技能除外)，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.批量技能倍率加成(1, 100, 0.02 * kill_num, [50, 85, 100])


def entry_360(char={}, mode=0, text=False, part=''):
    if text:
        return "每消灭一个敌人，获得1层强化(最多10层)，攻击领主敌人时消耗所有层数，每消耗1层，感电伤害 +3%，效果持续60秒"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('感电', 0.03 * kill_num)


def entry_235(char={}, mode=0, text=False, part=''):
    if text:
        return "消灭敌人时，所有速度 +5%，效果持续10秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.05 * 5)
        char.释放速度增加(0.05 * 5)
        char.移动速度增加(0.05 * 5)


def entry_239(char={}, mode=0, text=False, part=''):
    if text:
        return "消灭敌人时，恢复5%的已消耗HP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_240(char={}, mode=0, text=False, part=''):
    if text:
        return "消灭敌人时，恢复5%的已消耗MP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1175(char={}, mode=0, text=False, part=''):
    if text:
        return "消灭敌人时，Lv1~80所有技能范围 +5%(觉醒除外，最多叠加5次), 施放技能时，技能攻击力 -4%，持续10秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion

# region 无色相关词条


def entry_75(char={}, mode=0, text=False, part=''):
    if text:
        return "使用消耗10个以上无色小晶块的技能时，技能冷却时间恢复速度 +30%，效果持续20秒(冷却时间15秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.3)


def entry_222(char={}, mode=0, text=False, part=''):
    if text:
        return "使用消耗10个以上无色小晶块的技能时，攻击速度 +30%，施放速度 +45%，效果持续20秒(冷却时间15秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.3)
        char.释放速度增加(0.45)


def entry_249(char={}, mode=0, text=False, part=''):
    if text:
        return "施放不消耗无色小晶块的技能时，技能攻击力 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_878(char={}, mode=0, text=False, part=''):
    if text:
        return "不消耗无色小晶块的技能攻击力 -5%, 消耗无色小晶块的技能攻击力 +10%, 每次施放消耗无色小晶块的技能时，该技能的无色小晶块消耗量翻倍(最多叠加3次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_899(char={}, mode=0, text=False, part=''):
    if text:
        return "当施放不消耗无色小晶块的技能时，附加一个相当于HP MAX数值10%的保护罩，持续1.5秒(冷却时间0.5秒，最大叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1096(char={}, mode=0, text=False, part=''):
    if text:
        return "施放不消耗无色小晶块的技能时，技能MP消耗量-10%，效果持续10秒(最多叠加3次), - 当施放消耗无色小晶块的技能时，该效果会被重置"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1108(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，暗属性强化 +10，效果持续20秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1109(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，冰属性强化 +10，效果持续20秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1110(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，根据无色消耗量，获得能量(最多100),  获得的能量达100时，消耗所有能量，使用的技能剩余冷却时间 -5%(觉醒除外),  普攻、施放无需无色技能时，消耗1点能量"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1111(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，光属性强化 +10，效果持续20秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1112(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，火属性强化 +10，效果持续20秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1113(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，所有属性强化 +8，效果持续20秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1114(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，移动速度 +10%，效果持续10秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1115(char={}, mode=0, text=False, part=''):
    if text:
        return "施放不消耗无色小晶块的技能时，攻击速度 +10%，施放速度 +15%(冷却时间5秒，最多叠加1次),  无需无色技能冷却时间 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1116(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗3个以上无色小晶块的技能时，所有属性强化 +20，效果持续20秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1117(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，10秒内恢复5%的MP(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1118(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，技能MP消耗量 -10%，效果持续20秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1119(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，所有属性强化 +3，效果持续10秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1120(char={}, mode=0, text=False, part=''):
    if text:
        return "施放消耗无色小晶块的技能时，攻击速度+5%，施放速度+7.5%，效果持续30秒(冷却时间5秒，最多叠加3次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1138(char={}, mode=0, text=False, part=''):
    if text:
        return "输入技能指令施放消耗无色小晶块的技能时，奖励效果+400%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1238(char={}, mode=0, text=False, part=''):
    if text:
        return "使用消耗无色小晶块的技能时，召唤D011-Risa，适用以下效果，持续20秒(冷却时间0.5秒，最多5个), - 地图中最强的敌人处于的异常状态适用于D011-Risa, - 在D011-Risa周围500px范围内是，所有异常状态抗性 +2%(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


# endregion

# region 连击相关词条
combo_num = 0
combo_num_list = [0, 3, 6, 9, 12, 15, 18, 21,
                  24, 27, 30, 50, 200, 400, 600, 800, 1000]


def set_combo_num(x):
    global combo_num
    combo_num = combo_num_list[x[0]]


entry_chose.append((20113, ['选择连击次数'] + ['{}连击'.format(i)
                                         for i in combo_num_list[1:]]))
multi_select[20113] = False
variable_set[20113] = set_combo_num


def entry_113(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成3次连击，光属性强化+4(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(4 * min(10, int(combo_num / 3)))


def entry_116(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成3次连击，攻击速度 +3%，施放速度 +4.5%(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度加成(0.03 * min(10, int(combo_num / 3)))
        char.释放速度加成(0.045 * min(10, int(combo_num / 3)))


def entry_117(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成3次连击，伤害增加 416(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(416 * min(10, int(combo_num / 3)))


def entry_122(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成3次连击，移动速度 +3%(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.移动速度加成(0.03 * min(10, int(combo_num / 3)))


def entry_153(char={}, mode=0, text=False, part=''):
    if text:
        return "每进行5次攻击，获得效果, - 伤害增加 N, - 物理防御力 -500"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_219(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成3次连击，物理、魔法防御力 +1400(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_220(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成3次连击，回避率 +3%(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.回避率增加(0.03 * min(10, int(combo_num / 3)))


def entry_221(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成3次连击，物理、魔法暴击率 +2%(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.02 * min(10, int(combo_num / 3)))


def entry_282(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成10次连击，敌人韧性减少量 +5%(最多增加30%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_284(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成50次连击，伤害增加 N"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_336(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成3次连击，火属性强化+4(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(4 * min(10, int(combo_num / 3)))


def entry_337(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成3次连击，冰属性强化+4(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(4 * min(10, int(combo_num / 3)))


def entry_338(char={}, mode=0, text=False, part=''):
    if text:
        return "每达成3次连击，暗属性强化+4(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(4 * min(10, int(combo_num / 3)))


def entry_891(char={}, mode=0, text=False, part=''):
    if text:
        return "达成30次连击时，伤害增加 2223，持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        if combo_num >= 30:
            char.伤害量加成(2223)


def entry_892(char={}, mode=0, text=False, part=''):
    if text:
        return "达成15次连击时，450px范围内所有敌人进入出血状态(冷却时间8秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_893(char={}, mode=0, text=False, part=''):
    if text:
        return "达成200次连击时，500px范围内绿名怪、领主剩余HP -1%(冷却时间30秒，辅助职业不适用该效果)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_911(char={}, mode=0, text=False, part=''):
    if text:
        return "达成10次连击时，伤害增加 3705，技能MP消耗量 +175%，持续30秒"
    if mode == 0:
        pass
    if mode == 1:
        if combo_num >= 10:
            char.伤害量加成(3705)
            char.MP消耗量加成(1.75)


def entry_912(char={}, mode=0, text=False, part=''):
    if text:
        return "达成20次连击时，无视敌人8%的防御力，持续30秒"
    if mode == 0:
        pass
    if mode == 1:
        if combo_num >= 20:
            char.百分比防御减少(0.08)


def entry_1044(char={}, mode=0, text=False, part=''):
    if text:
        return "每连击200次，武器耐久度 -1(冷却时间10秒), 每次连击减少耐久时，所有技能冷却时间恢复速度 +10%(最多叠加5次，觉醒除外)"
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.1 * min(10, int(combo_num / 200)), [50, 85, 100])


def entry_1242(char={}, mode=0, text=False, part=''):
    if text:
        return "地下城入场时激活Buff，冷却时间恢复速度 +25%(最多叠加1次，觉醒技能除外), 每达成6次连击，冷却时间恢复速度 -5%(最多叠加5次), - 施放技能时，冷却时间恢复速度减少效果叠加次数 -1"
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.25 - 0.05 *
                    min(5, int(combo_num / 6)), [50, 85, 100])
# endregion

# region 施放冷却时间词条


def entry_118(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在20秒以下的技能时，灼烧伤害 +10%，效果持续3秒(冷却时间3秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('灼烧', 0.1)


def entry_119(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在20秒以下的技能时，出血伤害 +10%，效果持续3秒(冷却时间3秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.1)


def entry_120(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在20秒以下的技能时，感电伤害 +10%，效果持续3秒(冷却时间3秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('感电', 0.1)


def entry_121(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在20秒以下的技能时，中毒伤害 +10%，效果持续3秒(冷却时间3秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('中毒', 0.1)


def entry_245(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在25秒以上的技能时，出血伤害 +20%，效果持续10秒(冷却时间5秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.20)


def entry_246(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在25秒以上的技能时，感电伤害 +20%，效果持续10秒(冷却时间5秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('感电', 0.20)


def entry_257(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在25秒以上的技能时，灼烧伤害 +20%，效果持续10秒(冷却时间5秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('灼烧', 0.2)


def entry_258(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在25秒以上的技能时，中毒伤害 +20%，效果持续10秒(冷却时间5秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('中毒', 0.2)


def entry_267(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在20秒以下的技能时，火属性强化 +25，效果持续10秒(冷却时间3秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(25)


def entry_268(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在20秒以下的技能时，冰属性强化 +25，效果持续10秒(冷却时间3秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(25)


def entry_269(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在20秒以下的技能时，光属性强化 +25，效果持续10秒(冷却时间3秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(25)


def entry_270(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在20秒以下的技能时，暗属性强化 +25，效果持续10秒(冷却时间3秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(25)


def entry_346(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在25秒以上的技能时，火属性强化 +25，效果持续10秒(冷却时间5秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_347(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在25秒以上的技能时，冰属性强化 +25，效果持续10秒(冷却时间5秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_348(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在25秒以上的技能时，光属性强化 +25，效果持续10秒(冷却时间5秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_349(char={}, mode=0, text=False, part=''):
    if text:
        return "施放冷却时间在25秒以上的技能时，暗属性强化 +25，效果持续10秒(冷却时间5秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion

# region 异常抗性词条


def entry_169(char={}, mode=0, text=False, part=''):
    if text:
        return "所有异常状态抗性 +20%, 所有属性强化 -15"
    if mode == 0:
        char.所有属性强化加成(-15)
    if mode == 1:
        pass


def entry_188(char={}, mode=0, text=False, part=''):
    if text:
        return "感电抗性 +20%, 攻击速度 -15%, 施放速度 -22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_193(char={}, mode=0, text=False, part=''):
    if text:
        return "中毒抗性 +20%, 攻击速度 -15%, 施放速度-22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_199(char={}, mode=0, text=False, part=''):
    if text:
        return "冰冻抗性 +20%, 攻击速度 -15%, 施放速度-22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_204(char={}, mode=0, text=False, part=''):
    if text:
        return "减速抗性 +20%, 攻击速度 -15%, 施放速度-22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_229(char={}, mode=0, text=False, part=''):
    if text:
        return "诅咒抗性 +20%, 攻击速度 -15%, 施放速度-22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_285(char={}, mode=0, text=False, part=''):
    if text:
        return "出血抗性 +20%, 攻击速度 -15%, 施放速度-22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_293(char={}, mode=0, text=False, part=''):
    if text:
        return "灼烧抗性 +20%, 攻击速度 -15%, 施放速度-22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_305(char={}, mode=0, text=False, part=''):
    if text:
        return "失明抗性 +20%, 攻击速度 -15%, 施放速度-22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_309(char={}, mode=0, text=False, part=''):
    if text:
        return "混乱抗性 +20%, 攻击速度 -15%, 施放速度-22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_323(char={}, mode=0, text=False, part=''):
    if text:
        return "束缚抗性 +20%, 攻击速度 -15%, 施放速度-22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_361(char={}, mode=0, text=False, part=''):
    if text:
        return "睡眠抗性 +20%, 攻击速度 -15%, 施放速度 -22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_366(char={}, mode=0, text=False, part=''):
    if text:
        return "眩晕抗性 +20%, 攻击速度 -15%, 施放速度 -22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


def entry_372(char={}, mode=0, text=False, part=''):
    if text:
        return "石化抗性 +20%, 攻击速度 -15%, 施放速度 -22.5%"
    if mode == 0:
        char.攻击速度增加(-0.15)
        char.释放速度增加(-0.225)
    if mode == 1:
        pass


# endregion

# region 队友数量词条
teammate_num = 0
teammate_num_list = [0, 1, 2, 3, 4]


def set_teammate_num(x):
    global teammate_num
    teammate_num = teammate_num_list[x[0]]


entry_chose.append((20165, ['选择队员数量'] + ['队员：{}名'.format(i)
                                         for i in teammate_num_list[1:]]))
multi_select[20165] = False
variable_set[20165] = set_teammate_num


def entry_165(char={}, mode=0, text=False, part=''):
    if text:
        return "队伍中每存在一名获得该词条的队友(包括自己)，伤害增加 N"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_166(char={}, mode=0, text=False, part=''):
    if text:
        return "队伍中每存在一名获得该词条的队友(包括自己)，所受伤害 -7%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1018(char={}, mode=0, text=False, part=''):
    if text:
        return "每1名包括自身在内的队友，伤害增加 371(最多叠加4次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(371 * teammate_num)


def entry_1019(char={}, mode=0, text=False, part=''):
    if text:
        return "每1名获得该装备词条的自身与队友，伤害增加 1112(最多叠加4次)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(1112 * teammate_num)


def entry_1244(char={}, mode=0, text=False, part=''):
    if text:
        return "物理伤害减少率和魔法伤害减少率总和超过60%以上时，攻击强化 4001, 每存在1名队友，所有技能范围 +5%(最多叠加4次，觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(4001)


# endregion

# region 选择敌人数量
enemy_num = 0
enemy_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60]


def set_enemy_num(x):
    global enemy_num
    enemy_num = enemy_num_list[x[0]]


entry_chose.append((20183, ['选择敌人数量'] + ['{}个敌人'.format(i)
                                         for i in enemy_num_list[1:]]))
multi_select[20183] = False
variable_set[20183] = set_enemy_num


def entry_183(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个敌人，火属性强化 +7(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.火属性强化加成(7 * enemy_num)


def entry_184(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个敌人，冰属性强化 +7(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.冰属性强化加成(7 * enemy_num)


def entry_185(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个敌人，光属性强化 +7(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.光属性强化加成(7 * enemy_num)


def entry_186(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个敌人，暗属性强化 +7(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.暗属性强化加成(7 * enemy_num)


def entry_266(char={}, mode=0, text=False, part=''):
    if text:
        return "地图每存在1个敌人，伤害增加 44(最多叠加60次), 受到总HP1%以上伤害时，攻击强化效果叠加次数 -12"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(44 * enemy_num)


def entry_283(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个敌人，技能冷却时间 -4%(觉醒技能除外，最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.04 * min(10, enemy_num), [50, 85, 100])


def entry_289(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个敌人，攻击速度+3%，施放速度+4.5%(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.03 * min(10, enemy_num))
        char.释放速度增加(0.045 * min(10, enemy_num))


def entry_290(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个敌人，物理、魔法防御力 +1500(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_291(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个敌人，所有属性抗性 +3(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性抗性加成(3 * min(10, enemy_num))


def entry_292(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个敌人，所有异常状态抗性 +3%(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_409(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内，每存在1个敌人，物理、魔法暴击率 +2%(最多增加20%)"
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.02 * min(10, enemy_num))


# endregion

# region 选择地下城类型
def entry_dungeons_type(char={}, mode=0, text=False, part=''):
    if text:
        return "选择地下城类型"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_189(char={}, mode=0, text=False, part=''):
    if text:
        return "[贵族机要]15%技攻"
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.15)


def entry_207(char={}, mode=0, text=False, part=''):
    if text:
        return "[毁坏的寂静城(高级)]15%技攻"
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.15)


def entry_225(char={}, mode=0, text=False, part=''):
    if text:
        return "[机械战神试验场]15%技攻"
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.15)


entry_func_list[187] = [entry_dungeons_type,
                        entry_189,
                        entry_207,
                        entry_225]
entry_id_bind[189] = (189, 1)
entry_id_bind[207] = (189, 2)
entry_id_bind[225] = (189, 3)
# endregion

# region 敌人韧性相关


def entry_194(char={}, mode=0, text=False, part=''):
    if text:
        return "每减少敌人10%的韧性，Lv45技能冷却时间恢复速度 +3%(最多增加30%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_195(char={}, mode=0, text=False, part=''):
    if text:
        return "根据敌人韧性破坏次数，伤害增加 N"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_200(char={}, mode=0, text=False, part=''):
    if text:
        return "每减少敌人10%的韧性，Lv75技能冷却时间恢复速度 +3%(最多增加30%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_205(char={}, mode=0, text=False, part=''):
    if text:
        return "根据敌人韧性破坏次数，出血伤害 +5%(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.05 * 5)


def entry_206(char={}, mode=0, text=False, part=''):
    if text:
        return "根据敌人韧性破坏次数，灼烧伤害 +5%(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('灼烧', 0.05 * 5)


def entry_213(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_286(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性每减少10%，Lv95技能冷却时间恢复速度 +3%(最多增加30%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_287(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性每减少10%，Lv60技能冷却时间恢复速度 +3%(最多增加30%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_310(char={}, mode=0, text=False, part=''):
    if text:
        return "根据敌人韧性破坏次数，中毒伤害 +5%(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_311(char={}, mode=0, text=False, part=''):
    if text:
        return "根据敌人韧性破坏次数，感电伤害 +5%(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_362(char={}, mode=0, text=False, part=''):
    if text:
        return "每减少敌人10%的韧性，Lv80技能冷却时间恢复速度 +3%(最多增加30%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_367(char={}, mode=0, text=False, part=''):
    if text:
        return "每减少敌人10%的韧性，Lv70技能冷却时间恢复速度 +3%(最多增加30%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_373(char={}, mode=0, text=False, part=''):
    if text:
        return "每减少敌人10%的韧性，Lv35技能冷却时间恢复速度 +3%(最多增加30%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_374(char={}, mode=0, text=False, part=''):
    if text:
        return "每减少敌人10%的韧性，Lv40技能冷却时间恢复速度 +3%(最多增加30%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_396(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +10%, 自身触发的眩晕状态持续时间 +1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_397(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +10%, 自身触发的诅咒状态持续时间 +1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_398(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +10%, 自身触发的石化状态持续时间 +1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_403(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +10%, 自身触发的冰冻状态持续时间 +1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_404(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +10%, 自身触发的失明状态持续时间 +1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_406(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +10%, 自身触发的睡眠状态持续时间 +1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_407(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +10%, 自身触发的减速状态持续时间 +1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_408(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +10%, 自身触发的混乱状态持续时间 +1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1258(char={}, mode=0, text=False, part=''):
    if text:
        return "敌人韧性减少量 +25%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1259(char={}, mode=0, text=False, part=''):
    if text:
        return "每减少敌人10%的韧性，技能攻击力 +2%(最多叠加10次), - 无力化效果消失时，技能攻击力增加效果重置"
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion

# region 异常状态解除相关


def entry_201(char={}, mode=0, text=False, part=''):
    if text:
        return "自身异常状态解除时，Lv60技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_202(char={}, mode=0, text=False, part=''):
    if text:
        return "自身异常状态解除时，Lv45技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_203(char={}, mode=0, text=False, part=''):
    if text:
        return "自身异常状态解除时，Lv35技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_208(char={}, mode=0, text=False, part=''):
    if text:
        return "自身异常状态解除时，Lv40技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_209(char={}, mode=0, text=False, part=''):
    if text:
        return "自身异常状态解除时，Lv70技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_210(char={}, mode=0, text=False, part=''):
    if text:
        return "自身异常状态解除时，Lv75技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_214(char={}, mode=0, text=False, part=''):
    if text:
        return "自身异常状态解除时，Lv80技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_215(char={}, mode=0, text=False, part=''):
    if text:
        return "自身异常状态解除时，Lv95技能技能冷却时间恢复速度 +30%，效果持续5秒(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion

# region 普攻相关


def entry_211(char={}, mode=0, text=False, part=''):
    if text:
        return "施放普通攻击最后一击时，冷却时间最长的技能剩余冷却时间 -3%(冷却时间1秒，觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_212(char={}, mode=0, text=False, part=''):
    if text:
        return "施放普通攻击最后一击时，冷却时间最短的技能剩余冷却时间 -3%(冷却时间1秒，觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1060(char={}, mode=0, text=False, part=''):
    if text:
        return "普通攻击时，不消耗无色小晶块的技能剩余冷却时间 -1%(冷却时间0.1秒),  施放消耗无色小晶块的技能时，不消耗无色小晶块的技能冷却时间+2%，持续30秒(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_380(char={}, mode=0, text=False, part=''):
    if text:
        return "施放普通攻击最后一击时，伤害增加 N，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_391(char={}, mode=0, text=False, part=''):
    if text:
        return "施放普通攻击最后一击时，攻击速度 +20%，施放速度 +30%，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1056(char={}, mode=0, text=False, part=''):
    if text:
        return "普通攻击时，Lv15~35主动技能攻击力 +3%，效果持续10秒(最多叠加10次), 施放Lv45以上技能时，技能攻击力增加效果叠加次数 -1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1057(char={}, mode=0, text=False, part=''):
    if text:
        return "普通攻击时，Lv15~35主动技能冷却时间恢复速度 +1%，效果持续10秒(最多叠加10次), 施放Lv45以上技能时，技能冷却时间恢复速度增加效果叠加次数 -1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1059(char={}, mode=0, text=False, part=''):
    if text:
        return "普通攻击、跳跃攻击、前冲攻击时，有10%的几率使适用攻击力 +300%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1061(char={}, mode=0, text=False, part=''):
    if text:
        return "普通攻击时，攻击速度 +10%，施放速度 +10%，效果持续2秒(最多叠加3次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1062(char={}, mode=0, text=False, part=''):
    if text:
        return "普通攻击时，基础精通攻击力 +15%，持续5秒(冷却时间0.1秒，最多叠加3次),  施放技能时，消耗所有基础精通重叠次数，根据消耗率比例，技能攻击力 +5%，技能冷却时间 +8%，效果持续5秒(只在没有该Buff时发动)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1063(char={}, mode=0, text=False, part=''):
    if text:
        return "普通攻击时，有15%的几率，使敌人随机进入灼烧、感电、出血、中毒状态中的1种(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1064(char={}, mode=0, text=False, part=''):
    if text:
        return "普通攻击时，攻击速度 +10%，施放速度 +10%，效果持续5秒(冷却时间0.1秒，最多叠加3次)"
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion

# region 敌人距离相关


def entry_253(char={}, mode=0, text=False, part=''):
    if text:
        return "越靠近敌人时，技能攻击力 +1%(与敌人距离50px以内时，最多增加5%)"
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)


def entry_254(char={}, mode=0, text=False, part=''):
    if text:
        return "越远离敌人时，技能攻击力 +1%(与敌人距离300px以外时，最多增加5%)"
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)


def entry_1181(char={}, mode=0, text=False, part=''):
    if text:
        return "与敌人距离在100px以内，伤害增加 2964"
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion

# region 进入地下城时相关


def entry_223(char={}, mode=0, text=False, part=''):
    if text:
        return "进入地下城时，每30秒以相同几率发动属性，效果持续20秒, - 攻击速度 +25%, - 施放速度 +37.5%, - 移动速度 +25%"
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(0.25)
        char.释放速度增加(0.375)
        char.移动速度增加(0.25)


def entry_224(char={}, mode=0, text=False, part=''):
    if text:
        return "进入地下城时，每30秒以相同几率发动属性，效果持续20秒, - 伤害增加 N, - 所受伤害 -25%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_997(char={}, mode=0, text=False, part=''):
    if text:
        return "进入地下城时，伤害增加 2223, 技能MP消耗量 +100%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_998(char={}, mode=0, text=False, part=''):
    if text:
        return "进入地下城时，制造一个草莓极光，被击5次后被销毁(冷却时间30秒), - 草莓极光状态下，所受伤害 -15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1103(char={}, mode=0, text=False, part=''):
    if text:
        return "施放技能时，攻击速度+5%，施放速度+8%，效果持续10秒(最多叠加5次), 进入地下城时，技能冷却时间 -5%(觉醒技能除外)，技能攻击力 -2%"
    if mode == 0:
        pass
    if mode == 1:
        pass
# endregion


def entry_218(char={}, mode=0, text=False, part=''):
    if text:
        return "受基础精通影响攻击时，出血、中毒、灼烧、感电伤害 +20%，效果持续10秒(冷却时间15秒)"
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.2)
        char.异常增伤('中毒', 0.2)
        char.异常增伤('灼烧', 0.2)
        char.异常增伤('感电', 0.2)


def entry_226(char={}, mode=0, text=False, part=''):
    if text:
        return "5秒未前冲时，伤害增加 267(最多叠加10次), 前冲时，攻击强化效果叠加次数 -1"
    if mode == 0:
        pass
    if mode == 1:
        char.伤害量加成(267 * 10)


def entry_227(char={}, mode=0, text=False, part=''):
    if text:
        return "5秒未被击时，所受伤害 -3%(最多叠加10次), 受到总HP1%以上伤害时，所受伤害减少效果叠加次数 -2"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_228(char={}, mode=0, text=False, part=''):
    if text:
        return "2秒滞空时，所有属性强化 +6(最多叠加10次), 受到总HP1%以上伤害时，所有属性强化增加效果叠加次数 -2"
    if mode == 0:
        pass
    if mode == 1:
        char.所有属性强化加成(6 * 10)


def entry_230(char={}, mode=0, text=False, part=''):
    if text:
        return "<成长、传送属性>的属性触发几率 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_236(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv95所有技能冷却时间 +30%, Lv80所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(95, 95, -0.3)
        char.技能倍率加成(80, 0.2)
    if mode == 1:
        pass


def entry_237(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv80所有技能冷却时间 +30%, Lv80所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(80, 80, -0.3)
        char.技能倍率加成(95, 0.2)
    if mode == 1:
        pass


def entry_238(char={}, mode=0, text=False, part=''):
    if text:
        return "物理防御力+25000, 魔法防御力+25000, 物理暴击率 -8%, 魔法暴击率 -8%"
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(-0.08)


def entry_241(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv35所有技能冷却时间 +30%, Lv35所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(35, 35, -0.3)
        char.技能倍率加成(35, 0.2)
    if mode == 1:
        pass


def entry_242(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv40所有技能冷却时间 +30%, Lv35所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(40, 40, -0.3)
        char.技能倍率加成(35, 0.2)
    if mode == 1:
        pass


def entry_243(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv40所有技能冷却时间 +30%, Lv40所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(40, 40, -0.3)
        char.技能倍率加成(40, 0.2)
    if mode == 1:
        pass


def entry_244(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv45所有技能冷却时间 +30%, Lv40所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(45, 45, -0.3)
        char.技能倍率加成(40, 0.2)
    if mode == 1:
        pass


def entry_247(char={}, mode=0, text=False, part=''):
    if text:
        return "使用技能指令施放技能时，该技能攻击力 +12%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_248(char={}, mode=0, text=False, part=''):
    if text:
        return "技能指令效果 +100%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_250(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv45所有技能冷却时间 +30%, Lv45所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(45, 45, -0.3)
        char.技能倍率加成(45, 0.2)
    if mode == 1:
        pass


def entry_251(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv60所有技能冷却时间 +30%, Lv45所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(60, 60, -0.3)
        char.技能倍率加成(45, 0.2)
    if mode == 1:
        pass


def entry_252(char={}, mode=0, text=False, part=''):
    if text:
        return "剩余MP超过50%以上时，物理、魔法暴击率 +15%"
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.15)


def entry_255(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv60所有技能冷却时间 +30%, Lv60所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(60, 60, -0.3)
        char.技能倍率加成(60, 0.2)
    if mode == 1:
        pass


def entry_256(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv70所有技能冷却时间 +30%, Lv60所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(70, 70, -0.3)
        char.技能倍率加成(60, 0.2)
    if mode == 1:
        pass


def entry_259(char={}, mode=0, text=False, part=''):
    if text:
        return "技能快捷栏中每存在1个空栏，技能攻击力 +2%(最多增加12%)"
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.12)


def entry_260(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv70所有技能冷却时间 +30%, Lv70所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(70, 70, -0.3)
        char.技能倍率加成(70, 0.2)
    if mode == 1:
        pass


def entry_261(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv75所有技能冷却时间 +30%, Lv70所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(75, 75, -0.3)
        char.技能倍率加成(70, 0.2)
    if mode == 1:
        pass


def entry_262(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv75所有技能冷却时间 +30%, Lv75所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(75, 75, -0.3)
        char.技能倍率加成(75, 0.2)
    if mode == 1:
        pass


def entry_263(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv80所有技能冷却时间 +30%, Lv75所有技能攻击力 +20%"
    if mode == 0:
        char.技能冷却缩减(80, 80, -0.3)
        char.技能倍率加成(75, 0.2)
    if mode == 1:
        pass


def entry_264(char={}, mode=0, text=False, part=''):
    if text:
        return "移动速度 +30%, 物理防御力-20000, 魔法防御力-20000"
    if mode == 0:
        char.移动速度增加(0.3)
    if mode == 1:
        pass


def entry_265(char={}, mode=0, text=False, part=''):
    if text:
        return "被攻击时，有30%的几率不会被击退(冷却时间3秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_271(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv45技能攻击力 +20%"
    if mode == 0:
        char.技能倍率加成(45, 0.2)
    if mode == 1:
        pass


def entry_272(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv35技能攻击力 +20%"
    if mode == 0:
        char.技能倍率加成(35, 0.2)
    if mode == 1:
        pass


def entry_273(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv45技能冷却时间 -20%"
    if mode == 0:
        char.技能冷却缩减(45, 45, 0.2)
    if mode == 1:
        pass


def entry_274(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv35技能冷却时间 -20%"
    if mode == 0:
        char.技能冷却缩减(35, 35, 0.2)
    if mode == 1:
        pass


def entry_275(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv45技能Lv+1"
    if mode == 0:
        char.技能等级加成('所有', 45, 45, 1)
    if mode == 1:
        pass


def entry_276(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv35技能Lv+1"
    if mode == 0:
        char.技能等级加成('所有', 35, 35, 1)
    if mode == 1:
        pass


def entry_277(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv40技能攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_278(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv30技能攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_279(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv40技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_280(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv30技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_281(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv40技能Lv+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_288(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv15技能时，进入2秒霸体状态，霸体解除时，攻击速度+15%，施放速度+22.5%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_294(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，伤害增加 111(最多叠加20次), 受到总HP1%以上伤害时，攻击强化效果叠加次数 -4"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_296(char={}, mode=0, text=False, part=''):
    if text:
        return "出血伤害 +30%, 所受伤害 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_297(char={}, mode=0, text=False, part=''):
    if text:
        return "感电伤害 +30%, 所受伤害 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_298(char={}, mode=0, text=False, part=''):
    if text:
        return "灼烧伤害 +30%, 所受伤害 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_299(char={}, mode=0, text=False, part=''):
    if text:
        return "中毒伤害 +30%, 所受伤害 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_301(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有异常状态抗性之和超过50%以上时，火属性强化 +35"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_302(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有异常状态抗性之和超过50%以上时，冰属性强化 +35"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_303(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有异常状态抗性之和超过50%以上时，光属性强化 +35"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_304(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有异常状态抗性之和超过50%以上时，暗属性强化 +35"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_306(char={}, mode=0, text=False, part=''):
    if text:
        return "消耗品的Buff效果 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_307(char={}, mode=0, text=False, part=''):
    if text:
        return "消耗品的持续时间 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_312(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv60技能攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_313(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv70技能攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_314(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv60技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_315(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv70技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_316(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv60技能Lv+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_317(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv70技能Lv+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_318(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv20技能攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_319(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv25技能攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_320(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv20技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_321(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv25技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_324(char={}, mode=0, text=False, part=''):
    if text:
        return "被攻击时，有30%的几率施放Lv20[念气罩](冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_325(char={}, mode=0, text=False, part=''):
    if text:
        return "被攻击时，有30%的几率施放Lv20[圣光守护](冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_326(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv95技能攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_327(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv95技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_328(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv95技能Lv+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_330(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv75技能攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_331(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv80技能攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_332(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv75技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_333(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv80技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_334(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv75技能Lv+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_335(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv80技能Lv+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_339(char={}, mode=0, text=False, part=''):
    if text:
        return "火属性抗性 +40, 命中率 -15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_340(char={}, mode=0, text=False, part=''):
    if text:
        return "冰属性抗性 +40, 命中率 -15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_341(char={}, mode=0, text=False, part=''):
    if text:
        return "光属性抗性 +40, 命中率 -15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_342(char={}, mode=0, text=False, part=''):
    if text:
        return "暗属性抗性 +40, 命中率 -15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_343(char={}, mode=0, text=False, part=''):
    if text:
        return "自身移动速度超过100%以上时，HP、MP MAX +2000"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_344(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有属性抗性之和超过250以上时，出血伤害 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_345(char={}, mode=0, text=False, part=''):
    if text:
        return "命中率 +20%, HP、MP MAX -1200"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_350(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有属性抗性之和超过250以上时，灼烧伤害 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_351(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击普通敌人时，技能攻击力 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_352(char={}, mode=0, text=False, part=''):
    if text:
        return "每12%的出血抗性，出血伤害 +5%(最多增加15%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_353(char={}, mode=0, text=False, part=''):
    if text:
        return "每12%的中毒抗性，中毒伤害 +5%(最多增加15%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_354(char={}, mode=0, text=False, part=''):
    if text:
        return "每12%的感电抗性，感电伤害 +5%(最多增加15%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_355(char={}, mode=0, text=False, part=''):
    if text:
        return "每12%的灼烧抗性，灼烧伤害 +5%(最多增加15%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_356(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所有属性抗性之和超过250以上时，感电伤害 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_357(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv25~40技能时，Lv45技能剩余冷却时间 -10%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_358(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv30~45技能时，Lv60技能剩余冷却时间 -10%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_359(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv15~30技能时，Lv35技能剩余冷却时间 -10%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_363(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv35~60技能时，Lv70技能剩余冷却时间 -10%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_364(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv40~70技能时，Lv75技能剩余冷却时间 -10%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_365(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv20~35技能时，Lv40技能剩余冷却时间 -10%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_368(char={}, mode=0, text=False, part=''):
    if text:
        return "装备保护罩效果 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_369(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击绿名/稀有敌人时，技能攻击力 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_370(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv60~80技能时，Lv95技能剩余冷却时间 -10%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_371(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv40~75技能时，Lv80技能剩余冷却时间 -10%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_375(char={}, mode=0, text=False, part=''):
    if text:
        return "剩余MP在30%以下时，消耗10个无色小晶块，恢复30%的MP(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_381(char={}, mode=0, text=False, part=''):
    if text:
        return "受到领主敌人攻击时，所受伤害 -20%，效果持续20秒, 20秒后，所受伤害 +10%，效果持续10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_384(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv20技能时，进入2秒霸体状态，霸体解除时，攻击速度+15%，施放速度+22.5%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_385(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv25技能时，进入2秒霸体状态，霸体解除时，攻击速度+15%，施放速度+22.5%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_386(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv30技能时，进入2秒霸体状态，霸体解除时，攻击速度+15%，施放速度+22.5%(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_387(char={}, mode=0, text=False, part=''):
    if text:
        return "正面攻击敌人时，技能攻击力 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_388(char={}, mode=0, text=False, part=''):
    if text:
        return "背击攻击敌人时，技能攻击力 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_392(char={}, mode=0, text=False, part=''):
    if text:
        return "受基础精通影响攻击时，所有属性强化 +35，效果持续10秒(冷却时间15秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_393(char={}, mode=0, text=False, part=''):
    if text:
        return "破招攻击时，Lv1~30技能剩余冷却时间 -10%(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_394(char={}, mode=0, text=False, part=''):
    if text:
        return "出血抗性 +5%, 出血伤害 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_395(char={}, mode=0, text=False, part=''):
    if text:
        return "中毒抗性 +5%, 中毒伤害 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_399(char={}, mode=0, text=False, part=''):
    if text:
        return "破招攻击时，技能攻击力 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_400(char={}, mode=0, text=False, part=''):
    if text:
        return "非破招攻击时，技能攻击力 +8%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_401(char={}, mode=0, text=False, part=''):
    if text:
        return "灼烧抗性 +5%, 灼烧伤害 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_402(char={}, mode=0, text=False, part=''):
    if text:
        return "感电抗性 +5%, 感电伤害 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_538(char={}, mode=0, text=False, part=''):
    if text:
        return "Lv30 buff技能Lv+1, Lv50 主动技能Lv+2"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_539(char={}, mode=0, text=False, part=''):
    if text:
        return "[嗜血]蕃力功能删除, [嗜血]可以在施放技能时发动"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_540(char={}, mode=0, text=False, part=''):
    if text:
        return "施放时[嗜血]时，消耗10%HP获得3层血气(最大10层）, 进入地下城时获得1层血气"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_541(char={}, mode=0, text=False, part=''):
    if text:
        return "[血气之刃]、[暴怒狂斩]技能使用时消耗1层血气，该技能的技能攻击力+30%、攻击范围+15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_542(char={}, mode=0, text=False, part=''):
    if text:
        return "[血气之刃]、[暴怒狂斩]攻击时恢复5%的最大HP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_543(char={}, mode=0, text=False, part=''):
    if text:
        return "[万剑归宗]技能终结攻击发动后不会结束(每次万剑归宗只适用一次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_544(char={}, mode=0, text=False, part=''):
    if text:
        return "施放适用于基础精通的技能时，[万剑归宗]持续时间+0.5秒(增加的持续时间不会超过[万剑归宗]的最大持续时间)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_545(char={}, mode=0, text=False, part=''):
    if text:
        return "[万剑归宗]的穿云剑可以在除觉醒技能以外的所有转职技能使用时发动"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_546(char={}, mode=0, text=False, part=''):
    if text:
        return "[万剑归宗]穿云剑发射个数+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_547(char={}, mode=0, text=False, part=''):
    if text:
        return "[冥炎之卡洛]获得冥界的力里，冥炎强化为冥界之炎, 冥界之炎最大重叠数+2"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_548(char={}, mode=0, text=False, part=''):
    if text:
        return "[冰霜之萨亚]、[瘟疫之罗刹]、[死亡墓碑]、[冥祭之沼]、[幽魂之布雷德]的攻击附带冥界之炎"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_549(char={}, mode=0, text=False, part=''):
    if text:
        return "被冥界之炎附着的对象使用特定的技能命中可以即时引爆，冥界之炎爆炸攻击力是冥炎之卡洛冥炎攻击力的500%, - 鬼斩, - 月光斩, - 鬼斩:狂暴, - 鬼影闪, - 鬼斩:炼狱, - 冥炎剑, - 幽鬼降临:式, - 鬼神剑·黄泉摆渡"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_550(char={}, mode=0, text=False, part=''):
    if text:
        return "每附着一个冥界之炎，冥界之炎引爆攻击力+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_551(char={}, mode=0, text=False, part=''):
    if text:
        return "[杀意波动]技能波动领域范围+20%, [邪光波动阵]技能波动攻击范围+25%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_552(char={}, mode=0, text=False, part=''):
    if text:
        return "施放特定技能时吸收雷神之力，使[邪光波动阵]获得强化，施放[邪光波动阵]时可无施放动作使用, - 爆炎波动剑, - 不动冥王阵, - 天雷波动剑"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_553(char={}, mode=0, text=False, part=''):
    if text:
        return "[爆炎波动剑]爆发间隔距离-90%，爆发位置更变，爆发间隔时间-30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_554(char={}, mode=0, text=False, part=''):
    if text:
        return "[爆炎波动剑]第二次爆发大小+45%, [爆炎波动剑]第三次爆发大小+70%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_555(char={}, mode=0, text=False, part=''):
    if text:
        return "剑术系列技能攻击时，[鬼步]冷却时间初始化 (通过[鬼步]发动的剑术系列技能不会触发这个效果)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_556(char={}, mode=0, text=False, part=''):
    if text:
        return "合击系列技能攻击时，[鬼步]冷却时间初始化"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_557(char={}, mode=0, text=False, part=''):
    if text:
        return "[鬼步]攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_558(char={}, mode=0, text=False, part=''):
    if text:
        return "[鬼步]Y轴攻击范围 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_559(char={}, mode=0, text=False, part=''):
    if text:
        return "强化恶即斩，使用誓约之剑:雷沃丁对敌人一刀两断, [恶即斩]攻击力 -15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_560(char={}, mode=0, text=False, part=''):
    if text:
        return "恶即斩总是发动最大蕃力"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_561(char={}, mode=0, text=False, part=''):
    if text:
        return "被恶即斩命中的敌人生成2秒的撕裂伤痕, 使用破军旋舞斩攻击伤痕状态的敌人时，恶疾斩技能冷却时间 -10%(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_562(char={}, mode=0, text=False, part=''):
    if text:
        return "伤痕维持时间+2秒, 使用瞬影三绝斩攻击伤痕状态的敌人时，恶即斩技能冷却时间 -10%(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_563(char={}, mode=0, text=False, part=''):
    if text:
        return "[腹剑:破]更变为最大3次的堆栈型技能, - 不会自动填充, - [蛇腹剑:破]以外的转职技能攻击时填充1次"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_564(char={}, mode=0, text=False, part=''):
    if text:
        return "[蛇腹剑:破]喷发的剑刃数里+3"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_565(char={}, mode=0, text=False, part=''):
    if text:
        return "觉醒技以外的转职技能的收招硬直可以使用[蛇腹剑:破]取消"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_566(char={}, mode=0, text=False, part=''):
    if text:
        return "[蛇腹剑:破]的收招硬直可以使用转职技能取消"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_567(char={}, mode=0, text=False, part=''):
    if text:
        return "[啸空十字斩]自动追击前方的强力敌人"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_568(char={}, mode=0, text=False, part=''):
    if text:
        return "[啸空十字斩]的水平、垂直斩击同时发动，斩击后角色的方向变换"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_569(char={}, mode=0, text=False, part=''):
    if text:
        return "[一花渡江]、[啸空十字斩]、[樱花劫]、[落英惊鸿掌] 技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_570(char={}, mode=0, text=False, part=''):
    if text:
        return "转职技能的收招硬直时间可以柔化使用[啸空十字斩]和[落英惊鸿掌]"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_571(char={}, mode=0, text=False, part=''):
    if text:
        return "[汲魂之力]最大灵魂吸收量+30"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_572(char={}, mode=0, text=False, part=''):
    if text:
        return "[释魂狂怒]攻击成功时额外吸收5个灵魂, [暗影盛宴]爆炸攻击时额外吸收5个灵魂, [暗影绽放:死亡荆棘]爆炸攻击时额外吸收5个灵魂"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_573(char={}, mode=0, text=False, part=''):
    if text:
        return "[释魂飞弹]每消耗2个灵魂就会减少特定技能的1%剩余冷却时间, - 暗影盛宴, - 天罚死光, - 天罚之剑, - 暗影绽放:死亡荆棘"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_574(char={}, mode=0, text=False, part=''):
    if text:
        return "[释魂飞弹]最大追踪距离+20%, [释魂飞弹]每次发射消耗的灵魂数量+2"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_575(char={}, mode=0, text=False, part=''):
    if text:
        return "[鬼缚钉]斩击攻击删除，斩击攻击百分比整合到踢击中"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_576(char={}, mode=0, text=False, part=''):
    if text:
        return "[鬼缚钉]收招硬直可以使用转职技能取消"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_577(char={}, mode=0, text=False, part=''):
    if text:
        return "[回旋十字斩]和除觉醒技外的转职技能的收招硬直，可以使用[鬼缚钉]取消"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_578(char={}, mode=0, text=False, part=''):
    if text:
        return "[收刀术]连击成功时，连击的技能和使用[收刀术]连接的技能，剩余冷却时间-15%(觉醒技除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_579(char={}, mode=0, text=False, part=''):
    if text:
        return "二重解放更变为持续10秒的buff, - 强化1次技能效果删除, - 强化特定技能限制删除, - 强化攻击力效果删除, - 持续时间内，技能攻击力+45%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_580(char={}, mode=0, text=False, part=''):
    if text:
        return "[柔化肌肉]使用时[双重释放]的剩余冷却时间-2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_581(char={}, mode=0, text=False, part=''):
    if text:
        return "[柔化肌肉]强制中断次数+2"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_582(char={}, mode=0, text=False, part=''):
    if text:
        return "[柔化肌肉]强制中断后，下一个技能的伤害增加量+2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_583(char={}, mode=0, text=False, part=''):
    if text:
        return "[念兽·猛虎震地]使用时、删除原有的多段攻击和爆炸攻击、召唤出念兽咆哮后即时爆炸, - 咆哮攻击：统一为[念兽·猛虎震地]的多段攻击次数和多段攻击力, - 爆炸攻击：统一为[念兽·猛虎震地]的爆炸攻击次数和爆炸攻击力"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_584(char={}, mode=0, text=False, part=''):
    if text:
        return "[念兽·猛虎震地]咆哮攻击可以把敌人聚集到前方, [念兽·猛虎震地]攻击范围+20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_585(char={}, mode=0, text=False, part=''):
    if text:
        return "[禅语·形灭]技能使用后可以移动"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_586(char={}, mode=0, text=False, part=''):
    if text:
        return "[禅语·形灭]释放速度+20%、攻击范围+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_587(char={}, mode=0, text=False, part=''):
    if text:
        return "抓取技能攻击失败时、对应的技能减少5秒冷却（这个效果冷却时间10秒）, —无情摔机, —霹雳旋踢, —浮空凌云踢（地上）, —地狱风火轮, —死亡旋律（地上）, —武莲华, —黑震旋风"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_588(char={}, mode=0, text=False, part=''):
    if text:
        return "[地狱风火轮]变更为最大2次的堆栈型技能"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_589(char={}, mode=0, text=False, part=''):
    if text:
        return "[地狱风火轮]终结攻击产生地震, 地震攻击力是终结攻击力的50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_590(char={}, mode=0, text=False, part=''):
    if text:
        return "[地狱风火轮]释放后的僵直时间内可以使用转职技能"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_591(char={}, mode=0, text=False, part=''):
    if text:
        return "[狂·霸王拳]终结攻击删除、改为向下投掷火焰瓶爆弹"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_592(char={}, mode=0, text=False, part=''):
    if text:
        return "[狂·霸王拳]使用时对周边波及到的敌人适用抓取敌人攻击的伤害、抓取失败时发动终结攻击"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_593(char={}, mode=0, text=False, part=''):
    if text:
        return "每个异常状态可以减少[狂·霸王拳]的冷却时间10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_594(char={}, mode=0, text=False, part=''):
    if text:
        return "每个异常状态可以让[狂·霸王拳]的攻击范围增加10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_595(char={}, mode=0, text=False, part=''):
    if text:
        return "[闪电之舞]攻击单一目标时在目标的左右交替移动攻击"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_596(char={}, mode=0, text=False, part=''):
    if text:
        return "[闪电之舞]移动次数 -4, [闪电之舞]攻击速度 +30%, [闪电之舞]攻击力 -15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_597(char={}, mode=0, text=False, part=''):
    if text:
        return "[闪电之舞]攻击时发生冲击波, - 攻击单一目标时不会产生冲击波, - 被直接攻击的对象不会受到冲击波攻击"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_598(char={}, mode=0, text=False, part=''):
    if text:
        return "[闪电之舞]移动范围+5%, [闪电之舞]攻击时，使敌人进入感电状态(冷却时间15秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_599(char={}, mode=0, text=False, part=''):
    if text:
        return "[蓄念炮]蓄力时间删除, [蓄念炮]冷却时间删除"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_600(char={}, mode=0, text=False, part=''):
    if text:
        return "气功师转职时对[念气波]冷却时间减少功能删除, [念气波]冷却时间 +4秒，技能攻击力 +120%，念气波大小 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_601(char={}, mode=0, text=False, part=''):
    if text:
        return "[念气波]技能命中时，[聚能念起炮]技能剩余冷却时间 -5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_602(char={}, mode=0, text=False, part=''):
    if text:
        return "[念气波]使用时，有10%的几率发射念起螺旋, - 念起螺旋攻击能是蓄念炮影响下念气波技能攻击力的500%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_603(char={}, mode=0, text=False, part=''):
    if text:
        return "转职技能使用时获得技术点（最大20点）, - Lv30以下技能：1点, - Lv35-Lv80技能：2点, - 末日风暴、苍宇彗星落、送葬舞步：5点, - 女皇时代·辉煌舞台：10点, - 无情抓取连接/空中使用时额外追加1点"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_604(char={}, mode=0, text=False, part=''):
    if text:
        return "技术点在1以上时,使用连接无情抓取可以减少3秒恢复时间"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_605(char={}, mode=0, text=False, part=''):
    if text:
        return "技术点在6以上时,使用抓取技能失败时,消费3点技术点减少3秒对应技能的冷却时间"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_606(char={}, mode=0, text=False, part=''):
    if text:
        return "技术点在11以上时,使用觉醒技能消耗所有的技术点,觉醒技以外的所有技能剩余冷却时间-30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_607(char={}, mode=0, text=False, part=''):
    if text:
        return "街霸可以赋予敌人异常状态效果的技能,可以通过特定的技能攻击产生暴血效果，马上适用异常状态剩余的伤害, - 擒月炎抓取攻击时生成爆血, - 猛毒擒月炎抓取攻击时生成爆血"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_608(char={}, mode=0, text=False, part=''):
    if text:
        return "触发爆血技能追加, - 伏虎霸王拳终结攻击"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_609(char={}, mode=0, text=False, part=''):
    if text:
        return "每一个异常状态，[擒月炎]、[猛毒擒月炎]攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_610(char={}, mode=0, text=False, part=''):
    if text:
        return "每一个异常状态，[狂·霸王拳]攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_611(char={}, mode=0, text=False, part=''):
    if text:
        return "[激光炮]变更为最大3次的堆栈型技能,被击中的敌人生成电磁场标记, - 充能时间：7秒, - 电磁场标记维持时间：10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_612(char={}, mode=0, text=False, part=''):
    if text:
        return "[激光炮]攻击范围+40%,攻击力+20%, [蓄电激光炮]最大蓄力时间-50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_613(char={}, mode=0, text=False, part=''):
    if text:
        return "[FM-92刺弹炮]使用时如果前方存在电磁场标记的场合下,向目标发射强化高爆弹, - 根据领主/的HP顺序追击"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_614(char={}, mode=0, text=False, part=''):
    if text:
        return "[FM-92刺弹炮]攻击力+15%,爆炸范围+25%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_615(char={}, mode=0, text=False, part=''):
    if text:
        return "使用机械引爆技能引爆以下敌人时,在爆炸中生成R-追击者（R-追击者可以被机械引爆技能引爆产生爆炸对敌人造成伤害,适用的攻击力为机械师本身学习的Rx-78追击者技能攻击力的50%）, 【R-追击者生成技能】, —Rx-78追击者, —Ez-8自爆者, —RX-60陷阱追击者"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_616(char={}, mode=0, text=False, part=''):
    if text:
        return "R-追击者生成技能追加, —空战机械·风暴, —空投支援, —拦截机工厂"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_617(char={}, mode=0, text=False, part=''):
    if text:
        return "R-追击者生成技能追加, —Ez-10反击者, —TX-45特工队"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_618(char={}, mode=0, text=False, part=''):
    if text:
        return "Rx-78追击者攻击力+5%, R-追击者最大生成数+5, R-追击者引爆适用于机械引爆技能的攻击力变换率效果"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_619(char={}, mode=0, text=False, part=''):
    if text:
        return "穿戴时，生成光谱效果；释放[双鹰回旋]时增加30%的攻击速度，持续4秒(最多叠加1次）"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_620(char={}, mode=0, text=False, part=''):
    if text:
        return "第二次投掷手枪至成功接取第二次返回的手枪之间所释放的技能剩余冷却时间减少20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_621(char={}, mode=0, text=False, part=''):
    if text:
        return "[双鹰回旋]的手枪大小+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_622(char={}, mode=0, text=False, part=''):
    if text:
        return "[花式枪术]使用次数+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_623(char={}, mode=0, text=False, part=''):
    if text:
        return "聚合弹强化,使用时向房间内最强的敌人发动狙击请求"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_624(char={}, mode=0, text=False, part=''):
    if text:
        return "超负荷装载状态下适用10次普通攻击可以向聚合弹装填1发特殊弹药, —最大装填数量：3发, —进入地下城时候基本保有装填数量：1发"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_625(char={}, mode=0, text=False, part=''):
    if text:
        return "聚合弹释放时消耗所有超负荷装载的特殊弹药,强化攻击力, —消耗1发特殊弹药：聚合弹攻击力+15%, —消耗2发特殊弹药：聚合弹攻击力+40%, 消耗3发特殊弹药：聚合弹攻击力+80%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_626(char={}, mode=0, text=False, part=''):
    if text:
        return "聚合弹在其他技能释放时可以取消释放动作使用"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_627(char={}, mode=0, text=False, part=''):
    if text:
        return "M-3喷火器释放时将火焰压缩发射"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_628(char={}, mode=0, text=False, part=''):
    if text:
        return "聚焦喷火器释放时将火焰压缩发射"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_629(char={}, mode=0, text=False, part=''):
    if text:
        return "聚焦喷火器变成最大3次的堆栈技能, —每次的攻击力是总攻击力的50%, —每次的补充时间是4秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_630(char={}, mode=0, text=False, part=''):
    if text:
        return "UHT-03爆炎喷火器移动速度比率+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_631(char={}, mode=0, text=False, part=''):
    if text:
        return "[G-1科罗纳]状态下转换成[G-2旋雷者]或[G-3捕食者]时，生成持续8秒的全息G-1科罗纳, - 全息G-1科罗纳攻击力：[G-1科罗纳]的50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_632(char={}, mode=0, text=False, part=''):
    if text:
        return "全息G-1科罗纳生成的状态下使用[G-磁力弹]时，会让全息G-1科罗纳代替发射"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_633(char={}, mode=0, text=False, part=''):
    if text:
        return "[G-3捕食者]发射强化型激光，攻击力+5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_634(char={}, mode=0, text=False, part=''):
    if text:
        return "[G-S.P. 猎鹰]技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_635(char={}, mode=0, text=False, part=''):
    if text:
        return "[移动射击]技能左轮枪发射数+50%, [移动射击]攻击力 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_636(char={}, mode=0, text=False, part=''):
    if text:
        return "[移动射击技能的攻击范围+10%, [移动射击攻击速度+30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_637(char={}, mode=0, text=False, part=''):
    if text:
        return "[移动射击技能使用时就开始计算冷却时间, [移动射击]技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_638(char={}, mode=0, text=False, part=''):
    if text:
        return "[移动射击使用时进入地下城的下一个房间会维持移动射击的射击状态, [移动射击技能的移动速度增加比率+30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_639(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃状态下使用G-14手雷、G-35L感电手雷、G-18C冰冻手雷不会消耗单兵推进器的次数"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_640(char={}, mode=0, text=False, part=''):
    if text:
        return "G-14手雷、G-35L感电手雷、G-18C冰冻手雷最大装载数+2"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_641(char={}, mode=0, text=False, part=''):
    if text:
        return "G-96热压手雷技能使用时,消耗保有的有所手雷强化G-96热压手雷, —消耗1个手雷可使得G-96热压手雷攻击力+2%（最大30%）, —可消耗的技能：G-14手雷、G-35L感电手雷、G-18C冰冻手雷"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_642(char={}, mode=0, text=False, part=''):
    if text:
        return "空袭战略使用时G-96热压手雷适用最大强化效果"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_643(char={}, mode=0, text=False, part=''):
    if text:
        return "[冰之技艺]生成的冰枪向着所有被击中的敌人发射, [冰之技艺]冰枪爆炸功能删除"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_644(char={}, mode=0, text=False, part=''):
    if text:
        return "[冰之技艺]冰枪击中的敌人时，有10%几率使敌人进入冰东状态，持续2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_645(char={}, mode=0, text=False, part=''):
    if text:
        return "[冰之技艺]的冰枪攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_646(char={}, mode=0, text=False, part=''):
    if text:
        return "[冰舞乱击]追踪前方500px范围内最强的敌人进行攻击，攻击会波及到附近的敌人"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_647(char={}, mode=0, text=False, part=''):
    if text:
        return "[元素炮]使用时，变更为前方生成深渊之球爆发攻击, [元素炮]属性变化魔法球攻击力增加率 +50%，冷却时间 +5秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_648(char={}, mode=0, text=False, part=''):
    if text:
        return "其他技能释放时可以使用[元素炮]取消"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_649(char={}, mode=0, text=False, part=''):
    if text:
        return "每层元素之力可以使[元素炮]的攻击力增加+10%，太小+5%, [元素炮]施放时，每消耗一层元素之力，所有技能冷却时间恢复速度 +6%，效果持续5秒(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_650(char={}, mode=0, text=False, part=''):
    if text:
        return "[聚能魔炮]、[聚能轰击]施放时，可以初始化[元素炮]的技能冷却时间"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_651(char={}, mode=0, text=False, part=''):
    if text:
        return "[狂风冲刺]更变为最大施放3次的堆栈型技能"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_652(char={}, mode=0, text=False, part=''):
    if text:
        return "[狂风冲刺]使用时生成游离之风追击敌人, - 游离之风攻击力为逐风者自身习得的[游离之风]攻击力的50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_653(char={}, mode=0, text=False, part=''):
    if text:
        return "使用[狂风冲刺]、[朔风牵引]、[刃风]取消专职技能时，可以获得1层风魂(最多15层), 风魂累积到15层时，使用[风暴之拳]可以消耗所有层数，攻击力 +50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_654(char={}, mode=0, text=False, part=''):
    if text:
        return "[游离之风]大小+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_655(char={}, mode=0, text=False, part=''):
    if text:
        return "[狱血之噬]施放速度+30%，冷却时间-10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_656(char={}, mode=0, text=False, part=''):
    if text:
        return "[狱血之噬]使用时获得2个血源之眼(最大5个), 进入地下城时获得1个血源之眼"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_657(char={}, mode=0, text=False, part=''):
    if text:
        return "[血腥狩猎]施放时消耗1个血源之眼强化为死亡狩猎, - 攻击力+50%, - 攻击500px范围内所有敌人, - 更变为单段攻击技能"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_658(char={}, mode=0, text=False, part=''):
    if text:
        return "[血腥炼狱]施放时消耗1个血源之眼强化为死亡炼狱, - 攻击力+50%, - 施放后可以移动"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_659(char={}, mode=0, text=False, part=''):
    if text:
        return "[次元:粒子风暴]适用[次元边界]效果时，在自身周围生成多个粒子风暴"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_660(char={}, mode=0, text=False, part=''):
    if text:
        return "[次元:粒子风暴]攻击范围+25%，爆炸速度+50%，攻击力+15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_661(char={}, mode=0, text=False, part=''):
    if text:
        return "[古史记忆]强化，施放奈雅丽系列技能时，生成分身代替施放(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_662(char={}, mode=0, text=False, part=''):
    if text:
        return "[乖离 : 魅魔之舞]、[乖离 : 异界蜂群]、[乖离 : 禁锢]、[乖离 : 沉沦]技能冷却时间 -10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_663(char={}, mode=0, text=False, part=''):
    if text:
        return "超级棒棒糖每个生成的糖果人偶可以使超级棒棒糖技能冷却时间-3%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_664(char={}, mode=0, text=False, part=''):
    if text:
        return "可以吸收没有爆炸的糖果人偶（最大15个）, —超级棒棒糖使用时,追加生成和吸收数量相等的糖果人偶, —追加生成的糖果人偶不会即时吸收,不会算进超级棒棒糖最大的糖果人偶数量中"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_665(char={}, mode=0, text=False, part=''):
    if text:
        return "每个被超级棒棒糖击中的敌人生成的糖果人偶个数+2, 糖果人偶攻击力-20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_666(char={}, mode=0, text=False, part=''):
    if text:
        return "超级棒棒糖最大糖果人偶生成个数+5"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_667(char={}, mode=0, text=False, part=''):
    if text:
        return "达成5次以上连击时，自动发动炫纹发射"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_668(char={}, mode=0, text=False, part=''):
    if text:
        return "发射炫纹数量+2, 炫纹攻击力 +10%, 炫纹发射MP消耗量 -70%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_669(char={}, mode=0, text=False, part=''):
    if text:
        return "尼巫的战术最后一击、天击、龙牙、落花掌、圆舞棍每次使用时生成的炫纹数量+4, 自动炫纹每次生成的炫纹个数+4"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_670(char={}, mode=0, text=False, part=''):
    if text:
        return "超大炫纹大小比率+20%, 炫纹最大生成个数+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_671(char={}, mode=0, text=False, part=''):
    if text:
        return "【装备属性操作键】输入时生成持续60秒的可以保存技能的元素结晶, —使用高级元素技能可以将技能保存在结晶中（最大一次）, —输入【装备属性操作键】可以释放出元素结晶保有的技能<br—高级元素结晶技能：杰克降临、极冰盛宴、天雷、湮灭黑洞, 再次生成元素结晶的冷却时间是0.5秒, - 保有的技能冷却时间为原先的15%, - 元素水晶激活的技能攻击力为原先的15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_672(char={}, mode=0, text=False, part=''):
    if text:
        return "追加可储存技能, - 元素之幕、元素震荡、圣灵水晶"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_673(char={}, mode=0, text=False, part=''):
    if text:
        return "元素结晶保存的技能维持最大蓄力状态"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_674(char={}, mode=0, text=False, part=''):
    if text:
        return "[魔法记忆]技能的施放速度提升率 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_675(char={}, mode=0, text=False, part=''):
    if text:
        return "精灵召唤：亡魂默克尔暗黑雾攻击力+20%，追加控制功能, 精灵召唤：极光格雷林闪电攻击力+20%，追加聚集敌人功能"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_676(char={}, mode=0, text=False, part=''):
    if text:
        return "精灵召唤：冰景阿奎利斯冰导弹攻击力+20%，范围+15%, 精灵召唤：火焰赫瑞克火焰剑攻击力+20%，追加聚集敌人功能"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_677(char={}, mode=0, text=False, part=''):
    if text:
        return "精灵召唤：精灵王伊伽贝拉的激光攻击更变为向地面发射大量激光，攻击力+20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_678(char={}, mode=0, text=False, part=''):
    if text:
        return "蚀月附灵技能追加操作使用时删除释放动作"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_679(char={}, mode=0, text=False, part=''):
    if text:
        return "[哇咔咔!]不需要释放动作就可以使用"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_680(char={}, mode=0, text=False, part=''):
    if text:
        return "[咆哮吧!疯疯熊]技能的诅咒气息更变为爆发喷射攻击, - 攻击力是[咆哮吧!疯疯熊]诅咒气息魔法攻击力总和的50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_681(char={}, mode=0, text=False, part=''):
    if text:
        return "装备时，[禁忌诅咒]对队友提升效果+8%(解除装备后[禁忌诅咒]失效；Buff登记系统不适用该效果), [细心缝补]HP恢复量 -50%, [爱之急救]HP回复量 -50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_682(char={}, mode=0, text=False, part=''):
    if text:
        return "[细心缝补]技能buff适用范围+20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_683(char={}, mode=0, text=False, part=''):
    if text:
        return "[正义审判]更变为召唤光束，向范围内的敌人发射正义之枪, - 最大锁定敌人数：10, - 正义之枪最大发射个数:10, - 正义之枪攻击力为光刃攻击力的1600%, - 正义之枪爆炸攻击力为魔法阵最大展开后100%的终结攻击力"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_684(char={}, mode=0, text=False, part=''):
    if text:
        return "使用技能时可以柔化施放[正义审判]"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_685(char={}, mode=0, text=False, part=''):
    if text:
        return "装备时，[荣誉祝福]对队友提升效果+8%(解除装备后[荣誉祝福]失效；Buff登记系统不适用该效果), [缓慢愈合]HP恢复量 -50%, [圣愈之风]HP恢复量 -50%, [圣佑结界]HP恢复量 -50%, [圣光突袭]突进距离 -70%, [圣光突袭]攻击力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_686(char={}, mode=0, text=False, part=''):
    if text:
        return "[圣光沁盾]不再移动, [圣光沁盾]HP增加5倍, [缓慢愈合]队友选择范围+20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_687(char={}, mode=0, text=False, part=''):
    if text:
        return "前冲时可以使用[无双击], [无双击]技能可以聚集霸体护甲敌人, 式神白虎技能球体大小 +50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_688(char={}, mode=0, text=False, part=''):
    if text:
        return "[脉轮：圣光]使用后，[无双击]技能攻击力+20%, 无双技范围+20%, 落雷符攻击力 +20%, 落雷符范围 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_689(char={}, mode=0, text=False, part=''):
    if text:
        return "[狂乱锤击]最后一击删除，每次打击都生成冲击波, - 最后一击攻击力合算到技能总攻击力中"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_690(char={}, mode=0, text=False, part=''):
    if text:
        return "[狂乱锤击]攻击次数+100%, [狂乱锤击]技能冷却时间 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_691(char={}, mode=0, text=False, part=''):
    if text:
        return "正义执行:雷米迪奥斯的圣座的觉醒替代技能选择为泯灭神击时，制裁∶怒火疾风技能更变为最大使用次数3次的堆栈型技能,对600px范围内的敌人进行追击, - 连打攻击力 +100%，连打次数 -9, - 删除终结攻击最后的爆发, - 每40秒充能—次使用次数, - 追击r较多的领主/精英敌人, - MP消耗量 -30%, - 无色小晶块消耗量 -5个"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_692(char={}, mode=0, text=False, part=''):
    if text:
        return "[制裁∶怒火疾风]追击范围+30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_693(char={}, mode=0, text=False, part=''):
    if text:
        return "正义执行:雷米迪奥斯的圣座的觉醒替代技能选择为泯灭神击时，适用以下效果, - 转职后技能可以柔化使用[制裁∶怒火疾风], - 转职后技能柔化使用[制裁∶怒火疾风]时不消耗干涸之泉层数"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_694(char={}, mode=0, text=False, part=''):
    if text:
        return "正义执行:雷米迪奥斯的圣座的觉醒替代技能选择为泯灭神击时，适用以下效果, - 刺拳猛击技能使用时，制裁 : 怒火疾风剩余冷却时间 -12%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_695(char={}, mode=0, text=False, part=''):
    if text:
        return "魔化状态下，恶魔能量在30以上时，每使用一次消耗恶魔能量的技能都会追加消耗40恶魔能量发动恶魔之爪(觉醒技能除外), - 恶魔之爪攻击力是恶魔之力攻击力的1000%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_696(char={}, mode=0, text=False, part=''):
    if text:
        return "魔化普通攻击和技能的恶魔能量恢复量+10%, [恶魔之爪]的攻击力比率追加增加500%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_697(char={}, mode=0, text=False, part=''):
    if text:
        return "化魔恶魔能量恢复量+10%, [恶魔之爪]的攻击力比率追加增加500%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_698(char={}, mode=0, text=False, part=''):
    if text:
        return "魔化攻击速度增加量+20%，移动速度增加量+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_699(char={}, mode=0, text=False, part=''):
    if text:
        return "[圣洁之光]击中敌人不会爆炸，移动300px后产生爆炸, [圣洁之光]攻击力+100%，大小+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_700(char={}, mode=0, text=False, part=''):
    if text:
        return "[圣洁之光]攻击可以使得[神光十字]和[忏悔重击]的剩余冷却时间-2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_701(char={}, mode=0, text=False, part=''):
    if text:
        return "装备时，[勇气祝福]对队友提升效果+8%(解除装备后[勇气祝福]失效；Buff登记系统不适用该效果), [治愈祈祷]HP恢复量 -50%, [新生圣歌]HP恢复量 -50%, [圣光普照]HP恢复量 -50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_702(char={}, mode=0, text=False, part=''):
    if text:
        return "[治愈祈祷]的队员选择范围+20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_703(char={}, mode=0, text=False, part=''):
    if text:
        return "诱魔之手罪业增加量+2, [原罪释放·净化]状态下，使用诱魔之手攻击敌人时，增加12秒持续时间(无法超过[原罪释放·净化]的持续时间上限)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_704(char={}, mode=0, text=False, part=''):
    if text:
        return "[七宗罪]消耗罪业层数增加罪业加身的控制时间的机能删除, [七宗罪]技能的罪业加身控制时间加成+1秒, 罪业层数在3以上时，使用罪业加身技能消耗3层罪业层数，10秒内所受伤害-15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_705(char={}, mode=0, text=False, part=''):
    if text:
        return "[暴食之噬]技能更变为以自身为中心吸收后爆发的技能, [暴食之噬]攻击力+30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_706(char={}, mode=0, text=False, part=''):
    if text:
        return "罪业层数在3以上时，施放暴食之噬消耗3层罪业层数，使用分身施放技能"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_707(char={}, mode=0, text=False, part=''):
    if text:
        return "火焰精华更变为使用次数5次的堆栈技能, - 充能时间: 8秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_708(char={}, mode=0, text=False, part=''):
    if text:
        return "每触发焚烧状态一次，火焰精华的剩余充能时间-1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_709(char={}, mode=0, text=False, part=''):
    if text:
        return "[净化之焰]攻击力 -20%, [净化之焰]施放时，有50%的几率初始化该技能的冷却时间, 10秒内再次施放初始化的[净化之焰]时，初始化概率 -10%(最多降低到10%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_710(char={}, mode=0, text=False, part=''):
    if text:
        return "[净化之焰]爆发范围+30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_711(char={}, mode=0, text=False, part=''):
    if text:
        return "[念珠连射]、[木槵子经]攻击时获得1个神力之珠(最大20个), 特定技能使用时消耗神力之珠获得强化, - 不动珠箔阵: 念珠回转次数+1，消耗8个神力之珠"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_712(char={}, mode=0, text=False, part=''):
    if text:
        return "追加可以消耗神力之珠获得强化的技能, - 百八念珠: 念珠射出个数+10，消耗10个神力之珠, - 退魔阴阳符: 弹击次数+3，消耗10个神力之珠"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_713(char={}, mode=0, text=False, part=''):
    if text:
        return "追加可以消耗神力之珠获得强化的技能, - 天坠阴阳玉: 念珠落下数+1，消耗15个神力之珠, 神力之珠最大保有数+5"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_714(char={}, mode=0, text=False, part=''):
    if text:
        return "每射出一次念珠连射的念珠，百八念珠、不动珠箔阵技能冷却时间恢复速度+1%, 每使用一次木槵子经，百八念珠、不动珠箔阵技能冷却时间恢复速度+1%, (冷却时间中念珠连射，木槵子经的关联效果初始化)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_715(char={}, mode=0, text=False, part=''):
    if text:
        return "降临:僵尸莱迪娅更变为最大使用3次的堆栈技能, - 每次攻击力：总攻击力的45%, - 补充时间：15秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_716(char={}, mode=0, text=False, part=''):
    if text:
        return "降临:僵尸莱迪娅的追加操作删除，召唤莱迪娅后直接自爆"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_717(char={}, mode=0, text=False, part=''):
    if text:
        return "被莱迪娅攻击的敌人生成持续5秒的恐怖烙印"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_718(char={}, mode=0, text=False, part=''):
    if text:
        return "使用特定技能攻击拥有恐怖烙印的敌人减少对应技能10的剩余冷却时间, [特定技能], - 暗黑蛛丝引, - 暴君极刑斩, - 死灵之缚"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_719(char={}, mode=0, text=False, part=''):
    if text:
        return "剑刃风暴每次攻击获得的终结点 +100%, 位移速度 +30%，吸附能力 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_720(char={}, mode=0, text=False, part=''):
    if text:
        return "剑刃风暴变成最大3次的堆栈技能"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_721(char={}, mode=0, text=False, part=''):
    if text:
        return "剑刃风暴技能使用中施放终结追击时，剑刃风暴剩余的打击攻击为会整合到终结追击中，向最强的敌人发射首"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_722(char={}, mode=0, text=False, part=''):
    if text:
        return "死亡风暴发射的匕首变得可以贯穿敌人, 死亡风暴发射的匕首数-10"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_723(char={}, mode=0, text=False, part=''):
    if text:
        return "忍法 : 残影术技能每消耗1个残影，六道轮回再生的残影攻击力比率追加增加1.5%(最多叠加12次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_724(char={}, mode=0, text=False, part=''):
    if text:
        return "忍法:六道轮回技能释放完毕后恢复5个残影"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_725(char={}, mode=0, text=False, part=''):
    if text:
        return "忍法:六道轮回技能释放时获得5秒霸体护甲"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_726(char={}, mode=0, text=False, part=''):
    if text:
        return "维持装备赋予的霸体护甲状态时，技能冷却时间恢复速度+50%(最大重叠1次,觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_727(char={}, mode=0, text=False, part=''):
    if text:
        return "背击时获得2影之碎片(最大50), 正面攻击减少3影之碎片"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_728(char={}, mode=0, text=False, part=''):
    if text:
        return "剜心背击成功时消耗影之碎片,每消耗1的影之碎片强化1%的剜心攻击力(最大50%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_729(char={}, mode=0, text=False, part=''):
    if text:
        return "刺心使用后15秒内进入伪装状态"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_730(char={}, mode=0, text=False, part=''):
    if text:
        return "维持这个装备的伪装状态时，技能冷却时间恢复速度+12%(最大重叠1次,觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_731(char={}, mode=0, text=False, part=''):
    if text:
        return "碎灵屠戮使用时，亚丁的化身召唤恶魔们的幻影进行爆炸攻击"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_732(char={}, mode=0, text=False, part=''):
    if text:
        return "没有恶魔时使用碎灵屠戮,马上召唤所有的恶魔"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_733(char={}, mode=0, text=False, part=''):
    if text:
        return "碎灵屠戮使用时可以使用午夜嘉年华"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_734(char={}, mode=0, text=False, part=''):
    if text:
        return "碎灵屠戮攻击力+10%，范围+20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_735(char={}, mode=0, text=False, part=''):
    if text:
        return "神光冲击消耗天使光翼时控制敌人2秒, 神光冲击消耗天使光翼最大数量是2个(只要消耗天使光翼就适用6阶段的效果), 神光冲击攻击范围比率 +20%, 天使光翼聚集效果范围 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_736(char={}, mode=0, text=False, part=''):
    if text:
        return "神光冲击攻击成功时获得的天使光翼数量+2, 天使光翼的挑衅效果作用于敌人时，帕拉丁维持防御状态的情况下天使光翼获得时间间隔 -50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_737(char={}, mode=0, text=False, part=''):
    if text:
        return "神罚之锤技能消耗天使光翼使用时使敌人进入眩晕状态"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_738(char={}, mode=0, text=False, part=''):
    if text:
        return "神罚之锤技能消耗天使光翼使用时适用以下效果, - 每消耗1天使光翼，神罚之锤技能攻击力+4%, - 每消耗1天使光翼，范围+3%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_739(char={}, mode=0, text=False, part=''):
    if text:
        return "龙刃无双更变为最大使用两次的堆栈型技能, - 攻击力 -40%, - 充能时间10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_740(char={}, mode=0, text=False, part=''):
    if text:
        return "龙刃无双技能使用中使用阿斯特拉系列技能可以使龙刃无双剩余的冷却时间 -10%, - 每次龙刃无双只会适用1次冷却缩减效果"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_741(char={}, mode=0, text=False, part=''):
    if text:
        return "龙刃无双使用时10秒内技能攻击力5%(最天重叠1次,觉醒技除外）"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_742(char={}, mode=0, text=False, part=''):
    if text:
        return "火焰吐息、龙语召唤:阿斯特拉、龙之撕咬、魔龙之息、魔龙天翔冷却时间-10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_743(char={}, mode=0, text=False, part=''):
    if text:
        return "剑盾猛攻6阶段状态下使用剑盾强袭进入8秒狂热时间中，狂热时间中连锁槽所有区域都被视为成功区域​"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_744(char={}, mode=0, text=False, part=''):
    if text:
        return "狂热时间时剑盾猛攻攻击力+500%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_745(char={}, mode=0, text=False, part=''):
    if text:
        return "狂热时间时Lv1-30的技能冷却时间-70%、攻击力-50%(不包括剑盾猛攻)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_746(char={}, mode=0, text=False, part=''):
    if text:
        return "剑盾猛攻使用时Lv1-30的技能剩余冷却时间-10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_747(char={}, mode=0, text=False, part=''):
    if text:
        return "每个被暗蚀的敌人每秒产生10%的黑雷气息，没有被暗蚀的敌人时每秒减少5%的黑雷气息, 攻击领主怪物时，获得1%的黑雷气息, 黑雷气息达到100%后生成持续5秒的强化黑雷buff"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_748(char={}, mode=0, text=False, part=''):
    if text:
        return "强化黑雷buff维持时间+10秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_749(char={}, mode=0, text=False, part=''):
    if text:
        return "强化黑雷buff状态下，坠蚀之雨的黑雷之枪会同时坠落"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_750(char={}, mode=0, text=False, part=''):
    if text:
        return "强化黑雷buff状态下，使用坠蚀之雨时追加落下—把巨式黑雷魔枪, 黑雷魔枪攻击为坠蚀之雨多段攻击力的1000%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_751(char={}, mode=0, text=False, part=''):
    if text:
        return "使用猎杀枪技能累计狩猎层数,根据累计的层数来提升狩猎阶段, - 猎杀枪：3层, - 猎杀枪·掠食：10层, - 猎杀枪·穿心：每次打击4层, 累计层数对应阶段, - 1-19层：1阶段, - 20-39层：2阶段, - 40层以上：3阶段, 根据适用的阶段数提升光焰枪的攻击力, - 1阶段：10%攻击力, - 2阶段：20%攻击力, - 3阶段：30%攻击力"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_752(char={}, mode=0, text=False, part=''):
    if text:
        return "狩猎阶段影响攻击力增加的技能追加地龙狩、无尽杀戮"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_753(char={}, mode=0, text=False, part=''):
    if text:
        return "猎杀枪再生成时间-30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_754(char={}, mode=0, text=False, part=''):
    if text:
        return "猎杀枪再发射冷却时间-30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_755(char={}, mode=0, text=False, part=''):
    if text:
        return "灭天之魂技能效果战戟猛攻适用时，额外增加0.3秒的恢复减少时间"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_756(char={}, mode=0, text=False, part=''):
    if text:
        return "被战戟猛攻取消的技能冷却时间-20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_757(char={}, mode=0, text=False, part=''):
    if text:
        return "战戟猛攻堆栈次数+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_758(char={}, mode=0, text=False, part=''):
    if text:
        return "战戟之魂技能效果战戟猛攻buff攻击速度增加量+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_759(char={}, mode=0, text=False, part=''):
    if text:
        return "特定技能攻击时获得极限点穴层数(最多30层，使用行云诀攻击时不获得), - 双龙流云灭: 10层, - 无双突刺: 5层, - 无畏波动枪: 4层, - 双重刺击: 2层, - 刺击: 1层, 夺命雷霆枪攻击速度 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_760(char={}, mode=0, text=False, part=''):
    if text:
        return "每拥有1层极限点穴层数，夺命雷霆枪的冷却时间恢复速度+1%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_761(char={}, mode=0, text=False, part=''):
    if text:
        return "夺命雷霆枪攻击时，消耗所有极限点穴层数，每层极限点穴层数都会适用于积累的创伤效果数量"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_762(char={}, mode=0, text=False, part=''):
    if text:
        return "每拥有1层极限点穴层数，攻击速度+1%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_763(char={}, mode=0, text=False, part=''):
    if text:
        return "对带[暗杀标记]的敌人使用[精准射击]、[锁定射击] 技能攻击时，使敌人获得枪伤状态，持续15秒(最多叠加3次), [精准射击]、[锁定射击] 技能冷却时间-15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_764(char={}, mode=0, text=False, part=''):
    if text:
        return "对带[暗杀标记]的敌人使用[双弦斩]、[月影秘步] 技能攻击时，使敌人获得切伤状态，持续15秒(最多叠加3次) , [双弦斩]、[月影秘步] 技能冷却时间-15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_765(char={}, mode=0, text=False, part=''):
    if text:
        return "使用[月相轮舞] 对枪伤敌人攻击时，每层枪伤重叠次数增加 [月相轮舞] 攻击力8% , -效果生效后，枪伤状态解除 , 使用 [毁灭狂欢] 技能对切伤敌人攻击时，每层切伤重叠次数增加, [毁灭狂欢] 攻击力8% , -效果生效后，切伤状态解除 "
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_766(char={}, mode=0, text=False, part=''):
    if text:
        return "使用 [月光镇魂曲] 对切伤、枪伤状态敌人攻击时，每层枪伤或切伤重叠次数增加 [月光镇魂曲] 攻击力8% , -效果生效后，切伤、枪伤状态解除 , [月相轮舞] 大小+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_767(char={}, mode=0, text=False, part=''):
    if text:
        return "爆裂斩即使没有击中敌人也会产生爆炸，爆裂斩追加攻击键位输入时间+3秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_768(char={}, mode=0, text=False, part=''):
    if text:
        return "爆裂斩收招硬直的时候可以取消使用转职技能, 其他转职技能可以取消收招硬直使用爆裂斩, 爆裂斩技能结束后开始计算冷却时间(追加攻击键位输入时间经过后也会开始计算冷却时间)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_769(char={}, mode=0, text=False, part=''):
    if text:
        return "爆裂斩释放时3秒内转职技能攻击力 +20%(觉醒技除外), 爆裂斩爆炸范围 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_770(char={}, mode=0, text=False, part=''):
    if text:
        return "爆裂斩冷却时间 -35%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_771(char={}, mode=0, text=False, part=''):
    if text:
        return "消耗源能提炼发动CEAB-2时，发动已充能60%多段攻击次数的状态"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_772(char={}, mode=0, text=False, part=''):
    if text:
        return "消耗源能提炼发动CEAB-2时，CEAB-2最大蓄力攻击力 +40%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_773(char={}, mode=0, text=False, part=''):
    if text:
        return "源能提炼次数 +2"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_774(char={}, mode=0, text=False, part=''):
    if text:
        return "消耗源能提炼发动技能时，追加消耗1次源能提炼次数，5秒内觉醒技除外所有技能冷却时间 -20%(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_775(char={}, mode=0, text=False, part=''):
    if text:
        return "转职技能的收招硬直可以使用轮盘连射取消"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_776(char={}, mode=0, text=False, part=''):
    if text:
        return "每取消一次转职后技能，8秒内攻击速度 +7%(最多叠加3次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_777(char={}, mode=0, text=False, part=''):
    if text:
        return "取消转职技能使用轮盘连射时，轮盘连射冷却时间 -50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_778(char={}, mode=0, text=False, part=''):
    if text:
        return "取消转职技能使用轮盘连射时，被取消的对应转职技能冷却时间-20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_779(char={}, mode=0, text=False, part=''):
    if text:
        return "时间停滞最大连击阶段+1, - 6阶段连击攻击力比率: 220"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_780(char={}, mode=0, text=False, part=''):
    if text:
        return "发动[时空主宰]效果施放其他连击技能栏技能时，可以累积时间停滞的能量"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_781(char={}, mode=0, text=False, part=''):
    if text:
        return "[时空主宰]效果适用时，施放扩充技能栏技能时，不会中断目前的连击技能栏技能"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_782(char={}, mode=0, text=False, part=''):
    if text:
        return "[时空主宰]效果持续时间+2秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_783(char={}, mode=0, text=False, part=''):
    if text:
        return "末日虫洞更变为生成时间隔离领域禁锢内部泊的敌人,持续5秒，时间隔离领域持续时间结束时，时间隔离领域崩坏产生爆炸, - 爆炸攻击力是末日虫洞的100%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_784(char={}, mode=0, text=False, part=''):
    if text:
        return "时间隔离领域持续时间内再次输入技能键可以即时引爆"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_785(char={}, mode=0, text=False, part=''):
    if text:
        return "时间隔离领域内部拥有终末之时计表,使用烈炎、寒水、风暴系列技能可以攻击终末之时计表，每2次攻击增加5%的爆炸攻击力和各系列技能的剩余能量条(最大重叠到50%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_786(char={}, mode=0, text=False, part=''):
    if text:
        return "风暴吸引范围 +30%，消耗量 -35%, 装备时，风暴能量条从0开始恢复(复活和进入地下城时除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_787(char={}, mode=0, text=False, part=''):
    if text:
        return "使用超频技能取消转职技能时获得1层电力(最大5层）"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_788(char={}, mode=0, text=False, part=''):
    if text:
        return "[炎神攻城炮]技能施放时，消耗所有电力强化攻击力, - 每层电力强化10%攻击力"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_789(char={}, mode=0, text=False, part=''):
    if text:
        return "[超频:电流闪踢]击中的敌人时，可以控制敌人1.5秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_790(char={}, mode=0, text=False, part=''):
    if text:
        return "[超频:电流闪踢]技能使用时消耗所有电力强化效果, - 每层电力强化10%攻击力, - 每层电力延长0.5秒控制时间"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_791(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv1-100技能攻击力+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_792(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv1-100技能Lv+1(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_793(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备操作键]输入后300秒内，施放无色技能时，消耗白色小晶块代替无色小晶块(冷却时间10秒), 消耗白色小晶块进行攻击时，使敌人进入感电状态(冷却时间15秒), 攻击感电状态敌人时，技能攻击力 +2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_794(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备操作键]输入后300秒内，施放无色技能时，消耗黑色小晶块代替无色小晶块(冷却时间10秒), 消耗黑色小晶块进行攻击时，使敌人进入失明状态(冷却时间25秒), 攻击失明状态敌人时，技能攻击力 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_795(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备操作键]输入后300秒内，施放无色技能时，消耗红色小晶块代替无色小晶块(冷却时间10秒), 消耗红色小晶块进行攻击时，使敌人进入灼烧状态(冷却时间10秒), 攻击灼烧状态敌人时，技能攻击力 +2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_796(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备操作键]输入后300秒内，施放无色技能时，消耗金色小晶块代替无色小晶块(冷却时间10秒), 消耗金色小晶块进行攻击时，使使敌人进入眩晕状态(冷却时间20秒), 攻击眩晕状态敌人时，技能攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_797(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备操作键]输入后300秒内，施放无色技能时，消耗蓝色小晶块代替无色小晶块(冷却时间10秒), 消耗蓝色小晶块进行攻击时，使使敌人进入冰冻状态(冷却时间25秒), 攻击冰冻状态敌人时，技能攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_798(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备操作键]输入时，地图所有道具移动至角色脚下(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_799(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备操作键]输入时，武器属性按火、冰、光、暗的顺序变更, 当该装备赋予属性时，对应属性强化 -10，对应属性抗性 -10"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_800(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备操作键]输入时，消耗15%的HP，5秒内召唤神圣盾牌(冷却时间45秒，词条不会使HP减少至1%以下), - 神圣盾牌的HP以自身HP最大值30%为准, - 神圣盾牌存在于地图上时，物理、魔法防御力 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_801(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备操作键]输入时，选择1名队友带到自己位置(冷却时间50秒，队友无敌时无法选择), 带到自己位置的队友获得20秒移速+20%的Buff"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_802(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备属性操作键]输入时，召唤稻草人，周围500px范围内敌人进入诅咒(持续30秒，冷却时间30秒), 自身处于受诅咒的稻草人范围内时，技能冷却时间恢复速度 +20%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_803(char={}, mode=0, text=False, part=''):
    if text:
        return "[装备属性操作键]输入时，召唤异空间(持续2秒，冷却时间60秒), - 异空间周围按跳跃键，可进入异空间, - 异空间只能发动者进入, - 异空间内部无敌, - 异空间结束时，10秒内，所有速度 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_804(char={}, mode=0, text=False, part=''):
    if text:
        return "150px内存在敌人时，每秒增加2%的技能攻击力(最多叠加5次，150px内没有敌人时，每秒减少1次叠加次数)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_805(char={}, mode=0, text=False, part=''):
    if text:
        return "150px内有敌人时，所有速度 +10%，效果持续10秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_806(char={}, mode=0, text=False, part=''):
    if text:
        return "450px范围内每存在1名处于出血状态的敌人，技能、消耗品、装备的HP恢复效果 +5%(最多增加50%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_807(char={}, mode=0, text=False, part=''):
    if text:
        return "450px范围内每存在1名处于出血状态的敌人，技能冷却时间恢复速度 +10%(最多增加30%，觉醒技能除外), 攻击出血状态敌人时，技能攻击力 +2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_808(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内存在出血状态的敌人时，出血抗性 +20%, 攻击出血状态敌人时，技能攻击力 +2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_809(char={}, mode=0, text=False, part=''):
    if text:
        return "500px范围内每存在1名处于灼烧状态的敌人，所有速度 +3%、火属性抗性 +1(最多叠加10次), 绿名怪、领主进入灼烧状态时，所有速度、火属性抗性增加适用为最大叠加"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_810(char={}, mode=0, text=False, part=''):
    if text:
        return "5秒没有攻击时，所受伤害 -50%(最多叠加1次，攻击与施放技能时取消Buff), 被破招攻击时所受伤害 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_811(char={}, mode=0, text=False, part=''):
    if text:
        return "HP MAX +10%, 所有异常状态抗性 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_812(char={}, mode=0, text=False, part=''):
    if text:
        return "HP MAX +1500, MP MAX -200"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_813(char={}, mode=0, text=False, part=''):
    if text:
        return "HP MAX +4196, 每20000点剩余的MP，伤害增加 267(最多叠加10次), 剩余MP在60%以下时，技能攻击力 -4%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_814(char={}, mode=0, text=False, part=''):
    if text:
        return "HP为0时，5秒内，进入狂暴化，不会死亡, - 狂暴化状态下，被击时伤害无效化, - 狂暴化状态下，伤害增加 4466, - 施放技能时，每消耗1个无色，狂暴化持续时间+0.1秒(增加的持续时间不超过5秒), - 角色在狂暴状态结束时死亡"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_815(char={}, mode=0, text=False, part=''):
    if text:
        return "HP为0时，5秒内适用不死Buff(冷却时间300秒), - 恢复10%的HP, - 所有HP恢复效果无效, - 被击时伤害无效, - 不死Buff结束后，HP MAX -30%(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_816(char={}, mode=0, text=False, part=''):
    if text:
        return "HP为0时，获得英雄气魄Buff, 所有HP恢复效果无效, 被击时，代替HP消耗MP，MP为0时死亡, 英雄气魄Buff期间，每秒减少2%的MP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_817(char={}, mode=0, text=False, part=''):
    if text:
        return "HP为0时，自身进入睡眠状态(冷却时间300秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_818(char={}, mode=0, text=False, part=''):
    if text:
        return "HP在10%以下：15秒内，恢复50%的HP(冷却时间60秒), 技能、消耗品、装备的HP恢复效果 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_819(char={}, mode=0, text=False, part=''):
    if text:
        return "HP在20%以下：被击时，消耗所有MP，根据消耗的MP恢复HP(冷却时间60秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_820(char={}, mode=0, text=False, part=''):
    if text:
        return "HP在30%以下：攻击领主时，恢复1%的HP(冷却时间1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_821(char={}, mode=0, text=False, part=''):
    if text:
        return "HP在50%以下时，所有速度+20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_822(char={}, mode=0, text=False, part=''):
    if text:
        return "HP在50%以下时，物理/魔法暴击率 +20%, HP在10%以上时，每次攻击会减少5%的HP (该效果不会将HP减少到5%以下，冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_823(char={}, mode=0, text=False, part=''):
    if text:
        return "HP在70%以上：技能冷却时间 -10%(觉醒技能除外), HP在50%~70%：技能冷却时间 -12%(觉醒技能除外), HP在50%以下：技能冷却时间 -15%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_824(char={}, mode=0, text=False, part=''):
    if text:
        return "HP在90%以上：每2秒，20秒内，物理、魔法暴击率 +2%(最多叠加5次), HP在90%以下：每3秒，物理、魔法暴击重叠次数解除1次"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_825(char={}, mode=0, text=False, part=''):
    if text:
        return "HP在90%以上时，技能冷却时间恢复速度 +10%(觉醒除外), 被击伤害 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_826(char={}, mode=0, text=False, part=''):
    if text:
        return "HP在90%以下时，进行攻击可恢复2%的HP(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_827(char={}, mode=0, text=False, part=''):
    if text:
        return "MP MAX+2000, 技能MP消耗量+100%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_828(char={}, mode=0, text=False, part=''):
    if text:
        return "MP MAX+4196, 技能MP消耗量+50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_829(char={}, mode=0, text=False, part=''):
    if text:
        return "MP低于50%时，发动农夫的祝福，恢复20%的MP(冷却时间40)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_830(char={}, mode=0, text=False, part=''):
    if text:
        return "MP在10%以下的状态持续10秒以上：10秒内，伤害增加 3557"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_831(char={}, mode=0, text=False, part=''):
    if text:
        return "MP在20%以下时，伤害增加 2223"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_832(char={}, mode=0, text=False, part=''):
    if text:
        return "MP在50%以下：HP/MP每分钟恢复量 +5000%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_833(char={}, mode=0, text=False, part=''):
    if text:
        return "MP在90%以上：每2秒，20秒内，伤害增加 711(最多叠加5次), MP在90%以下：每3秒减少1次伤害增加效果叠加次数"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_834(char={}, mode=0, text=False, part=''):
    if text:
        return "Y轴移动速度 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_835(char={}, mode=0, text=False, part=''):
    if text:
        return "按住受身蹲伏时，最多4秒内，每秒恢复5%的HP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_836(char={}, mode=0, text=False, part=''):
    if text:
        return "暗属性抗性 +20"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_837(char={}, mode=0, text=False, part=''):
    if text:
        return "暗属性抗性 +50, 火属性抗性、冰属性抗性、光属性抗性 -20"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_838(char={}, mode=0, text=False, part=''):
    if text:
        return "暗属性强化达150以上：物理、魔法暴击率 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_839(char={}, mode=0, text=False, part=''):
    if text:
        return "暴击5次时，使300px范围内所有敌人进入灼烧状态(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_840(char={}, mode=0, text=False, part=''):
    if text:
        return "金币1亿以下(无效果)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_840_1(char={}, mode=0, text=False, part=''):
    if text:
        return "金币1亿以上(10%暴击)"
    if mode == 0:
        char.物理暴击率增加(0.1)
        char.魔法暴击率增加(0.1)
    if mode == 1:
        pass


def entry_840_2(char={}, mode=0, text=False, part=''):
    if text:
        return "金币4亿以上(3%技攻)"
    if mode == 0:
        char.物理暴击率增加(0.1)
        char.魔法暴击率增加(0.1)
        char.技能攻击力增加(0.03)
    if mode == 1:
        pass


entry_func_list[840] = [entry_840, entry_840_1, entry_840_2]
multi_select[840] = False


def entry_841(char={}, mode=0, text=False, part=''):
    if text:
        return "背包与仓库金币总和每达到1千万金币，伤害增加 222(最多叠加20次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_842(char={}, mode=0, text=False, part=''):
    if text:
        return "背击5次时，使300px范围内所有敌人进入中毒状态(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_843(char={}, mode=0, text=False, part=''):
    if text:
        return "背击攻击时，使敌人随机进入出血、灼烧、中毒、感电状态中的1种，效果持续10秒(冷却时间10秒), 所有异常状态抗性 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_844(char={}, mode=0, text=False, part=''):
    if text:
        return "被暗属性攻击时，5秒内，恢复5%的HP(冷却时间3秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_845(char={}, mode=0, text=False, part=''):
    if text:
        return "被暗属性攻击时，暗属性强化 +30，效果持续10秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_846(char={}, mode=0, text=False, part=''):
    if text:
        return "被冰属性攻击时，5秒内，恢复5%的HP(冷却时间3秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_847(char={}, mode=0, text=False, part=''):
    if text:
        return "被冰属性攻击时，冰属性强化 +30，效果持续10秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_848(char={}, mode=0, text=False, part=''):
    if text:
        return "被攻击时，有25%的几率使自身受到惊吓，物理、魔法防御力 +10%，效果持续10秒(最多叠加2次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_849(char={}, mode=0, text=False, part=''):
    if text:
        return "被光属性攻击时，5秒内，恢复5%的HP(冷却时间3秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_850(char={}, mode=0, text=False, part=''):
    if text:
        return "被光属性攻击时，光属性强化 +30，效果持续10秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_851(char={}, mode=0, text=False, part=''):
    if text:
        return "被火属性攻击时，5秒内，恢复5%的HP(冷却时间3秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_852(char={}, mode=0, text=False, part=''):
    if text:
        return "被火属性攻击时，火属性强化 +30，效果持续10秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_853(char={}, mode=0, text=False, part=''):
    if text:
        return "被击后，3秒内，攻击敌人时，在各时间段恢复所受伤害(冷却时间3秒), - 1秒内：攻击时所受伤害的70%, - 2秒内：攻击时所受伤害的50%, - 3秒内：攻击时所受伤害的20%, "
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_854(char={}, mode=0, text=False, part=''):
    if text:
        return "被击伤害 +10%, 物理暴击率 +5%, 魔法暴击率 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_855(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时，冰属性强化 +20，效果持续10秒(最多叠加1次), HP MAX -1000"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_856(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时，暗属性强化 +20，效果持续10秒(最多叠加1次), HP MAX -1000"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_857(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时，光属性强化 +20，效果持续10秒(最多叠加1次), HP MAX -1000"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_858(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时，恢复5%的HP(冷却时间20秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_859(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时，火属性强化 +20，效果持续10秒(最多叠加1次), HP MAX -1000"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_860(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时，所有属性强化 -1，被击时所受伤害-1%(最多叠加10次，该属性仅在受到HP1%以上伤害时适用)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_861(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时，消耗10%的MP，30秒内，攻击速度、移动速度 +15%，施放速度 +20%(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_862(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时，自身周围300px随机位置召唤救济无人机(救济箱只能发动者获得，冷却时间30秒),  拾取救济箱时，恢复30%的HP和MP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_863(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时按跳跃键(C)，可从当前位置瞬移至一定距离的掉落位置(冷却时间10秒), - 瞬移期间按方向键可调整方向, 瞬移后恢复10%的HP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_864(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时所受攻击转换为冰属性伤害, 被击时，冰属性抗性 +5，效果持续10秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_865(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时所受攻击转换为光属性伤害, 被击时，光属性抗性 +5，效果持续10秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_866(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时所受攻击转换为火属性伤害, 被击时，火属性抗性 +5，效果持续10秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_867(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时所受伤害转换为暗属性伤害, 被击时，暗属性抗性 +5，效果持续10秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_868(char={}, mode=0, text=False, part=''):
    if text:
        return "被击时先消耗MP, HP MAX -99%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_869(char={}, mode=0, text=False, part=''):
    if text:
        return "被击所受伤害的50%在10秒内分开承受, 分开承受伤害期间，HP恢复效果 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_870(char={}, mode=0, text=False, part=''):
    if text:
        return "被正面攻击时，所受伤害 -40%, 被背击、破招攻击时，所受伤害 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_871(char={}, mode=0, text=False, part=''):
    if text:
        return "被正面攻击时，有20%的几率，生成相当于最大HP10%的保护罩(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_872(char={}, mode=0, text=False, part=''):
    if text:
        return "冰冻抗性 +3%, 灼烧抗性 -1.5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_873(char={}, mode=0, text=False, part=''):
    if text:
        return "冰冻抗性 -3% 聊天窗输入含“冰”时，自身进入10秒冰冻(冷却时间30秒), 该装备词条的冰冻在聊天窗输入含“砰”时解除"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_874(char={}, mode=0, text=False, part=''):
    if text:
        return "冰属性攻击灼烧敌人时，引发剧烈爆炸(冷却时间0.5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_875(char={}, mode=0, text=False, part=''):
    if text:
        return "冰属性抗性 +50,  火属性抗性、光属性抗性、暗属性抗性 -20"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_876(char={}, mode=0, text=False, part=''):
    if text:
        return "冰属性强化达150以上：物理、魔法暴击率 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_877(char={}, mode=0, text=False, part=''):
    if text:
        return "不消耗无色小晶块的技能攻击力 +20%, 消耗无色小晶块的技能攻击力 -10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_879(char={}, mode=0, text=False, part=''):
    if text:
        return "不消耗无色小晶块的技能冷却时间-30%, 消耗无色小晶块的技能冷却时间+15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_880(char={}, mode=0, text=False, part=''):
    if text:
        return "草莓极光状态下，消耗品的HP恢复效果提高20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_881(char={}, mode=0, text=False, part=''):
    if text:
        return "出血抗性 +1%, 物理防御力 +500"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_882(char={}, mode=0, text=False, part=''):
    if text:
        return "出血伤害 +15%, 出血抗性 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_883(char={}, mode=0, text=False, part=''):
    if text:
        return "出血伤害 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_884(char={}, mode=0, text=False, part=''):
    if text:
        return "除Buff技能外所有职业Lv40主动技能Lv +10, - 如下技能除外：猫拳、爱之急救、生命源泉、复苏之光、六道, 施放Lv40技能时，该技能Lv -1(最多减少Lv10，该效果适用至通关前), 剩余HP在70%以下的状态持续120秒时，恢复减少的技能Lv(冷却时间120秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_885(char={}, mode=0, text=False, part=''):
    if text:
        return "除Buff技能外所有职业Lv45主动技能Lv +10, - 如下技能除外：圣愈之风、新生圣歌, 施放Lv45技能时，该技能Lv -1(最多减少Lv10，该效果适用至通关前), 剩余HP在70%以下的状态持续120秒时，恢复减少的技能Lv(冷却时间120秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_886(char={}, mode=0, text=False, part=''):
    if text:
        return "除Buff技能外所有职业Lv35主动技能Lv +10, - 如下技能除外：嗜血、暗影蓄能, 、挑衅、幻影化身、忍法 : 残影术, 施放Lv35技能时，该技能Lv-1(最多减少Lv10，该效果适用至通关前), 剩余HP在70%以下的状态持续120秒时，恢复减少的技能Lv(冷却时间120秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_887(char={}, mode=0, text=False, part=''):
    if text:
        return "除Buff技能外所有职业Lv60主动技能Lv +10, 施放Lv60技能时，该技能Lv-1(最多减少Lv10，该效果适用至通关前), 剩余HP在70%以下的状态持续120秒时，恢复减少的技能Lv(冷却时间120秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_888(char={}, mode=0, text=False, part=''):
    if text:
        return "除Buff技能外所有职业Lv70主动技能Lv +10, - 如下技能除外 : 永恒的占有、圣洁之翼,  施放Lv70技能时，该技能Lv-1(最多减少Lv10，该效果适用至通关前), 剩余HP在70%以下的状态持续120秒时，恢复减少的技能Lv(冷却时间120秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_889(char={}, mode=0, text=False, part=''):
    if text:
        return "穿戴时生成灵魂剑, 施放技能时，灵魂剑累积5层灵魂(最多50), 普攻时，消耗1层灵魂，灵魂剑对敌人额外造成伤害(冷却时间0.1秒), 灵魂满层数时，普攻时，消耗所有灵魂层数，灵魂剑对敌人额外造成伤害"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_890(char={}, mode=0, text=False, part=''):
    if text:
        return "存在无力化状态的敌人时，所有技能冷却时间恢复速度+50%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_894(char={}, mode=0, text=False, part=''):
    if text:
        return "待机、行走、前冲状态下，[装备属性操作键]输入时，瞬移至一定距离的位置(冷却时间20秒), 瞬移时，按方向键可调整方向, 瞬移后，10秒内，移动速度 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_895(char={}, mode=0, text=False, part=''):
    if text:
        return "待机、行走时，Y轴移动速度 +50%, 前冲时Y轴移动速度 -50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_896(char={}, mode=0, text=False, part=''):
    if text:
        return "待机、行走时，获得伪装Buff, - 伪装Buff解除时，进入5秒冷却, 前冲、被击时，伪装Buff解除"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_897(char={}, mode=0, text=False, part=''):
    if text:
        return "待机、行走时，移动速度 +200%, 前冲时移动速度 -100%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_898(char={}, mode=0, text=False, part=''):
    if text:
        return "当敌人处于3种以上异常状态时，该敌人周围300px内无异常状态的敌人进入相同的异常状态(冷却时间25秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_900(char={}, mode=0, text=False, part=''):
    if text:
        return "当自身面对敌人3秒时，使300px范围内自身面对的敌人进入石化状态(冷却时间30秒), 自身进入异常状态时，HP -2.5%(该效果不会使HP减少到1%以下，冷却时间20秒), , 攻击石化状态敌人时，技能攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_901(char={}, mode=0, text=False, part=''):
    if text:
        return "地图上有小太阳时，赋予武器光属性攻击和火属性攻击效果"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_902(char={}, mode=0, text=False, part=''):
    if text:
        return "地下城入场后，每10%消耗的HP，伤害增加 400(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_903(char={}, mode=0, text=False, part=''):
    if text:
        return "地下城入场时，伤害增加 3260, 被击时所受伤害 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_904(char={}, mode=0, text=False, part=''):
    if text:
        return "非破招攻击时，技能攻击力+35%, 破招攻击时，技能攻击力-20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_905(char={}, mode=0, text=False, part=''):
    if text:
        return "孵化宠物个数达20个以上：获得光谱，所有速度 +15%，技能冷却时间 -8%(觉醒除外，光谱仅获得1个)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_906(char={}, mode=0, text=False, part=''):
    if text:
        return "复活后，300秒内每次受到攻击，恢复10%的生命值(最多5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_907(char={}, mode=0, text=False, part=''):
    if text:
        return "感电抗性 +3%, 中毒抗性 +3%, 出血抗性 +3%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_908(char={}, mode=0, text=False, part=''):
    if text:
        return "感电伤害 +15%, 感电抗性 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_909(char={}, mode=0, text=False, part=''):
    if text:
        return "感电伤害 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_910(char={}, mode=0, text=False, part=''):
    if text:
        return "根据孵化宠物个数，发动词条, - 3~9个：伤害增加 1482, - 10个以上：伤害增加 2075"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_913(char={}, mode=0, text=False, part=''):
    if text:
        return "根据前冲持续时间，增加攻击速度、施放速度、移动速度(词条效果在前冲结束后适用), - 前冲1秒以上：攻击速度 +5%，施放速度 +7.5%，移动速度 +5%, - 前冲2秒以上：攻击速度 +10%，施放速度 +15%，移动速度 +10%, - 前冲4秒以上：攻击速度 +20%，施放速度 +30%，移动速度 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_914(char={}, mode=0, text=False, part=''):
    if text:
        return "根据装扮背包中的装扮个数，发动效果, - 21~50个 : 伤害增加 1482, - 51个以上：伤害增加 2668"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_915(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击50次领主、绿名、稀有怪物时，敌人血管爆裂，剩余HP -2%(最多5次，辅助职业无法触发该效果),  - 每次血管爆裂，条件次数增加5倍,  - 领主血管爆裂时，30秒内，攻击速度 +15%，施放速度 +22.5%，移动速度 +15%(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_916(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击冰冻敌人30次时，冰冻状态持续时间 +5秒(冷却时间15秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_917(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击冰冻敌人时，引发寒冰爆炸(冷却时间0.5秒), 攻击冰冻状态敌人时，技能攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_918(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击感电敌人时，引发闪光爆炸(冷却时间0.5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_919(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击感电敌人时，周围300px范围内，随机坠落闪电，使敌人与自身感电(冷却时间15秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_920(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击感电状态敌人时，使敌人进入眩晕状态(冷却时间20秒), 攻击眩晕状态敌人时，技能攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_921(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击感电状态敌人时，引发EMP冲击，消耗2%的MP，对敌人造成光属性伤害(冷却时间10秒), 攻击感电敌人时，EMP冲击冷却时间 -1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_922(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击石化状态的敌人时，可使所有进入石化状态的敌人所受伤害+20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_923(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击石化状态的敌人时，可以储存伤害，敌人石化状态结束后，储存的伤害会一次性爆发, - 每命中一个技能储存2%(最多20%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_924(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有2%的几率使300px范围内的敌人进入石化状态(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_925(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，所有异常状态抗性 +3%，效果持续20秒(最多叠加5次), 被击时，所有异常状态抗性增加效果叠加次数 -2"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_926(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，触发暗属性爆炸，对自身与敌人造成伤害(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_927(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，触发冰属性爆炸，对自身与敌人造成伤害(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_928(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，触发光属性爆炸，对自身与敌人造成伤害(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_929(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，触发火属性爆炸，对自身与敌人造成伤害(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_930(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，敌人的异常数量增加时，伤害增加 889(最多叠加3次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_931(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，敌人的异常数量增加时，物理、魔法防御力 +4000(最多叠加3次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_932(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，攻击速度、施放速度 +2%(最多叠加15次), 非攻击状态下，攻击速度、施放速度增加效果叠加次数每0.5秒减少1次"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_933(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，恢复0.1%MP(冷却时间0.1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_934(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，恢复3%的HP(冷却时间5秒), 技能、消耗品的HP恢复效果 -99%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_935(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，减少10%的HP最大值，伤害增加 889(最多叠加5次，冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_936(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，技能冷却时间恢复速度+2%(觉醒技能除外，冷却时间1秒，最多叠加10次), 受到总HP1%以上伤害时，技能冷却时间恢复速度效果叠加次数 -2"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_937(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，伤害增加 356(最多叠加10次，被击时减少1次), 装备词条的伤害增加每叠加1次，移动速度 -2%(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_938(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，消耗10%的MP，30秒内，攻击速度 +15%，施放速度 +20%，移动速度 +15%(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_939(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，消耗2%的HP，周围500px内引发爆炸(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_940(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有10%的几率，向300px范围内敌人坠落闪电(冷却时间1秒), 被闪电击中的敌人进入感电状态(冷却时间15秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_941(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有10%的几率扔出1个农作物(冷却20秒，最多存在1次), 收获农作物时获得效果, - 大白菜：恢复18%的HP, - 巨型南瓜：恢复15%HP和 MP, - 大萝卜：回复18%的MP, - 巨枝：回复15%的HP，身体变得强壮，持续 30 秒, - 大白菜：MP恢复15%，头脑变得清醒，持续30秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_942(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有3%的几率使敌人进入失明状态(冷却时间1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_943(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有5%的几率，消耗3个红色小晶块，使自身与300px范围内的敌人进入灼烧状态(冷却时间10秒), 灼烧伤害 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_944(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率，根据冰属性强化数值，发动冰元素攻击(冷却时间5秒), - 冰属性强化100~150：发动冰阵, - 冰属性强化150~250：发动冰息, - 冰属性强化250以上：发动暴风雪, - 被暴风雪命中的敌人进入冰冻状态，持续10秒(冷却时间30秒), - 发动暴风雪时，冰属性抗性+20，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_945(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率，根据光属性强化数值，发动光元素攻击(冷却时间5秒), - 光属性强化100~150：发动光爆, - 光属性强化150~250：发动闪电, - 光属性强化250以上：发动雷暴, - 被雷暴命中的敌人进入感电状态，持续10秒(冷却时间15秒), - 发动雷暴时，光属性抗性+20，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_946(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率，根据火属性强化数值，发动火元素攻击(冷却时间5秒), - 火属性强化100~150：发动火爆, - 火属性强化150~250：发动火路, - 火属性强化250以上：发动陨石, - 被陨石命中的敌人进入灼烧状态，持续10秒(冷却时间15秒), - 发动陨石时，火属性抗性+20，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_947(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率，根据自身暗属性强化数值，发动暗元素攻击(冷却时间5秒), - 暗属性强化100~150：发动黑爆, - 暗属性强化150~250：发动黑球, - 暗属性强化250以上：发动黑洞, - 被黑洞命中的敌人进入失明状态，持续10秒(冷却时间30秒), - 发动黑洞时，暗属性抗性 +20，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_948(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，有50%的几率生成黑白球，持续10秒(冷却时间1秒), - 黑球：15秒内，攻击速度 +8%，施放速度 +12%(最多叠加3次), - 白球：15秒内，生成相当于HP最大值10%的保护罩(最多叠加1次), 获得球时，自身HP/MP-1%，15秒内，移动速度 +20(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_949(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，增加1层电池(冷却时间10秒), 每1层电池，伤害增加 667(最多叠加4次), 达到5层电池3秒后，引发强烈爆炸，减少30%的HP，初始化层数, 电池爆炸时，物理、魔法防御力 -20000，攻击速度、移动速度 、施放速度 +40%，效果持续30秒, 施放后跳时，减少1层电池"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_950(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，自身脚下生成光之领域(冷却时间5秒), 站在光之领域上，所受伤害 -10%, 脱离光之领域时，光之领域立即删除, 光之领域最多生成1个, - 站在光之领域上，攻击20次时，光之领域大小增加(最多5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_951(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时生成幽灵(冷却时间0.5秒),  - 幽灵追击周围200px内最近敌人引发爆炸,  - 没有可追击敌人时，原地3秒后爆炸,  生成幽灵时，有30%的几率，生成2个幽灵"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_952(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时有1%几率使敌人进入诅咒状态，持续3 秒(冷却时间1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_953(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时有15%几率扔出最多5个农作物, 每扔出一个农作物，增加3%的物理、魔法暴击率，效果持续30秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_954(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时有3%几率使敌人进入冰冻状态，持续1秒(冷却时间1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_955(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时有5%几率增加7%命中率，效果持续10秒(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_956(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击速度 +5%, 施放速度 +7.5%, 技能MP消耗量 +50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_957(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击速度 +5%, 移动速度 +5%, 施法速度 +8%, HP MAX -250"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_958(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击速度、施放速度之和在100以下：技能冷却时间-10%(觉醒除外),  攻击速度、施放速度之和在100以上：技能冷却时间+10%(觉醒除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_959(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击无力化状态的敌人时，技能攻击力 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_960(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击异常状态敌人时，技能攻击力 +5%, 攻击非异常状态敌人时，技能攻击力 -5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_961(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击异常状态敌人时，恢复1500的HP(冷却时间0.5秒), 自身进入异常状态时，HP -2.5%(该效果不会使HP减少到1%以下，冷却时间20秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_962(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击异常状态敌人时，恢复1%的HP(冷却时间1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_963(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击与施放时，自身周围300px随机位置召唤补给箱无人机(补给箱只能发动者获得，冷却时间20秒),  拾取补给箱时，20秒内，伤害增加 3409"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_964(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击灼烧敌人时，5秒内，获得1个火种, 火种到达5个时，消耗所有火种，引发爆炸"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_965(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击灼烧敌人时，除觉醒外所有技能剩余冷却时间 -0.5%(冷却时间0.5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_966(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击灼烧敌人时，触发冰冻(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_967(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击灼烧敌人时，火属性强化+5，火属性抗性 -10，效果持续5秒(冷却时间1秒，最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_968(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击灼烧敌人时，使300px范围内所有敌人进入灼烧状态(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_969(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击灼烧敌人时，引发火焰爆炸(冷却时间0.5秒), 攻击灼烧状态敌人时，技能攻击力 +2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_970(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击灼烧敌人时，引发火属性爆炸(冷却时间1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_971(char={}, mode=0, text=False, part=''):
    if text:
        return "光属性抗性 +50, 火属性抗性、冰属性抗性、暗属性抗性 -20"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_972(char={}, mode=0, text=False, part=''):
    if text:
        return "光属性强化达150以上时，物理、魔法暴击率 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_973(char={}, mode=0, text=False, part=''):
    if text:
        return "回避率 +10%, 被击时，20秒内，物理、魔法暴击率 +10%(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_974(char={}, mode=0, text=False, part=''):
    if text:
        return "回避率 +5%, 混乱抗性 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_975(char={}, mode=0, text=False, part=''):
    if text:
        return "火、冰、光、暗属性数值相同时，赋予武器全属性攻击"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_976(char={}, mode=0, text=False, part=''):
    if text:
        return "火、冰、光、暗属性数值相同时，所有属性抗性 +25"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_977(char={}, mode=0, text=False, part=''):
    if text:
        return "火属性攻击时，使敌人进入灼烧状态(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_978(char={}, mode=0, text=False, part=''):
    if text:
        return "火属性抗性 +50, 冰属性抗性、光属性抗性、暗属性抗性 -20"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_979(char={}, mode=0, text=False, part=''):
    if text:
        return "火属性强化达150以上：物理、魔法暴击率 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_980(char={}, mode=0, text=False, part=''):
    if text:
        return "获得该装备词条的队友之间获得效果, - 相互分摊伤害, - 其他队友受到伤害时，自身攻击速度、移动速度 +2%，效果持续5秒(最多叠加5次), 被击伤害 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_981(char={}, mode=0, text=False, part=''):
    if text:
        return "击杀敌人后，恢复10%MP, 技能MP消耗量+50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_982(char={}, mode=0, text=False, part=''):
    if text:
        return "击杀敌人后，恢复5%HP, 攻击石化状态敌人时，技能攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_983(char={}, mode=0, text=False, part=''):
    if text:
        return "基础精通技能攻击力增加量+30%, Lv15~30主动技能攻击力 +10%, 消耗无色小晶块的技能攻击力-15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_984(char={}, mode=0, text=False, part=''):
    if text:
        return "基础精通技能攻击力增加量+30%, Lv15~30主动技能攻击力 +10%, 消耗无色小晶块的技能冷却时间+10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_985(char={}, mode=0, text=False, part=''):
    if text:
        return "技能、装备的HP恢复效果 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_986(char={}, mode=0, text=False, part=''):
    if text:
        return "技能MP消耗量 +100%, 技能冷却时间 -12%(觉醒除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_987(char={}, mode=0, text=False, part=''):
    if text:
        return "技能MP消耗量 -20%, MP MAX +4196"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_988(char={}, mode=0, text=False, part=''):
    if text:
        return "技能MP消耗量在4000以上的技能攻击力 +15%(觉醒除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_989(char={}, mode=0, text=False, part=''):
    if text:
        return "技能和消耗品的HP恢复效果 -10%, 装备的HP恢复效果 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_990(char={}, mode=0, text=False, part=''):
    if text:
        return "技能快捷栏中每存在1个处于冷却中的技能，快捷栏中技能冷却时间恢复速度 +3.5%(最多增加42%，觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_991(char={}, mode=0, text=False, part=''):
    if text:
        return "技能冷却时间15秒以上的技能攻击力 +10%, 技能冷却时间15秒以下的技能攻击力 -15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_992(char={}, mode=0, text=False, part=''):
    if text:
        return "角色处于灼烧、中毒、出血、感电状态中至少一种时攻击敌人，有5%的几率使敌人进入与角色相同的异常状态(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_993(char={}, mode=0, text=False, part=''):
    if text:
        return "角色进入睡眠状态时，技能冷却时间恢复速度 +50%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_994(char={}, mode=0, text=False, part=''):
    if text:
        return "角色进入睡眠状态时，在10秒内恢复60%的HP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_995(char={}, mode=0, text=False, part=''):
    if text:
        return "角色所经之处留下寒冰地带，持续3秒(冷却时间0.5秒，跳跃、技能的移动不会产生寒冰地带), 接触寒冰地带2秒的敌人进入冰冻状态(冷却时间25秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_996(char={}, mode=0, text=False, part=''):
    if text:
        return "角色所经之处留下火焰地带，持续3秒(冷却时间0.5秒，跳跃、技能的移动不会产生火焰地带), 接触火焰地带的敌人进入灼烧状态(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_999(char={}, mode=0, text=False, part=''):
    if text:
        return "觉醒技能攻击力-25%, 非觉醒技能攻击力+20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1000(char={}, mode=0, text=False, part=''):
    if text:
        return "空中被击时，按拍卖行键，恢复滞空姿势(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1001(char={}, mode=0, text=False, part=''):
    if text:
        return "聊天窗输入含有“哇”时，召唤战争领主(冷却时间120秒，地图内存在战争领主时无法召唤), - 战争领主持续时间 : 40秒, - 消灭敌人时，召唤冷却时间 -1秒, - 施放技能时，召唤冷却时间 -1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1002(char={}, mode=0, text=False, part=''):
    if text:
        return "落地时，物理、魔法防御力 +20%，伤害增加 593，效果持续10秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1003(char={}, mode=0, text=False, part=''):
    if text:
        return "落地时，1秒内，生成相当于HP最大值10%的保护罩(冷却时间5秒), 跳跃力 -100"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1004(char={}, mode=0, text=False, part=''):
    if text:
        return "落地时，伤害增加 2223 ，移动速度 +100%，效果持续2秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1005(char={}, mode=0, text=False, part=''):
    if text:
        return "落地时，引发冲击波，对周围敌人造成伤害, 引发冲击波时，有20%的几率，引发更强的冲击波，使敌人进入眩晕状态(冷却时间20秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1006(char={}, mode=0, text=False, part=''):
    if text:
        return "每10%的回避率增加5%的移动速度(最多增加25%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1007(char={}, mode=0, text=False, part=''):
    if text:
        return "每10%的移动速度，物理、魔法防御力 +500(最多叠加20次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1008(char={}, mode=0, text=False, part=''):
    if text:
        return "每10%的移速，物理、魔法暴击率 +1%(最多增加10%), 移动速度 -30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1009(char={}, mode=0, text=False, part=''):
    if text:
        return "每10秒，HP MAX +100(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1010(char={}, mode=0, text=False, part=''):
    if text:
        return "每10秒，MP MAX +100(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1011(char={}, mode=0, text=False, part=''):
    if text:
        return "每10秒，自身进入消耗品无法解除的感电状态，效果持续10秒, 自身进入感电状态时，所有属性强化 +15，所有属性抗性 +15"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1012(char={}, mode=0, text=False, part=''):
    if text:
        return "每11点火属性抗性，增加5%的所有速度(最多增加45%) 被击时，10秒内，所有速度-30%(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1013(char={}, mode=0, text=False, part=''):
    if text:
        return "每1点暗属性抗性，增加1点暗属性强化(最多增加30点), 暗属性抗性 -20"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1014(char={}, mode=0, text=False, part=''):
    if text:
        return "每1点冰属性抗性，增加1点冰属性强化(最多增加30点), 冰属性抗性 -20"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1015(char={}, mode=0, text=False, part=''):
    if text:
        return "每1点光属性抗性，增加1点光属性强化(最多增加30点), 光属性抗性 -20"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1016(char={}, mode=0, text=False, part=''):
    if text:
        return "每1点火属性抗性，增加1点火属性强化(最多增加30点), 火属性抗性 -20"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1017(char={}, mode=0, text=False, part=''):
    if text:
        return "每1个扩展技能栏中的技能，未放置扩展技能栏的技能攻击力 +2%(最多增加14%), 扩展技能栏的技能攻击力 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1020(char={}, mode=0, text=False, part=''):
    if text:
        return "每1名异常敌人，伤害增加 326(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1021(char={}, mode=0, text=False, part=''):
    if text:
        return "每20%的移动速度，增加6点最高属强(最多增加30点)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1022(char={}, mode=0, text=False, part=''):
    if text:
        return "每25点最高属抗，除觉醒外技能冷却时间 -5%(最多减少15%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1023(char={}, mode=0, text=False, part=''):
    if text:
        return "每30%移动速度，技能冷却时间恢复速度 +10%(最多增加30%，觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1024(char={}, mode=0, text=False, part=''):
    if text:
        return "每30秒随机消耗普通、高级灵魂中的1个，适用以下效果, - 普通灵魂：恢复10%的HP, - 普通灵魂：恢复10%的MP, - 高级灵魂：恢复10%的HP、MP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1025(char={}, mode=0, text=False, part=''):
    if text:
        return "每30秒消耗1个稀有灵魂，30秒内伤害增加 2371, 累计消耗5个稀有灵魂，30秒内伤害增加 1186"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1026(char={}, mode=0, text=False, part=''):
    if text:
        return "每40秒出现一朵云朵，持续40秒, 云朵存在时，提供增益，持续40秒, - 暗属性抗性 +15, - 冰属性抗性 +15, - 攻击速度 +10%, - 施放速度 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1027(char={}, mode=0, text=False, part=''):
    if text:
        return "每40秒出现一个小太阳，持续40秒, 地图上有小太阳时，发动buff, - 火属性抗性 +15, - 光属性抗性 +15, - 移动速度 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1028(char={}, mode=0, text=False, part=''):
    if text:
        return "每5点暗属性抗性，攻击速度 +1%，施放速度+ 1.5%(最多叠加10次), 暗属性抗性 -15"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1029(char={}, mode=0, text=False, part=''):
    if text:
        return "每5点冰属性抗性，攻击速度 +1%，施放速度+ 1.5%(最多叠加10次), 冰属性抗性 -15"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1030(char={}, mode=0, text=False, part=''):
    if text:
        return "每5点光属性抗性，攻击速度 +1%，施放速度+ 1.5%(最多叠加10次), 光属性抗性 -15"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1031(char={}, mode=0, text=False, part=''):
    if text:
        return "每5点火属性抗性，攻击速度 +1%，施放速度+ 1.5%(最多叠加10次), 火属性抗性 -15"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1032(char={}, mode=0, text=False, part=''):
    if text:
        return "每8%的MP，物理、魔法暴击率 +3%(最多增加30%), 技能MP消耗量 +100%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1033(char={}, mode=0, text=False, part=''):
    if text:
        return "每8%剩余的MP，除觉醒外的技能冷却时间恢复速度 +3%(最多增加30%), 技能MP消耗量 +100%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1034(char={}, mode=0, text=False, part=''):
    if text:
        return "每8点暗属性强化，火属性强化、光属性强化、冰属性强化 +1(最多增加50), 每10点暗属性抗性，火属性抗性、光属性抗性、冰属性抗性 -1(最多减少30)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1035(char={}, mode=0, text=False, part=''):
    if text:
        return "每8点冰属性强化，火属性强化、光属性强化、暗属性强化 +1(最多增加50), 每10点冰属性抗性，火属性抗性、光属性抗性、暗属性抗性 -1(最多减少30)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1036(char={}, mode=0, text=False, part=''):
    if text:
        return "每8点光属性强化，火属性强化、冰属性强化、暗属性强化 +1(最多增加50), 每10点光属性抗性，火属性抗性、冰属性抗性、暗属性抗性 -1(最多减少30)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1037(char={}, mode=0, text=False, part=''):
    if text:
        return "每8点火属性强化，冰属性强化、光属性强化、暗属性强化 +1(最多增加50), 每10点火属性抗性，冰属性抗性、光属性抗性、暗属性抗性 -1(最多减少30)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1038(char={}, mode=0, text=False, part=''):
    if text:
        return "每次拾取地面掉落道具时，移动速度 +10%，效果持续10秒(最多叠加3次), 每5秒减少5%移动速度(最多叠加5次，拾取道具时解除)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1039(char={}, mode=0, text=False, part=''):
    if text:
        return "每攻击5次，攻击速度 +5%，效果持续30秒(最多增加50%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1040(char={}, mode=0, text=False, part=''):
    if text:
        return "每减少10%的HP，伤害增加 165，物理/魔法防御力 -2200(最多叠加9次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1041(char={}, mode=0, text=False, part=''):
    if text:
        return "每减少10%的MP，伤害增加 362(最多叠加9次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1042(char={}, mode=0, text=False, part=''):
    if text:
        return "每减少5%的HP，伤害增加 156(最多叠加19次), 施放技能时减少1%的HP(剩余HP在1%以下时不适用该效果)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1043(char={}, mode=0, text=False, part=''):
    if text:
        return "每累积消耗50个无色，恢复10%的HP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1045(char={}, mode=0, text=False, part=''):
    if text:
        return "每秒暗属性强化 +2(最多叠加10次), - 受到总HP1%以上伤害时，暗属性强化增加效果叠加次数 -5, 被击时，火属性抗性、冰属性抗性、光属性抗性 -1(最多叠加10次), 物理暴击率 +5%, 魔法暴击率 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1046(char={}, mode=0, text=False, part=''):
    if text:
        return "每秒冰属性强化 +2(最多叠加10次), - 受到总HP1%以上伤害时，冰属性强化增加效果叠加次数 -5, 被击时，火属性抗性、光属性抗性、暗属性抗性 -1(最多叠加10次), 物理暴击率 +5%, 魔法暴击率 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1047(char={}, mode=0, text=False, part=''):
    if text:
        return "每秒光属性强化 +2(最多叠加10次), - 受到总HP1%以上伤害时，光属性强化增加效果叠加次数 -5, 被击时，火属性抗性、冰属性抗性、暗属性抗性 -1(最多叠加10次), 物理暴击率 +5%, 魔法暴击率 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1048(char={}, mode=0, text=False, part=''):
    if text:
        return "每秒火属性强化 +2(最多叠加10次), - 受到总HP1%以上伤害时，火属性强化增加效果叠加次数 -5, 被击时，冰属性抗性、光属性抗性、暗属性抗性 -1(最多叠加10次), 物理暴击率 +5%, 魔法暴击率 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1049(char={}, mode=0, text=False, part=''):
    if text:
        return "每使用5次技能，技能攻击力 +20%，技能冷却时间 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1050(char={}, mode=0, text=False, part=''):
    if text:
        return "每消耗30000点MP，伤害增加 889，效果持续20秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1051(char={}, mode=0, text=False, part=''):
    if text:
        return "魔法防御力 +2000, 物理防御力 -500"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1052(char={}, mode=0, text=False, part=''):
    if text:
        return "农夫的祝福激活时，所有属性抗性 +40，回避率 +5%，效果持续30秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1053(char={}, mode=0, text=False, part=''):
    if text:
        return "破招3次时，使400px范围内所有敌人进入感电状态(冷却时间15秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1054(char={}, mode=0, text=False, part=''):
    if text:
        return "破招攻击力 +15% , 每3秒减少1%的MP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1055(char={}, mode=0, text=False, part=''):
    if text:
        return "破招攻击时，技能攻击力 +10%，效果持续5秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1058(char={}, mode=0, text=False, part=''):
    if text:
        return "基础精通技能攻击力 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1065(char={}, mode=0, text=False, part=''):
    if text:
        return "前冲、行走状态下，[装备操作键]输入时，角色巨大化，持续25秒, - 所受伤害 -20%, - 禁用技能及普攻, - 移动速度 -20%, - 前冲持续引发冲击波，跳跃落地后引发更强冲击波, - 巨大化时霸体"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1066(char={}, mode=0, text=False, part=''):
    if text:
        return "前冲攻击时，疾跑至前方400px距离(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1067(char={}, mode=0, text=False, part=''):
    if text:
        return "前冲期间，每0.5秒，所受伤害-3%(最多叠加10次，停留时每秒减少1层叠加效果)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1068(char={}, mode=0, text=False, part=''):
    if text:
        return "前冲时，移动速度 +100%，持续0.5秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1069(char={}, mode=0, text=False, part=''):
    if text:
        return "前冲时回避率 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1070(char={}, mode=0, text=False, part=''):
    if text:
        return "前冲时每0.2秒移动速度 +3%(最多叠加15次，非前冲状态下每0.5秒减少1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1071(char={}, mode=0, text=False, part=''):
    if text:
        return "伤害的50%转化为中毒伤害, 中毒伤害 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1072(char={}, mode=0, text=False, part=''):
    if text:
        return "伤害的50%转化为灼烧伤害, 灼烧伤害 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1073(char={}, mode=0, text=False, part=''):
    if text:
        return "伤害的50%转换为出血伤害, 出血伤害 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1074(char={}, mode=0, text=False, part=''):
    if text:
        return "伤害的50%转换为感电伤害, 感电伤害 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1075(char={}, mode=0, text=False, part=''):
    if text:
        return "生成草坪休息点，HP MAX +10%，持续30秒(冷却10秒，最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1076(char={}, mode=0, text=False, part=''):
    if text:
        return "生命值低于50%时，发动渔夫的祝福，回复20%的生命值(冷却时间40秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1077(char={}, mode=0, text=False, part=''):
    if text:
        return "剩余HP在50%以下时，物理、魔法防御力+7000，伤害增加 2223，技能攻击力 +5%, 被击伤害 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1078(char={}, mode=0, text=False, part=''):
    if text:
        return "剩余HP在80%以上时，伤害增加 445, 剩余HP在50%到80%之间时，伤害增加 2668, 剩余HP在50%以下时，伤害增加 2668，技能攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1079(char={}, mode=0, text=False, part=''):
    if text:
        return "剩余MP在90%以上时，伤害增加 445, 剩余MP在60%到90%之间时，伤害增加 2668, 剩余MP在60%以下时，伤害增加 4298"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1080(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv1~35技能时，Lv1~35技能攻击力 -2%，效果持续20秒, Lv40~80技能冷却时间恢复速度 +10%(最多叠加5次，觉醒除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1081(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv30以下技能时，基础精通攻击力+15%，Lv15~30主动技能攻击力 +5%，效果持续10秒(冷却时间1秒，最多叠加3次), 施放Lv45以上技能时，基础精通攻击力增加效果和Lv15~30主动技能攻击力增加效果叠加次数 -1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1082(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv35技能时，所有属性强化 +20，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1083(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv35以下技能时，火属性强化 +4，效果持续15秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1084(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv35以下技能时，暗属性强化 +4，效果持续15秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1085(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv35以下技能时，冰属性强化 +4，效果持续15秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1086(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv35以下技能时，光属性强化 +4，效果持续15秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1087(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv40~80技能时，Lv40~80技能攻击力 -2%，效果持续20秒, Lv1~35技能冷却时间恢复速度 +10%(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1088(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv40技能时，所有属性强化 +20，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1089(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv40以上技能时，火属性抗性 +3，效果持续15秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1090(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv40以上技能时，暗属性抗性 +3，效果持续15秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1091(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv40以上技能时，冰属性抗性 +3，效果持续15秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1092(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv40以上技能时，光属性抗性 +3，效果持续15秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1093(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv45技能时，所有属性强化 +20，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1094(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv60技能时，所有属性强化 +20，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1095(char={}, mode=0, text=False, part=''):
    if text:
        return "施放Lv70技能时，所有属性强化 +20，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1097(char={}, mode=0, text=False, part=''):
    if text:
        return "施放后跳期间，所受伤害-10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1098(char={}, mode=0, text=False, part=''):
    if text:
        return "施放后跳期间，移动速度 +200%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1099(char={}, mode=0, text=False, part=''):
    if text:
        return "施放后跳时，10秒内，增加8%的攻击速度、施放速度(最多叠加3次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1100(char={}, mode=0, text=False, part=''):
    if text:
        return "施放后跳时，施放回避之吼，落地之前，回避率 +50%(3秒内可连续使用3次，3秒后发动冷却时间7秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1101(char={}, mode=0, text=False, part=''):
    if text:
        return "施放技能期间被击时，不会被中断，而是继续施放(冷却时间10秒),  施放技能期间被击时，所受伤害+15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1102(char={}, mode=0, text=False, part=''):
    if text:
        return "施放技能时，根据技能消耗的无色小晶块数量增加该技能的攻击力, - 消耗1个以上时，技能攻击力+2%, - 消耗15个以上时，技能攻击力+10%, - 消耗30个以上时，技能攻击力+20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1104(char={}, mode=0, text=False, part=''):
    if text:
        return "施放技能时，恢复相当于技能MP消耗量10%的HP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1105(char={}, mode=0, text=False, part=''):
    if text:
        return "施放技能时，伤害增加 504，技能MP消耗量+20%，效果持续20秒(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1106(char={}, mode=0, text=False, part=''):
    if text:
        return "施放技能时，消耗当前HP的30%，伤害增加 2223，技能攻击力 +6%，效果持续30秒(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1107(char={}, mode=0, text=False, part=''):
    if text:
        return "施放技能时，有10%的几率随机初始技能冷却时间20秒以内的技能(冷却时间20秒,觉醒除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1121(char={}, mode=0, text=False, part=''):
    if text:
        return "使用技能指令施放非快捷栏中的技能时，该技能冷却时间 -15%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1122(char={}, mode=0, text=False, part=''):
    if text:
        return "使用技能指令施放快捷栏中的技能时，该技能攻击力 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1123(char={}, mode=0, text=False, part=''):
    if text:
        return "使用消耗品时，自身进入消耗品无法解除的中毒状态, 自身处于中毒状态时，技能冷却时间恢复速度 +25%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1124(char={}, mode=0, text=False, part=''):
    if text:
        return "受到惊吓时，攻击速度 +20%，移动速度 +20%，施放速度 +30%，效果持续30秒(最多叠加 1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1125(char={}, mode=0, text=False, part=''):
    if text:
        return "受到异常状态影响时，移除异常状态(冷却时间100 秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1126(char={}, mode=0, text=False, part=''):
    if text:
        return "受到总HP20%以上的伤害时，所受伤害 -25%，效果持续10秒(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1127(char={}, mode=0, text=False, part=''):
    if text:
        return "受到总HP20%以上的伤害时，自身进入眩晕状态(冷却时间3秒),  自身进入眩晕状态时，技能冷却时间恢复速度 +20%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1128(char={}, mode=0, text=False, part=''):
    if text:
        return "受到总HP25%以上的伤害时，使300px范围内敌人进入眩晕状态(冷却时间20秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1129(char={}, mode=0, text=False, part=''):
    if text:
        return "受到总HP25%以上的伤害时，生成相当于HP最大值25%的保护罩，持续20秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1130(char={}, mode=0, text=False, part=''):
    if text:
        return "受到总HP25%以上的伤害时，自身进入石化状态(冷却时间20秒), 自身进入石化状态时，技能剩余冷却时间 -5%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1131(char={}, mode=0, text=False, part=''):
    if text:
        return "受到总HP25%以上的伤害时，自身进入睡眠状态(冷却时间30秒), 自身进入睡眠状态时，技能、消耗品的HP恢复效果 +50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1132(char={}, mode=0, text=False, part=''):
    if text:
        return "受身蹲伏蹲坐下时，最大无敌时间 +1秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1133(char={}, mode=0, text=False, part=''):
    if text:
        return "受身蹲伏结束时，伤害增加 2519，效果持续60秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1134(char={}, mode=0, text=False, part=''):
    if text:
        return "受身蹲伏状态下按方向键，隐藏在暗影中移动，持续2秒(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1135(char={}, mode=0, text=False, part=''):
    if text:
        return "输入技能指令施放的技能攻击力 +5%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1136(char={}, mode=0, text=False, part=''):
    if text:
        return "输入技能指令施放技能时，所有速度 +5%，效果持续3秒(最多叠加3次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1137(char={}, mode=0, text=False, part=''):
    if text:
        return "输入技能指令施放技能时，根据输入方向键的个数，增加技能攻击力(觉醒技能除外), - 输入1个方向键：技能攻击力 +7%, - 输入2个方向键：技能攻击力 +9%, - 输入3个方向键：技能攻击力 +11%, - 输入4个方向键：技能攻击力 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1139(char={}, mode=0, text=False, part=''):
    if text:
        return "睡眠抗性 -50%, 所有异常状态抗性 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1140(char={}, mode=0, text=False, part=''):
    if text:
        return "死亡时，角色会哭泣, 复活后，攻击速度 +30%，施放速度 +45%，移动速度 +30%，效果持续30秒(冷却60秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1141(char={}, mode=0, text=False, part=''):
    if text:
        return "所有被击伤害的50%转化为中毒伤害, 攻击中毒状态敌人时，技能攻击力 +2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1142(char={}, mode=0, text=False, part=''):
    if text:
        return "所有被击伤害的50%转化为灼烧伤害, 攻击灼烧状态敌人时，技能攻击力 +2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1143(char={}, mode=0, text=False, part=''):
    if text:
        return "所有被击伤害的50%转换为出血伤害, 攻击出血状态敌人时，技能攻击力 +2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1144(char={}, mode=0, text=False, part=''):
    if text:
        return "所有被击伤害的50%转换为感电伤害, 攻击感电状态敌人时，技能攻击力 +2%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1145(char={}, mode=0, text=False, part=''):
    if text:
        return "所有异常状态抗性 +15%, HP MAX -300"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1146(char={}, mode=0, text=False, part=''):
    if text:
        return "所有异常状态抗性 +25%, 移动速度 -5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1147(char={}, mode=0, text=False, part=''):
    if text:
        return "所有职业Lv1-30技能攻击力 +12%, 不消耗无色小晶块的技能变为消耗2个无色小晶块"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1148(char={}, mode=0, text=False, part=''):
    if text:
        return "所有属性抗性之和小于100时，所有属性强化 +30"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1149(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃Lv+5, 跳跃时，进入霸体状态，持续30秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1150(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃攻击时，立即落地，生成冲击波(冷却时间5秒), 每100px角色高度，冲击波伤害增加2倍(最多增加至300px)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1151(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃力 +100, 跳跃期间，按拍卖行键，立即开始落地，增加落地速度(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1152(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃力 +50, 跳跃时，回避率 +3%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1153(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃落地时，掉落一个西瓜，赋予武器冰属性攻击，冰属性抗性 +10，移动速度 +10%，效果持续20秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1154(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃期间，可再次跳跃"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1155(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃期间进入霸体状态(落地时解除霸体状态)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1156(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃时，进入霸体状态"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1157(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃时，有1%的几率移除自身的异常状态(冷却时间60秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1158(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃时按跳跃键(C)0.5秒，维持5秒飞行状态，获得以下效果(冷却时间30秒),  - 飞行中再次按方向键可空中前冲(最多2次),  - 飞行中进入霸体状态"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1159(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃时所受伤害 -15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1160(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃状态下，[装备属性操作键]输入时，10秒内，乘坐旋风，可浮空移动(冷却时间40秒), - 旋风之力可吸附周围敌人, - 浮空状态下进入霸体状态"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1161(char={}, mode=0, text=False, part=''):
    if text:
        return "跳跃状态下，攻击速度 +10%，施放速度 +15%，移动速度 -10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1162(char={}, mode=0, text=False, part=''):
    if text:
        return "停留时，每0.5秒，伤害增加 445(最多叠加10次，移动时每秒减少1层叠加效果)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1163(char={}, mode=0, text=False, part=''):
    if text:
        return "伪装Buff期间，增加45%的回避率，被击时所受伤害 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1164(char={}, mode=0, text=False, part=''):
    if text:
        return "武器耐久度减少率 +100%, 技能攻击力 +6%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1165(char={}, mode=0, text=False, part=''):
    if text:
        return "物理防御力 +2000, 魔法防御力 -500"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1166(char={}, mode=0, text=False, part=''):
    if text:
        return "物理防御力 -21000, 魔法防御力 -21000, 技能冷却时间 -10%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1167(char={}, mode=0, text=False, part=''):
    if text:
        return "物品栏负重上限 +2kg, HP MAX +300"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1168(char={}, mode=0, text=False, part=''):
    if text:
        return "物品栏负重上限 +3kg, MP MAX +500"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1169(char={}, mode=0, text=False, part=''):
    if text:
        return "向地图最强敌人生成标志，500px范围内存在标志敌人时，施放后跳，可移动至标志敌人后方(冷却时间20秒), 背击标志敌人时，技能攻击力 +8%，效果持续5秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1170(char={}, mode=0, text=False, part=''):
    if text:
        return "消耗品、装备的MP恢复效果 +10%, 每分钟HP/MP恢复量固定为0"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1171(char={}, mode=0, text=False, part=''):
    if text:
        return "消耗品的MP恢复效果 +50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1172(char={}, mode=0, text=False, part=''):
    if text:
        return "消耗品恢复HP时，被击伤害 -20%，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1173(char={}, mode=0, text=False, part=''):
    if text:
        return "消耗品恢复MP时，伤害增加 2519，效果持续30秒(最多叠加1次), 消耗品的MP恢复效果 +80%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1174(char={}, mode=0, text=False, part=''):
    if text:
        return "消耗无色小晶块的技能攻击力 +8%, 消耗无色小晶块的技能无色小晶块消耗量 +2"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1176(char={}, mode=0, text=False, part=''):
    if text:
        return "眩晕解除时，伤害增加 3853，效果持续30秒(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1177(char={}, mode=0, text=False, part=''):
    if text:
        return "移动速度在100%以上时，Lv30技能范围 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1178(char={}, mode=0, text=False, part=''):
    if text:
        return "用以下技能准确阻挡敌人攻击时，技能攻击力 +30%，持续2秒，仅限1次, -格挡、招架、格挡反击、武器格挡、盾牌格挡、圣盾、远程格挡(施放该技能后，0.5秒以内阻挡攻击，即视为准确阻挡)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1179(char={}, mode=0, text=False, part=''):
    if text:
        return "用以下技能准确阻挡敌人攻击时，强制控制2秒, -格挡、招架、格挡反击、武器格挡、盾牌格挡、圣盾、远程格挡(施放该技能后，0.5秒以内阻挡攻击，即视为准确阻挡)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1180(char={}, mode=0, text=False, part=''):
    if text:
        return "渔夫的祝福激活时，所有异常状态抗性 +20%，回避率 +5%，效果持续30秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1182(char={}, mode=0, text=False, part=''):
    if text:
        return "云朵存在时，赋予武器冰属性攻击和暗属性攻击"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1183(char={}, mode=0, text=False, part=''):
    if text:
        return "增加相当于技能MP消耗量词条总和5%的技能攻击力(最高增加25%), 技能MP消耗量 +100%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1184(char={}, mode=0, text=False, part=''):
    if text:
        return "站立、行走、冲刺状态下输入[装备指令键]，触发缩小效果，持续25秒, - 角色大小 -50%, - 回避率 +75%, - 移动速度 +30%, - 无法使用基础攻击与技能, - 每秒恢复1%的HP、MP, - 持续时间内再次输入[装备指令键]或者进入无法行动状态、死亡状态、强制发动技能状态时，效果解除, - [装备指令键]解除效果仅可在站立、行走、冲刺状态下触发"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1185(char={}, mode=0, text=False, part=''):
    if text:
        return "中毒抗性 +1%, 魔法防御力 +500"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1186(char={}, mode=0, text=False, part=''):
    if text:
        return "中毒伤害 +15%, 中毒抗性 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1187(char={}, mode=0, text=False, part=''):
    if text:
        return "中毒伤害 +10%, 中毒抗性 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1188(char={}, mode=0, text=False, part=''):
    if text:
        return "中毒伤害 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1189(char={}, mode=0, text=False, part=''):
    if text:
        return "250px范围内存在敌人时，每秒恢复100点HP"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1190(char={}, mode=0, text=False, part=''):
    if text:
        return "周围有草坪时，所有属性抗性 +20，所有异常状态抗性 +10%，命中率 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1191(char={}, mode=0, text=False, part=''):
    if text:
        return "装扮背包中的装扮个数在120个以上：触发聚光灯，进入霸体状态，技能冷却时间 -8%(觉醒除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1192(char={}, mode=0, text=False, part=''):
    if text:
        return "装备的HP恢复效果 +10%, 被击时所受伤害 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1193(char={}, mode=0, text=False, part=''):
    if text:
        return "装备的HP恢复效果 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1194(char={}, mode=0, text=False, part=''):
    if text:
        return "装备的MP恢复效果 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1195(char={}, mode=0, text=False, part=''):
    if text:
        return "装备时，每20秒，使250px范围内的敌人进入诅咒状态, 前冲期间，诅咒使用范围逐渐增加，每秒减少0.5%的HP(该效果不会使HP减少到1%以下), 非前冲时，诅咒范围逐渐缩小"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1196(char={}, mode=0, text=False, part=''):
    if text:
        return "装备时，生成火属性Buff，持续20秒, - 火属性Buff持续期间，赋予火属性攻击, - 被冰属性攻击时，火属性Buff解除，持续20秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1197(char={}, mode=0, text=False, part=''):
    if text:
        return "装备时，自身进入消耗品无法解除的出血状态, 出血状态每减少1100点HP，伤害增加 326(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1198(char={}, mode=0, text=False, part=''):
    if text:
        return "灼烧伤害 +15%, 灼烧抗性 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1199(char={}, mode=0, text=False, part=''):
    if text:
        return "灼烧伤害 +20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1200(char={}, mode=0, text=False, part=''):
    if text:
        return "灼烧抗性 +3%, 冰冻抗性 -1.5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1201(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于冰冻状态时，被击伤害 -30%，5秒内恢复20%的HP(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1202(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于出血状态时，出血伤害 +10%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1203(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于出血状态时，攻击速度、移动速度 +20%，施放速度 +30%,  出血抗性 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1204(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于出血状态时，伤害增加 2223, 自身处于出血状态时，每1秒，减少3%的攻击速度、移动速度、施放速度(最多叠加5次，解除出血状态时效果解除), 出血伤害 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1205(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于出血状态时，物理、魔法暴击率 +10%，攻击速度 +5%，施放速度 +7.5%, 被击时，自身进入出血状态(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1206(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于出血状态时进行10次攻击，10秒内恢复15%的HP(冷却时间10秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1207(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于出血状态时进行攻击，使敌人进入出血状态(冷却时间8秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1208(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于感电状态时，物理、魔法暴击率 +10%，攻击速度 +5%，施放速度 +7.5%, 被击时，自身进入感电状态(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1209(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于石化状态时，被击伤害-30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1210(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于石化状态时被击，使500px范围内所有敌人进入石化状态(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1211(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于睡眠状态时被击，不会解除睡眠状态, 自身处于睡眠状态时被击，恢复15%的HP(冷却时间1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1212(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于中毒状态时，物理、魔法暴击率 +10%，攻击速度 +5%，施放速度 +7.5%, 被击时，自身进入中毒状态(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1213(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于中毒状态时进行攻击，使敌人进入中毒状态(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1214(char={}, mode=0, text=False, part=''):
    if text:
        return "自身处于灼烧状态时，物理、魔法暴击率 +10%，攻击速度 +5%、施放速度 +7.5%, 被击时，自身进入灼烧状态(冷却时间5秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1215(char={}, mode=0, text=False, part=''):
    if text:
        return "自身的异常个数达到1个以上时，Lv45以下技能冷却时间恢复速度 +50%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1216(char={}, mode=0, text=False, part=''):
    if text:
        return "自身的异常个数达到3个以上时，Lv60以上技能冷却时间恢复速度 +50%(觉醒除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1217(char={}, mode=0, text=False, part=''):
    if text:
        return "自身感电时，攻击、移动速度 +20%，施放速度 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1218(char={}, mode=0, text=False, part=''):
    if text:
        return "自身攻击每次对领主造成HP10%的伤害时，伤害增加 593，物理、魔法防御力 -10%(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1219(char={}, mode=0, text=False, part=''):
    if text:
        return "自身获得2个以上消耗品效果时，自身进入出血状态，效果持续10秒(冷却时间10秒), 自身处于出血状态时，技能冷却时间恢复速度 +10%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1220(char={}, mode=0, text=False, part=''):
    if text:
        return "自身仅中毒异常状态时，每10秒随机适用下列效果中1个, - 所有速度 +30%, - 技能攻击力 +10%, - 技能冷却时间恢复速度 +30%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1221(char={}, mode=0, text=False, part=''):
    if text:
        return "自身每处于一种异常状态，被击伤害 -5%(最多减少30%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1222(char={}, mode=0, text=False, part=''):
    if text:
        return "自身每处于灼烧状态1秒，所有属性强化 +3，持续15秒(最多叠加10次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1223(char={}, mode=0, text=False, part=''):
    if text:
        return "自身命中率超过50%以上时，Lv1~25技能Lv+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1224(char={}, mode=0, text=False, part=''):
    if text:
        return "自身使敌人进入的冰冻状态无法被灼烧解除, 攻击冰冻状态敌人时，技能攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1225(char={}, mode=0, text=False, part=''):
    if text:
        return "自身使敌人进入灼烧状态解除敌人冰冻状态时，敌人受到的灼烧伤害 +30%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1226(char={}, mode=0, text=False, part=''):
    if text:
        return "自身受到的非破招攻击伤害 +20%, 自身受到的破招攻击伤害 -15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1227(char={}, mode=0, text=False, part=''):
    if text:
        return "自身睡眠时，无法使用消耗品，10秒内获得无敌Buff(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1228(char={}, mode=0, text=False, part=''):
    if text:
        return "自身受到超过最大HP15%以上的伤害时，使500px范围内的所有敌人进入石化状态(冷却时间30秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1229(char={}, mode=0, text=False, part=''):
    if text:
        return "自身所受睡眠状态持续时间 -50%, 睡眠抗性 -20%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1230(char={}, mode=0, text=False, part=''):
    if text:
        return "自身移动速度超过80%以上时，Lv1~25技能Lv+1"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1231(char={}, mode=0, text=False, part=''):
    if text:
        return "诅咒抗性 +25%, 所有异常状态抗性 -5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1232(char={}, mode=0, text=False, part=''):
    if text:
        return "最后一次赋予敌人的无力化异常状态（不包括出血、感电、中毒、灼烧）作为敌人下一次无力化的弱点属性"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1237(char={}, mode=0, text=False, part=''):
    if text:
        return ", 该装备的成长属性等级之和达到240，增加1%的技能攻击力,  - 该装备的成长属性等级之和每增加40级，额外增加1%的技能攻击力,  - 穿戴100级以下装备时不适用该效果"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1239(char={}, mode=0, text=False, part=''):
    if text:
        return "装备提供的异常状态抗性总和超过5%以上时，增加相同数值的异常伤害(最多增加10%，适用于所有场景)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1240(char={}, mode=0, text=False, part=''):
    if text:
        return "穿戴装备的强化/增幅数值总和每增加6，攻击强化 272(最多叠加24次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1241(char={}, mode=0, text=False, part=''):
    if text:
        return "穿戴装备的强化/增幅数值总和每增加1，所有速度 +2%(最多叠加12次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1243(char={}, mode=0, text=False, part=''):
    if text:
        return "地下城入场时，攻击强化 2223, 连击维持时间 -0.5秒"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1245(char={}, mode=0, text=False, part=''):
    if text:
        return "物理伤害减少率和魔法伤害减少率总和超过60%以上时，技能冷却时间恢复速度 +15%(觉醒技能除外)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1246(char={}, mode=0, text=False, part=''):
    if text:
        return "物品提供的攻击速度增加量总和超过140%以上时，技能攻击力 +30%, 被击时，所受伤害 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1247(char={}, mode=0, text=False, part=''):
    if text:
        return "技能MP消耗量 -50%, 被击时，所受伤害 +15%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1248(char={}, mode=0, text=False, part=''):
    if text:
        return "生成最大HP45%的自动充能保护罩，保护罩存在状态下10秒不被攻击时充能到最大值, 装备时，适用55%的HP(装备解除前，当前HP无法超过HP最大值的55%)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1249(char={}, mode=0, text=False, part=''):
    if text:
        return "HP在40%以下时，物理、魔法防御力 +14000，攻击强化 2816"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1250(char={}, mode=0, text=False, part=''):
    if text:
        return "最高属性强化每增加50，技能冷却时间恢复速度 +4%(最多叠加6次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1251(char={}, mode=0, text=False, part=''):
    if text:
        return "最高属性强化每增加50，所有速度 +3%(最多叠加5次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1252(char={}, mode=0, text=False, part=''):
    if text:
        return "根据最高属性强化数值适用以下效果：, - 200~249: 攻击强化 1037, - 250~299: 攻击强化 1927, - 300~： 攻击强化 2816，技能攻击力 +7%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1253(char={}, mode=0, text=False, part=''):
    if text:
        return "最高属性抗性超过75以上时，攻击强化 700"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1254(char={}, mode=0, text=False, part=''):
    if text:
        return "根据穿戴的所有装备的品级百分比总和适用以下效果：, - 800%以上：移动速度 +10%, - 900%以上：攻击速度 +10%，施放速度 +15%, - 1000%以上：物理、魔法暴击率 +10%, - 1150%以上：技能攻击力 +5%"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1255(char={}, mode=0, text=False, part=''):
    if text:
        return "根据装备的品级百分比适用以下效果：, - 90%以下: 攻击强化 445, - 90%~95%: 攻击强化 1186, - 95%以上: 攻击强化 3557"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1256(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，适用的属性攻击对应的属性抗性每增加10，相应的属性强化 +10，效果持续30秒(最多增加40，冷却时间1秒)"
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1257(char={}, mode=0, text=False, part=''):
    if text:
        return "攻击时，使用的属性攻击对应的属性抗性 +10(最多叠加1次)"
    if mode == 0:
        pass
    if mode == 1:
        pass


# 目前成长词条范围
for i in range(1260):
    try:
        if i not in entry_func_list.keys():
            entry_func_list[i] = [eval('entry_{}'.format(i))]
    except:
        pass


def entry_10001(char={}, mode=0, text=False, part=''):
    if text:
        return "成长属性240级以上时增加1%技能攻击，每40级增加1%"
    if mode == 0:
        x = sum(char.词条等级.get(part, [0]))
        if x >= 240:  # 判断是否穿戴神话装备
            char.技能攻击力加成(0.01 * int((x - 200) / 40))
    if mode == 1:
        pass


def entry_10002(char={}, mode=0, text=False, part=''):
    if text:
        return "(上衣)技能攻击力 +12%"
    if mode == 0:
        char.技能攻击力加成(0.12)
    if mode == 1:
        pass


def entry_10003(char={}, mode=0, text=False, part=''):
    if text:
        return "(下装)技能攻击力 +12%"
    if mode == 0:
        char.技能攻击力加成(0.12)
    if mode == 1:
        pass


def entry_10004(char={}, mode=0, text=False, part=''):
    if text:
        return "(头肩)技能攻击力 +34%"
    if mode == 0:
        char.技能攻击力加成(0.34)
    if mode == 1:
        pass


def entry_10005(char={}, mode=0, text=False, part=''):
    if text:
        return "(腰带)技能攻击力 +12%"
    if mode == 0:
        char.技能攻击力加成(0.12)
    if mode == 1:
        pass


def entry_10006(char={}, mode=0, text=False, part=''):
    if text:
        return "(鞋)技能攻击力 +29%， 移动速度 +4%"
    if mode == 0:
        char.技能攻击力加成(0.29)
        char.移动速度增加(0.04)
    if mode == 1:
        pass


def entry_10007(char={}, mode=0, text=False, part=''):
    if text:
        return "(手镯)技能攻击力 +12%"
    if mode == 0:
        char.技能攻击力加成(0.12)
    if mode == 1:
        pass


def entry_10008(char={}, mode=0, text=False, part=''):
    if text:
        return "(项链)技能攻击力 +12%"
    if mode == 0:
        char.技能攻击力加成(0.12)
    if mode == 1:
        pass


def entry_10009(char={}, mode=0, text=False, part=''):
    if text:
        return "(戒指)技能攻击力 +12%"
    if mode == 0:
        char.技能攻击力加成(0.12)
    if mode == 1:
        pass


def entry_10010(char={}, mode=0, text=False, part=''):
    if text:
        return "(辅助装备)技能攻击力 +12%"
    if mode == 0:
        char.技能攻击力加成(0.12)
    if mode == 1:
        pass


def entry_10011(char={}, mode=0, text=False, part=''):
    if text:
        return "(魔法石)技能攻击力 +12%"
    if mode == 0:
        char.技能攻击力加成(0.12)
    if mode == 1:
        pass


def entry_10012(char={}, mode=0, text=False, part=''):
    if text:
        return "(耳环)技能攻击力 +12%"
    if mode == 0:
        char.技能攻击力加成(0.12)
    if mode == 1:
        pass


def entry_10013(char={}, mode=0, text=False, part=''):
    if text:
        return "(胜负武器)技能攻击力 +50%"
    if mode == 0:
        char.技能攻击力加成(0.50)
    if mode == 1:
        pass


def entry_10014(char={}, mode=0, text=False, part=''):
    if text:
        return "(吞噬武器)技能攻击力 +35%"
    if mode == 0:
        char.技能攻击力加成(0.35)
    if mode == 1:
        pass


# 部位固有属性
for i in range(10001, 10015):
    try:
        if i not in entry_func_list.keys():
            entry_func_list[i] = [eval('entry_{}'.format(i))]
    except:
        pass

# 词条效果id范围 0~18999
