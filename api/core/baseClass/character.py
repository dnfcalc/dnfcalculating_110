from cgitb import text
from pickle import TRUE
from unittest import result
from core.baseClass.skill import 技能
from core.baseClass.equipment import equ
from core.store import store
from core.equipment.基础函数 import 基础属性输入, 刀魂之卡赞数据, 部位列表, 精通计算, 增幅计算, 耳环计算, 左右计算


class Detail:
    基础力量 = 0
    基础智力 = 0
    基础体力 = 0
    基础精神 = 0

    力量 = 0
    智力 = 0
    体力 = 0
    精神 = 0

    进图力量 = 0.0
    进图智力 = 0.0
    进图体力 = 0.0
    进图精神 = 0.0

    系统奶系数 = 0
    系统奶基数 = 0
    年宠技能 = False
    白兔子技能 = False
    斗神之吼秘药 = False

    物理攻击力 = 65
    魔法攻击力 = 65
    独立攻击力 = 1045
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    进图物理攻击力 = 0
    进图魔法攻击力 = 0
    进图独立攻击力 = 0
    进图属强 = 0

    # 旧词条
    百分比力智 = 0.0
    百分比三攻 = 0.0
    伤害增加 = 0.0
    附加伤害 = 0.0
    属性附加 = 0.0
    暴击伤害 = 0.0
    最终伤害 = 0.0
    技能攻击力 = 1.0
    技能攻击力累加 = 0.0
    持续伤害 = 0.0
    加算冷却缩减 = 0.0
    百分比减防 = 0.0
    固定减防 = 0

    攻击速度 = 0.00
    移动速度 = 0.00
    施放速度 = 0.00
    命中率 = 0.0
    回避率 = 0.0
    物理暴击率 = 0.00
    魔法暴击率 = 0.00

    # 根据前端传入初始化技能类
    技能类 = []
    #

    def __init__(self, 角色, 职业):
        基础属性输入(self, 角色, 职业)

    def 站街力量(self):
        return int(self.力量)

    def 站街智力(self):
        return int(self.智力)

    def 面板力量(self):
        return (self.力量 + int((self.力量 - self.基础力量) * self.系统奶系数 + self.系统奶基数)
                + self.进图力量) * (1 + self.百分比力智)

    def 面板智力(self):
        return (self.智力 + int((self.智力 - self.基础智力) * self.系统奶系数 + self.系统奶基数)
                + self.进图智力) * (1 + self.百分比力智)


class Character:
    alter = ''
    # 实际名称
    name = ''
    # 角色
    character: str = ''
    # 输出/奶
    characterType = ''
    # 转职
    classChange = ''
    # 武器类型

    weaponType = []
    # 输出类型选择，默认类型为第一个
    carry_type_list = []
    # 防具类型
    armor = ''
    # 防具类型精通，智力、力量
    armor_mastery = []
    # buff倍率
    buff_ratio = 1.0
    # 技能列表
    skillInfo = []
    # 个性化设置，技能选项等
    individuation = []
    # 护石及符文信息
    talisman = []
    # 符文信息
    rune = []
    # 药剂等相关信息设置
    # 白金列表
    platinum = []
    # 时装列表
    clothes = []
    clothes_bottom = ['远古记忆', '受身蹲伏']
    # 辟邪玉属性
    附加伤害增加增幅 = 1.0
    属性附加伤害增加增幅 = 1.0
    技能伤害增加增幅 = 1.0
    暴击伤害增加增幅 = 1.0
    伤害增加增幅 = 1.0
    最终伤害增加增幅 = 1.0
    力量智力增加增幅 = 1.0
    物理魔法攻击力增加增幅 = 1.0
    所有属性强化增加 = 1.0

    等级 = 110
    防御输入 = 506109
    火抗输入 = 0
    冰抗输入 = 0
    光抗输入 = 0
    暗抗输入 = 0
    状态 = 0  # 0站街 1图内
    类型 = ''
    武器类型 = ''
    防具类型 = ''
    技能栏 = []
    技能序号 = {}
    远古记忆 = -1
    刀魂之卡赞 = -1
    防具精通属性 = []

    # 打造属性

    # 装备触发选择

    def __init__(self) -> None:
        print("初始化Char")
        self.skillInfo = []
        self.rune = []
        self.talisman = []
        self.platinum = []
        self.clothes = []
        self.clothes_bottom = []

    def set_skill_info(self, skillClassList: 技能, rune_except=[], clothes=[], clothes_bottom=[]):
        """
        设置返回前端的技能信息
        """
        self.skillInfo = []
        self.rune = []
        self.talisman = []
        self.platinum = []
        self.clothes = []
        for skill in skillClassList:
            skill.等级 = skill.基础等级
            self.skillInfo.append({
                "name": skill.名称,
                "type": skill.是否有伤害,
                "need_level": skill.所在等级,
                "level_master": skill.等级精通,
                "level_max": skill.等级上限,
                "CD": 0 if not skill.是否有伤害 else skill.CD,
                "current_LV": skill.基础等级,
                "data": 0 if not skill.是否有伤害 else skill.等效百分比(''),
                "TP_max": skill.TP上限 if skill.是否有伤害 else None,
                "TP_Lv": skill.TP等级 if skill.是否有伤害 else None
            })
            # 护石
            if skill.是否有伤害 == 1 and skill.是否有护石 == 1:
                self.talisman.append(skill.名称)
            # 符文
            if skill.所在等级 >= 20 and skill.所在等级 <= 80 and skill.所在等级 != 50 and skill.是否有伤害 == 1 and skill.名称 not in rune_except:
                self.rune.append(skill.名称)
            # 白金
            if skill.所在等级 <= 70 and skill.所在等级 not in [48, 50]:
                self.platinum.append(skill.名称)
            # 时装
            if skill.所在等级 <= 95:
                self.clothes.append(skill.名称)
        if len(clothes) > 0:
            self.clothes = clothes
        if len(clothes_bottom) > 0:
            self.clothes_bottom = clothes_bottom

    def set_platinum_list(self):
        pass

    def set_shizhuang_info(self):
        pass

    def set_individuation(self):
        pass

    def get_skill_by_name(self, name):
        return self.技能栏[self.技能序号.get(name, 0)]

    # region 词条属性
    def 附加伤害加成(self, x, 辟邪玉加成=1):
        self.detail.附加伤害 += self.附加伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 三攻固定加成(self, x=0, y=0, z=0):
        if y == 0 or z == 0:
            y = x
            z = x
        self.detail.物理攻击力 += x
        self.detail.魔法攻击力 += y
        self.detail.独立攻击力 += z

    def 力智固定加成(self, x=0, y=0):
        if y == 0:
            y = x
        self.detail.力量 += x
        self.detail.智力 += y

    def 持续伤害加成(self, x):
        self.detail.持续伤害 += x

    def 属性附加加成(self, x):
        self.detail.属性附加 += self.属性附加伤害增加增幅 * x

    def 技能攻击力加成(self, x, 辟邪玉加成=1, 适用累加=1):
        if 适用累加 == 0:
            self.detail.技能攻击力 *= 1 + self.技能伤害增加增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.detail.技能攻击力累加 += x
            if self.detail.技能攻击力累加 <= 2:
                self.detail.技能攻击力 *= 1 + self.技能伤害增加增幅 * x if 辟邪玉加成 == 1 else x
            else:
                self.detail.技能攻击力 *= 1 + (self.技能伤害增加增幅*(2+x-self.detail.技能攻击力累加) +
                                          self.detail.技能攻击力累加-2) if self.detail.技能攻击力累加 - x < 2 or 辟邪玉加成 == 1 else x

    def 暴击伤害加成(self, x, 辟邪玉加成=1):
        self.detail.暴击伤害 += self.暴击伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 伤害增加加成(self, x, 辟邪玉加成=1):
        self.detail.伤害增加 += self.伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 最终伤害加成(self, x, 辟邪玉加成=1):
        self.detail.最终伤害 += self.最终伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 百分比力智加成(self, x, 辟邪玉加成=1):
        self.detail.百分比力智 += self.力量智力增加增幅 * x if 辟邪玉加成 == 1 else x

    def 百分比三攻加成(self, x, 辟邪玉加成=1):
        self.detail.百分比三攻 += self.物理魔法攻击力增加增幅 * x if 辟邪玉加成 == 1 else x

    def 火属性强化加成(self, x, 辟邪玉加成=1):
        if self.状态 == 0:
            self.detail.火属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
        else:
            self.detail.火属性强化 += int(self.所有属性强化增加 * x)

    def 冰属性强化加成(self, x, 辟邪玉加成=1):
        if self.状态 == 0:
            self.detail.冰属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
        else:
            self.detail.冰属性强化 += int(self.所有属性强化增加 * x)

    def 光属性强化加成(self, x, 辟邪玉加成=1):
        if self.状态 == 0:
            self.detail.光属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
        else:
            self.detail.光属性强化 += int(self.所有属性强化增加 * x)

    def 暗属性强化加成(self, x, 辟邪玉加成=1):
        if self.状态 == 0:
            self.detail.暗属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
        else:
            self.detail.暗属性强化 += int(self.所有属性强化增加 * x)

    def 所有属性强化加成(self, x, 辟邪玉加成=1):
        if self.状态 == 0:
            temp = self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
        else:
            temp = int(self.所有属性强化增加 * x)
        self.所有属性强化(temp)

    def 攻击速度增加(self, x):
        self.detail.攻击速度 += x

    def 移动速度增加(self, x):
        self.detail.移动速度 += x

    def 施放速度增加(self, x):
        self.detail.施放速度 += x

    def 命中率增加(self, x):
        self.detail.命中率 += x

    def 物理暴击率增加(self, x):
        self.detail.物理暴击率 += x

    def 魔法暴击率增加(self, x):
        self.detail.魔法暴击率 += x

    def 技能等级加成(self, 加成类型, minLv, maxLv, lv):
        lv = int(lv)
        if self.远古记忆 > 0:
            if minLv <= 15 and maxLv >= 15:
                self.远古记忆 = min(20, self.远古记忆 + lv)
        if self.刀魂之卡赞 > 0:
            if minLv <= 5 and maxLv >= 5:
                self.刀魂之卡赞 = min(20, self.刀魂之卡赞 + lv)
        for i in self.技能栏:
            if i.所在等级 >= minLv and i.所在等级 <= maxLv:
                if 加成类型 == '所有':
                    i.等级加成(lv)
                else:
                    if i.是否主动 == 1:
                        i.等级加成(lv)

    def 武器装扮等级加成(self, Lv, lv):
        lv = int(lv)
        for i in self.技能栏:
            if i.所在等级 == Lv and i.是否主动 == 1 and i.名称 not in [
                    "念兽龙虎啸", "风雷啸", "圣灵符文", "神圣之光"
            ]:
                i.等级加成(lv)

    def 技能冷却缩减(self, min, max, x):
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max:
                if i.是否有伤害 == 1:
                    i.CD *= (1 - x)

    def 技能恢复加成(self, min, max, x):
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max:
                if i.是否有伤害 == 1:
                    i.恢复 += x

    def 进图属强加成(self, x, 辟邪玉加成=1):
        self.detail.进图属强 += int(self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x)

    def 技能倍率加成(self, lv, x):
        for i in self.技能栏:
            if i.所在等级 == lv:
                if i.是否有伤害 == 1:
                    i.倍率 *= (1 + x * self.技能伤害增加增幅)

    def 单技能修改(self, 名称, 倍率, CD):
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                if i.名称 == 名称:
                    i.倍率 *= 倍率
                    i.CD *= CD

    def 所有属性强化(self, x):
        self.detail.火属性强化 += x
        self.detail.冰属性强化 += x
        self.detail.光属性强化 += x
        self.detail.暗属性强化 += x

    # endregion

    # region 面板相关函数
    def 站街物理攻击力倍率(self):
        站街物理攻击倍率 = 1.0
        for i in self.技能栏:
            try:
                站街物理攻击倍率 *= i.物理攻击力倍率(self.武器类型)
            except:
                pass
        return 站街物理攻击倍率

    def 站街魔法攻击力倍率(self):
        站街魔法攻击倍率 = 1.0
        for i in self.技能栏:
            try:
                站街魔法攻击倍率 *= i.魔法攻击力倍率(self.武器类型)
            except:
                pass
        return 站街魔法攻击倍率

    def 站街独立攻击力倍率(self):
        站街独立攻击倍率 = 1.0
        for i in self.技能栏:
            try:
                站街独立攻击倍率 *= i.独立攻击力倍率(self.武器类型)
            except:
                pass
        return 站街独立攻击倍率

    def 站街物理攻击力(self):
        return self.detail.物理攻击力 * self.站街物理攻击力倍率()

    def 站街魔法攻击力(self):
        return self.detail.魔法攻击力 * self.站街魔法攻击力倍率()

    def 站街独立攻击力(self):
        return self.detail.独立攻击力 * self.站街独立攻击力倍率()

    def 面板物理攻击力(self):
        面板物理攻击 = (self.detail.物理攻击力 + self.detail.进图物理攻击力) * (1 + self.detail.百分比三攻) * (
            1 + self.detail.年宠技能 * 0.10 + self.detail.斗神之吼秘药 * 0.12 + self.detail.白兔子技能 * 0.20)
        for i in self.技能栏:
            try:
                面板物理攻击 *= i.物理攻击力倍率进图(self.武器类型)
            except:
                pass
        return 面板物理攻击 * self.站街物理攻击力倍率()

    def 面板魔法攻击力(self):
        面板魔法攻击 = (self.detail.魔法攻击力 + self.detail.进图魔法攻击力) * (1 + self.detail.百分比三攻) * (
            1 + self.detail.年宠技能 * 0.10 + self.detail.斗神之吼秘药 * 0.12 + self.detail.白兔子技能 * 0.20)
        for i in self.技能栏:
            try:
                面板魔法攻击 *= i.魔法攻击力倍率进图(self.武器类型)
            except:
                pass
        return 面板魔法攻击 * self.站街魔法攻击力倍率()

    def 面板独立攻击力(self):
        面板独立攻击 = (self.detail.独立攻击力 + self.detail.进图独立攻击力) * \
            (1 + self.detail.百分比三攻)
        for i in self.技能栏:
            try:
                面板独立攻击 *= i.独立攻击力倍率进图(self.武器类型)
            except:
                pass
        return 面板独立攻击 * self.站街独立攻击力倍率()
    # endregion

    # 设置技能相关参数
    def skill_set(self, setinfo):
        for i in setinfo:
            k = self.get_skill_by_name(i['name'])
            k.等级 = i['level']
            k.TP等级 = i['tp']

    # 计算伤害前置流程
    def 计算伤害预处理(self):
        self.装备属性计算()
        self.所有属性强化(self.detail.进图属强)
        self.CD倍率计算()
        self.加算冷却计算()
        self.被动倍率计算()
        self.伤害指数计算()

    # 技能队列伤害计算
    def 伤害计算(self, skill_set_list):
        data = {}
        sumdamage = 0
        for i in skill_set_list:
            k = self.get_skill_by_name(i['name'])
            if k.是否有伤害 == 1:
                if k.名称 not in data.keys():
                    temp = {}
                    temp['rate'] = k.被动倍率
                    temp['cd'] = k.等效CD(self.武器类型, self.类型)
                damage = k.等效百分比(self.武器类型) * self.伤害指数 * k.被动倍率 * i['count']
                sumdamage += damage
                temp['count'] = temp.get('count', 0) + i['count']
                temp['damage'] = temp.get('damage', 0) + damage
                data[k.名称] = temp
        data['sumdamage'] = sumdamage
        return data

    # region 伤害计算相关函数
    def 装备属性计算(self):
        self.装备基础()
        self.装备词条计算()

    def 装备基础(self):
        self.防具基础()
        self.首饰基础()
        self.特殊基础()
        # self.武器基础()
        self.增幅基础()
        pass

    def 防具精通计算(self, i):
        temp = equ.get_equ_by_name(self.装备栏[i])
        部位 = 部位列表[i]
        return 精通计算(temp.等级, temp.品质, self.forge_set.get(部位, {}).get('cursed_number', 0), 部位)
        # if temp.所属套装 != '智慧产物':
        #    return 精通计算(temp.等级, temp.品质, self.forge_set.get(部位, {}).get('cursed_number', 0), 部位)
        # else:
        #    return 精通计算(temp.等级, temp.品质, self.forge_set.get(部位, {}).get('wisdom_number', 0), 部位)

    def 防具基础(self):
        for i in [0, 1, 2, 3, 4]:
            temp = equ.get_equ_by_name(self.装备栏[i])
            self.detail.力量 += temp.力量[self.防具类型]
            self.detail.智力 += temp.智力[self.防具类型]

            精通数值 = self.防具精通计算(i)
            if '力量' in self.防具精通属性:
                self.detail.力量 += 精通数值
            if '智力' in self.防具精通属性:
                self.detail.智力 += 精通数值

    def 增幅基础(self):
        for i in range(11):  # 暂时未计算武器
            temp = equ.get_equ_by_name(self.装备栏[i])
            部位 = 部位列表[i]
            if self.forge_set.get(部位, {}).get('cursed_type', 0) == 1:
                x = 增幅计算(temp.等级, temp.品质, self.forge_set.get(
                    部位, {}).get('cursed_number', 0))
                if '物理' in self.类型 or '力量' in self.类型:
                    self.detail.力量 += x
                else:
                    self.detail.智力 += x
            # if self.是否增幅[i] and temp.所属套装 != '智慧产物':
            #    x = 增幅计算(temp.等级, temp.品质, self.强化等级[i])

    def 首饰基础(self):
        for i in [5, 6, 7]:
            temp = equ.get_equ_by_name(self.装备栏[i])
            self.detail.力量 += temp.力量
            self.detail.智力 += temp.智力
            self.detail.物理攻击力 += temp.物理攻击力
            self.detail.魔法攻击力 += temp.魔法攻击力
            self.detail.独立攻击力 += temp.独立攻击力

    def 特殊基础(self):
        for i in [8, 9, 10]:
            temp = equ.get_equ_by_name(self.装备栏[i])
            self.detail.力量 += temp.力量
            self.detail.智力 += temp.智力
            self.detail.物理攻击力 += temp.物理攻击力
            self.detail.魔法攻击力 += temp.魔法攻击力
            self.detail.独立攻击力 += temp.独立攻击力

        # 耳环
        temp = equ.get_equ_by_name(self.装备栏[8])
        部位 = 部位列表[i]
        # if temp.所属套装 != '智慧产物':
        x = 耳环计算(temp.等级, temp.品质, self.forge_set.get(
            部位, {}).get('cursed_number', 0))
        self.detail.物理攻击力 += x
        self.detail.魔法攻击力 += x
        self.detail.独立攻击力 += x

        # 辅助装备、魔法石
        for i in [9, 10]:
            temp = equ.get_equ_by_name(self.装备栏[i])
            部位 = 部位列表[i]
            # if temp.所属套装 != '智慧产物':
            x = 左右计算(temp.等级, temp.品质, self.forge_set.get(
                部位, {}).get('cursed_number', 0))
            self.detail.力量 += x
            self.detail.智力 += x
    '''
    def 武器基础(self):
        temp = equ.get_equ_by_name(self.装备栏[11])

        self.力量 += temp.力量
        self.智力 += temp.智力
        self.物理攻击力 += temp.物理攻击力
        self.魔法攻击力 += temp.魔法攻击力
        self.独立攻击力 += temp.独立攻击力

        if temp.所属套装 != '智慧产物':
            self.物理攻击力 += 武器计算(temp.等级, temp.品质, self.强化等级[11], self.武器类型,
                               '物理')
            self.魔法攻击力 += 武器计算(temp.等级, temp.品质, self.强化等级[11], self.武器类型,
                               '魔法')
            self.独立攻击力 += 锻造计算(temp.等级, temp.品质, self.武器锻造等级)
    '''

    def 装备词条计算(self):
        for func in equ.get_func_list_by_namelist(self.装备栏):
            func(self)
            #打印相关函数和效果
            print('{}: {}'.format(func, func(self, text=TRUE)))

    def 被动倍率计算(self):
        if self.远古记忆 > 0:
            self.detail.进图智力 += self.远古记忆 * 15
        if self.刀魂之卡赞 > 0:
            self.detail.进图力量 += 刀魂之卡赞数据[self.刀魂之卡赞]
            self.detail.进图智力 += 刀魂之卡赞数据[self.刀魂之卡赞]
        for i in self.技能栏:
            i.被动倍率 = 1
        for i in self.技能栏:
            if i.关联技能 != ['无']:
                if i.关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率(self.武器类型)
                else:
                    for k in i.关联技能:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率(self.武器类型)
            if i.非关联技能 != ['无']:
                if i.非关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 /= i.加成倍率(self.武器类型)
                else:
                    for k in i.非关联技能:
                        self.技能栏[self.技能序号[k]].被动倍率 /= i.加成倍率(self.武器类型)

            if i.关联技能2 != ['无']:
                if i.关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率2(self.武器类型)
                else:
                    for k in i.关联技能2:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率2(self.武器类型)

            if i.非关联技能2 != ['无']:
                if i.非关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 /= i.加成倍率2(self.武器类型)
                else:
                    for k in i.非关联技能2:
                        self.技能栏[self.技能序号[k]].被动倍率 /= i.加成倍率2(self.武器类型)

            if i.关联技能3 != ['无']:
                if i.关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率3(self.武器类型)
                else:
                    for k in i.关联技能3:
                        self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率3(self.武器类型)

            if i.非关联技能3 != ['无']:
                if i.非关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.被动倍率 /= i.加成倍率3(self.武器类型)
                else:
                    for k in i.非关联技能3:
                        self.技能栏[self.技能序号[k]].被动倍率 /= i.加成倍率3(self.武器类型)

    def 加算冷却计算(self):
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                i.CD *= (1 - self.detail.加算冷却缩减)

    def CD倍率计算(self):
        for i in self.技能栏:
            if i.冷却关联技能 != ['无']:
                if i.冷却关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率(self.武器类型)
                else:
                    for k in i.冷却关联技能:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率(self.武器类型)
            if i.非冷却关联技能 != ['无']:
                if i.非冷却关联技能 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD /= i.CD缩减倍率(self.武器类型)
                else:
                    for k in i.非冷却关联技能:
                        self.技能栏[self.技能序号[k]].CD /= i.CD缩减倍率(self.武器类型)
            if i.冷却关联技能2 != ['无']:
                if i.冷却关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率2(self.武器类型)
                else:
                    for k in i.冷却关联技能2:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率2(self.武器类型)
            if i.非冷却关联技能2 != ['无']:
                if i.非冷却关联技能2 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD /= i.CD缩减倍率2(self.武器类型)
                else:
                    for k in i.非冷却关联技能2:
                        self.技能栏[self.技能序号[k]].CD /= i.CD缩减倍率2(self.武器类型)
            if i.冷却关联技能3 != ['无']:
                if i.冷却关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率3(self.武器类型)
                else:
                    for k in i.冷却关联技能3:
                        self.技能栏[self.技能序号[k]].CD *= i.CD缩减倍率3(self.武器类型)
            if i.非冷却关联技能3 != ['无']:
                if i.非冷却关联技能3 == ['所有']:
                    for j in self.技能栏:
                        if j.是否有伤害 == 1:
                            j.CD /= i.CD缩减倍率3(self.武器类型)
                else:
                    for k in i.非冷却关联技能3:
                        self.技能栏[self.技能序号[k]].CD /= i.CD缩减倍率3(self.武器类型)

    def 属性倍率计算(self):
        # 火、冰、光、暗
        self.属性倍率组 = []
        self.属性倍率组.append(1.05 + 0.0045 * int(self.detail.火属性强化 - self.火抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.detail.冰属性强化 - self.冰抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.detail.光属性强化 - self.光抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.detail.暗属性强化 - self.暗抗输入))
        self.属性倍率 = max(self.属性倍率组)
        '''
        if self.攻击属性 == 0:
            self.属性倍率 = max(self.属性倍率组)
        elif self.攻击属性 == 1:
            self.属性倍率 = self.属性倍率组[0]
        elif self.攻击属性 == 2:
            self.属性倍率 = self.属性倍率组[1]
        elif self.攻击属性 == 3:
            self.属性倍率 = self.属性倍率组[2]
        elif self.攻击属性 == 4:
            self.属性倍率 = self.属性倍率组[3]
        '''

    def 面板系数计算(self):
        if self.类型 == '物理百分比':
            return int((self.detail.面板力量() / 250 + 1) * self.面板物理攻击力() *
                       (1 + self.detail.百分比三攻))
        elif self.类型 == '魔法百分比':
            return int((self.detail.面板智力() / 250 + 1) * self.面板魔法攻击力() *
                       (1 + self.detail.百分比三攻))
        elif self.类型 == '物理固伤':
            return int((self.detail.面板力量() / 250 + 1) * self.面板独立攻击力() *
                       (1 + self.detail.百分比三攻))
        elif self.类型 == '魔法固伤':
            return int((self.detail.面板智力() / 250 + 1) * self.面板独立攻击力() *
                       (1 + self.detail.百分比三攻))

    def 伤害指数计算(self):

        防御 = max(self.防御输入 - self.detail.固定减防, 0) * (1 - self.detail.百分比减防)
        基准倍率 = 1.5 * self.buff_ratio * (1 - 防御 / (防御 + 200 * self.等级))

        # 避免出现浮点数取整BUG
        self.detail.伤害增加 += 0.00000001

        self.属性倍率计算()

        面板 = self.面板系数计算()

        增伤倍率 = 1 + int(self.detail.伤害增加 * 100) / 100
        增伤倍率 *= 1 + self.detail.暴击伤害
        增伤倍率 *= 1 + self.detail.最终伤害
        增伤倍率 *= self.detail.技能攻击力
        增伤倍率 *= 1 + self.detail.持续伤害  # * self.持续伤害计算比例
        增伤倍率 *= 1 + self.detail.附加伤害 + self.detail.属性附加 * self.属性倍率

        self.伤害指数 = 面板 * self.属性倍率 * 增伤倍率 * 基准倍率 / 100  # * self.队友增幅系数

        # 7.8日,伤害数据压缩
        self.伤害指数 /= 1000
    # endregion

    def calc(self, setName):
        self.detail = Detail(self.character, self.classChange)
        info = store.get("/{}/setinfo/{}".format(self.alter, setName))

        # 设置相关参数
        self.skill_set(info['skill_set'])
        self.forge_set = info['forge_set']
        
        # 词条选择相关信息 {词条id：选择序号}
        #print(equ.get_chose_set())
        equ.set_func_chose({839: 0})

        self.计算伤害预处理()

        result = {
            '站街力量': self.detail.站街力量(),
            '站街智力': self.detail.站街智力(),
            '面板力量': self.detail.面板力量(),
            '面板智力': self.detail.面板智力(),
            '站街物理攻击力': self.站街物理攻击力(),
            '站街魔法攻击力': self.站街魔法攻击力(),
            '站街独立攻击力': self.站街独立攻击力(),
            '面板物理攻击力': self.面板物理攻击力(),
            '面板魔法攻击力': self.面板魔法攻击力(),
            '面板独立攻击力': self.面板独立攻击力(),
            '伤害指数': self.伤害指数,
            'result': self.伤害计算(info['skill_set']),
        }
        print(result)
        return info
