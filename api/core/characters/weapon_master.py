
from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能

class 剑魂主动技能(主动技能):
    hit数 = 0  # 太刀时所需参数，计算期望刺伤

    def 额外刺伤层数(self, 武器类型):
        return 0

    def 穿云刺数量(self, 武器类型):
        return 0


class 剑魂流系技能(主动技能):
    hit数 = 0

    def 武器CD系数(self, 武器类型, 输出类型):
        return 1.0  #流系列技能不受武器CD影响

    def 额外刺伤层数(self, 武器类型):
        return 0

    def 穿云刺数量(self, 武器类型):
        return 0


class 技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    学习间隔 = 1
    等级精通 = 110
    关联技能 = ['里鬼剑术', '空中连斩']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

class 技能1(剑魂主动技能):
    hit数 = 8
    名称 = '里鬼剑术'
    所在等级 = 15
    等级上限 = 11
    学习间隔 = 15
    等级精通 = 1
    CD = 1.0
    TP成长 = 0.1
    TP上限 = 3
    data0 = [(1 + i / 1000) for i in [0, 0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870]]

    百分比 = {'短剑': 1004.68*1.085, 
             '光剑': 890.19*1.085,
             '巨剑': 1241.95*1.085, 
             '钝器': 1225.24*1.085, 
             '太刀': 1197.49*1.085}
    # 巨剑不蓄力441.19

    穿云刺 = {'短剑': 3, '光剑': 3, '巨剑': 2, '钝器': 4, '太刀': 4}

    MP = [6, 140]

    def 等效百分比(self, **argv):
        武器类型 = argv.get('武器类型', '光剑')
        hit0 = self.百分比[武器类型]
        return super().等效百分比(**argv)

    def 穿云刺数量(self, 武器类型):
        return self.穿云刺[武器类型]


class 技能2(被动技能):
    名称 = '武器奥义'
    所在等级 = 15
    等级上限 = 30
    学习间隔 = 3
    等级精通 = 20
    关联技能 = ['无']

class 技能3(被动技能):
    名称 = '光剑掌握'
    所在等级 = 15
    等级上限 = 20
    学习间隔 = 3
    等级精通 = 10
    关联技能 = ['无']
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['极鬼剑术暴风式','万剑归宗(终结)','万剑归宗(穿云刺)','万剑极诣开天斩']

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '光剑':
            return 1.0
        else:
            return round(1.0 - 0.01 * self.等级, 5)


class 技能4(剑魂主动技能):
    名称 = '流心狂'
    所在等级 = 30
    等级上限 = 20
    学习间隔 = 3
    等级精通 = 10
    是否有伤害 = 0
    MP = [20, 168]
    关联技能 = ['流心刺', '流心跃', '流心升']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.20 + 0.02 * self.等级, 5)


class 技能5(被动技能):
    名称 = '无我剑气'
    所在等级 = 20
    等级上限 = 15
    学习间隔 = 3
    等级精通 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'weapon_master'
        self.名称 = '极诣·剑魂'
        self.角色 = '鬼剑士(男)'
        self.类型 = '输出'
        self.职业 = '剑魂'
        self.武器选项 = ['光剑', '太刀', '钝器', '巨剑', '短剑']
        self.输出类型选项 = ['物理百分比']
        self.防具精通属性 = ['力量']
        self.类型 = '物理百分比'
        self.武器类型 = '光剑'
        self.防具类型 = '轻甲'
        技能列表 = []
        技能序号 = {}
        i = 0
        while i >= 0:
            try:
                tem = eval('技能'+str(i)+'()')
                tem.基础等级计算()
                技能序号[tem.名称] = i
                技能列表.append(tem)
                i += 1
            except:
                i = -1
        self.技能栏 = 技能列表
        self.技能序号 = 技能序号
        self.buff = 1.82

        super().__init__()
