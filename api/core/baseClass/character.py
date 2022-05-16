from pickle import TRUE
from core.baseClass.equipment import equ
from core.store import store
from core.equipment.基础函数 import 基础属性输入, 部位列表, 精通计算, 增幅计算, 耳环计算, 左右计算, 成长词条计算, 武器强化计算, 锻造计算
from core.baseClass.enchanting import get_encfunc_by_id
from core.baseClass.emblems import get_embfunc_by_id


class Character:
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
    打造详情 = {}
    装备栏 = []  # [装备id]
    部位装备 = {}  # {部位: 装备id}
    部位附魔 = {}  # {部位: 附魔函数}
    词条等级 = {}  # {部位: [等级1, 2, 3, 4]}

    # 需要职业自定义数据
    实际名称 = ''
    名称 = ''
    角色 = ''
    职业类型 = ''
    职业 = ''
    武器选项 = []
    输出类型选项 = []
    防具精通属性 = []
    类型 = ''
    武器类型 = ''
    防具类型 = ''
    技能栏 = []
    技能序号 = {}
    buff = 1.00

    def __init__(self) -> None:
        # 计算变量 ##########
        self.基础力量 = 0
        self.基础智力 = 0
        self.基础体力 = 0
        self.基础精神 = 0

        self.力量 = 0
        self.智力 = 0
        self.体力 = 0
        self.精神 = 0

        self.进图力量 = 0.0
        self.进图智力 = 0.0
        self.进图体力 = 0.0
        self.进图精神 = 0.0
        self.系统奶系数 = 0
        self.系统奶基数 = 0
        self.年宠技能 = False
        self.白兔子技能 = False
        self.斗神之吼秘药 = False

        self.物理攻击力 = 65
        self.魔法攻击力 = 65
        self.独立攻击力 = 1045
        self.火属性强化 = 13
        self.冰属性强化 = 13
        self.光属性强化 = 13
        self.暗属性强化 = 13
        self.进图物理攻击力 = 0
        self.进图魔法攻击力 = 0
        self.进图独立攻击力 = 0
        self.进图属强 = 0

        # 旧词条
        self.百分比力智 = 0.0
        self.百分比三攻 = 0.0
        self.伤害增加 = 0.0
        self.附加伤害 = 0.0
        self.属性附加 = 0.0
        self.暴击伤害 = 0.0
        self.最终伤害 = 0.0
        self.技能攻击力 = 1.0
        self.技能攻击力累加 = 0.0
        self.持续伤害 = 0.0
        self.加算冷却缩减 = 0.0
        self.百分比减防 = 0.0
        self.固定减防 = 0

        # 其它词条
        self.攻击速度 = 0.00
        self.移动速度 = 0.00
        self.施放速度 = 0.00
        self.命中率 = 0.0
        self.回避率 = 0.0
        self.物理暴击率 = 0.00
        self.魔法暴击率 = 0.00
        self.火属性抗性 = 0
        self.冰属性抗性 = 0
        self.光属性抗性 = 0
        self.暗属性抗性 = 0

        # 新属性
        self.伤害量 = 0
        self.百分比伤害量 = 0.0
        self.buff量 = 0

        # 设置基础属性
        基础属性输入(self)

    # region 返回前端信息
    def getinfo(self):
        info = {}
        info["alter"] = self.实际名称
        info["name"] = self.名称
        info["character"] = self.职业
        info["characterType"] = self.职业类型
        info["classChange"] = self.职业
        info["weaponType"] = self.武器选项
        info["carry_type_list"] = self.输出类型选项
        info["armor"] = self.防具类型
        info["armor_mastery"] = self.防具精通属性
        info["buff_ratio"] = self.buff
        self.set_skill_info(info)
        self.set_individuation(info)
        return info

    def set_skill_info(self, info, rune_except=[], clothes_bottom=[]):
        skillInfo = []  # 技能
        rune = []  # 符文
        talisman = []  # 护石
        platinum = []  # 白金
        clothes = []  # 时装
        # print(self.技能栏)
        for skill in self.技能栏:
            skill.等级 = skill.基础等级
            skillInfo.append({
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
                talisman.append(skill.名称)
            # 符文
            if skill.所在等级 >= 20 and skill.所在等级 <= 80 and skill.所在等级 != 50 and skill.是否有伤害 == 1 and skill.名称 not in rune_except:
                rune.append(skill.名称)
            # 白金
            if skill.所在等级 <= 70 and skill.所在等级 not in [48, 50]:
                platinum.append(skill.名称)
            # 时装
            if skill.所在等级 <= 95:
                clothes.append(skill.名称)
        info['skillInfo'] = skillInfo
        info['rune'] = rune
        info['talisman'] = talisman
        info['platinum'] = platinum
        info['clothes'] = clothes
        info['clothes_bottom'] = clothes_bottom

    def set_individuation(self, info):
        pass

    # endregion

    # region 词条属性
    def 伤害量加成(self, x):
        self.伤害量 += x

    def buff量加成(self, x):
        self.buff量 += x

    def 附加伤害加成(self, x, 辟邪玉加成=1):
        self.附加伤害 += self.附加伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 三攻固定加成(self, x=0, y=0, z=0):
        if y == 0 or z == 0:
            y = x
            z = x
        self.物理攻击力 += x
        self.魔法攻击力 += y
        self.独立攻击力 += z

    def 力智固定加成(self, x=0, y=0):
        if y == 0:
            y = x
        self.力量 += x
        self.智力 += y

    def 体精固定加成(self, x=0, y=0):
        if y == 0:
            y = x
        self.体力 += x
        self.精神 += y

    def 持续伤害加成(self, x):
        self.持续伤害 += x

    def 属性附加加成(self, x):
        self.属性附加 += self.属性附加伤害增加增幅 * x

    def 技能攻击力加成(self, x, 辟邪玉加成=1, 适用累加=1):
        if 适用累加 == 0:
            self.技能攻击力 *= 1 + self.技能伤害增加增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.技能攻击力累加 += x
            if self.技能攻击力累加 <= 2:
                self.技能攻击力 *= 1 + self.技能伤害增加增幅 * x if 辟邪玉加成 == 1 else x
            else:
                self.技能攻击力 *= 1 + (self.技能伤害增加增幅*(2+x-self.技能攻击力累加) +
                                   self.技能攻击力累加-2) if self.技能攻击力累加 - x < 2 or 辟邪玉加成 == 1 else x

    def 暴击伤害加成(self, x, 辟邪玉加成=1):
        self.暴击伤害 += self.暴击伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 伤害增加加成(self, x, 辟邪玉加成=1):
        self.伤害增加 += self.伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 最终伤害加成(self, x, 辟邪玉加成=1):
        self.最终伤害 += self.最终伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 百分比力智加成(self, x, 辟邪玉加成=1):
        self.百分比力智 += self.力量智力增加增幅 * x if 辟邪玉加成 == 1 else x

    def 百分比三攻加成(self, x, 辟邪玉加成=1):
        self.百分比三攻 += self.物理魔法攻击力增加增幅 * x if 辟邪玉加成 == 1 else x

    def 火属性强化加成(self, x, 辟邪玉加成=1):
        if self.状态 == 0:
            self.火属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
        else:
            self.火属性强化 += int(self.所有属性强化增加 * x)

    def 冰属性强化加成(self, x, 辟邪玉加成=1):
        if self.状态 == 0:
            self.冰属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
        else:
            self.冰属性强化 += int(self.所有属性强化增加 * x)

    def 光属性强化加成(self, x, 辟邪玉加成=1):
        if self.状态 == 0:
            self.光属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
        else:
            self.光属性强化 += int(self.所有属性强化增加 * x)

    def 暗属性强化加成(self, x, 辟邪玉加成=1):
        if self.状态 == 0:
            self.暗属性强化 += self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
        else:
            self.暗属性强化 += int(self.所有属性强化增加 * x)

    def 所有属性强化加成(self, x, 辟邪玉加成=1):
        if self.状态 == 0:
            temp = self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x
        else:
            temp = int(self.所有属性强化增加 * x)
        self.所有属性强化(temp)

    def 火属性抗性加成(self, x):
        self.火属性抗性 += x

    def 冰属性抗性加成(self, x):
        self.冰属性抗性 += x

    def 光属性抗性加成(self, x):
        self.光属性抗性 += x

    def 暗属性抗性加成(self, x):
        self.暗属性抗性 += x

    def 所有属性抗性加成(self, x):
        self.火属性抗性加成(x)
        self.冰属性抗性加成(x)
        self.光属性抗性加成(x)
        self.暗属性抗性加成(x)

    def 攻击速度增加(self, x):
        self.攻击速度 += x

    def 移动速度增加(self, x):
        self.移动速度 += x

    def 施放速度增加(self, x):
        self.施放速度 += x

    def 命中率增加(self, x):
        self.命中率 += x

    def 回避率增加(self, x):
        self.回避率 += x

    def 物理暴击率增加(self, x):
        self.物理暴击率 += x

    def 魔法暴击率增加(self, x):
        self.魔法暴击率 += x

    def 暴击率增加(self, x):
        self.物理暴击率增加(x)
        self.魔法暴击率增加(x)

    def buff技能等级加成(self, LV, lv):
        # LV级 buff技能等级 + lv
        pass

    def 技能等级加成(self, 加成类型, minLv, maxLv, lv):
        lv = int(lv)
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
        self.进图属强 += int(self.所有属性强化增加 * x if 辟邪玉加成 == 1 else x)

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
        self.火属性强化 += x
        self.冰属性强化 += x
        self.光属性强化 += x
        self.暗属性强化 += x

    # endregion

    # region 面板相关函数

    # 基础力量智力(站街力量智力)
    def 站街力量(self):
        return int(self.力量)

    def 站街智力(self):
        return int(self.智力)

    # 新词条计算的力量智力

    def 基础面板力量(self):
        return (self.力量 + int((self.力量 - self.基础力量) * self.系统奶系数 + self.系统奶基数)
                + self.进图力量)

    def 基础面板智力(self):
        return (self.智力 + int((self.智力 - self.基础智力) * self.系统奶系数 + self.系统奶基数)
                + self.进图智力)

    # 旧词条计算的力量智力(图内力量智力)

    def 面板力量(self):
        return self.基础面板力量() * (1 + self.百分比力智)

    def 面板智力(self):
        return self.基础面板智力() * (1 + self.百分比力智)

    # 站街生效的技能三攻倍率

    def 站街物理攻击力倍率(self):
        站街物理攻击倍率 = 1.0
        for i in self.技能栏:
            站街物理攻击倍率 *= i.物理攻击力倍率(self.武器类型)
        return 站街物理攻击倍率

    def 站街魔法攻击力倍率(self):
        站街魔法攻击倍率 = 1.0
        for i in self.技能栏:
            站街魔法攻击倍率 *= i.魔法攻击力倍率(self.武器类型)
        return 站街魔法攻击倍率

    def 站街独立攻击力倍率(self):
        站街独立攻击倍率 = 1.0
        for i in self.技能栏:
            站街独立攻击倍率 *= i.独立攻击力倍率(self.武器类型)
        return 站街独立攻击倍率

    # 站街三攻

    def 站街物理攻击力(self):
        return self.物理攻击力 * self.站街物理攻击力倍率()

    def 站街魔法攻击力(self):
        return self.魔法攻击力 * self.站街魔法攻击力倍率()

    def 站街独立攻击力(self):
        return self.独立攻击力 * self.站街独立攻击力倍率()


    # 新词条计算的三攻(旧词条需要额外乘百分比三攻)
    def 基础面板物理攻击力(self):
        面板物理攻击 = self.物理攻击力 + self.进图物理攻击力
        for i in self.技能栏:
            面板物理攻击 *= i.物理攻击力倍率进图(self.武器类型)
        return 面板物理攻击 * self.站街物理攻击力倍率()

    def 基础面板魔法攻击力(self):
        面板魔法攻击 = self.魔法攻击力 + self.进图魔法攻击力
        for i in self.技能栏:
            面板魔法攻击 *= i.魔法攻击力倍率进图(self.武器类型)
        return 面板魔法攻击 * self.站街魔法攻击力倍率()

    def 基础面板独立攻击力(self):
        面板独立攻击 = self.独立攻击力 + self.进图独立攻击力
        for i in self.技能栏:
            面板独立攻击 *= i.独立攻击力倍率进图(self.武器类型)
        return 面板独立攻击 * self.站街独立攻击力倍率()


    # 图内显示的三攻(不参与伤害计算)
    def 面板物理攻击力(self):
        面板物理攻击 = self.基础面板物理攻击力() * (1 + self.百分比三攻) * (
            1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        return 面板物理攻击

    def 面板魔法攻击力(self):
        面板魔法攻击 = self.基础面板魔法攻击力() * (1 + self.百分比三攻) * (
            1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        return 面板魔法攻击

    def 面板独立攻击力(self):
        面板独立攻击 = self.基础面板独立攻击力() * (1 + self.百分比三攻)
        return 面板独立攻击
    # endregion

    # region 其它函数
    def get_skill_by_name(self, name):
        return self.技能栏[self.技能序号.get(name, 0)]

    def 已穿戴神话(self):
        for i in self.装备栏:
            temp = equ.get_equ_by_id(i)
            if temp.品质 == '神话':
                return True
        return False

    # endregion

    # 打造设置
    def 打造设置(self, setinfo):
        self.打造详情 = setinfo
        for i in 部位列表 + ('称号', '宠物', ):
            id = setinfo.get(i, {}).get('enchanting', 0)
            self.部位附魔[i] = get_encfunc_by_id(id)

    # 设置技能相关参数
    def skill_set(self, setinfo):
        for i in setinfo:
            k = self.get_skill_by_name(i['name'])
            k.等级 = i['level']
            k.TP等级 = i['tp']

    # 设置装备选项参数
    def equ_chose_set(self, setinfo):
        for i in setinfo:
            equ.set_func_chose({i['id']: i['select']})

    # 设置穿戴的装备
    def 穿戴装备(self, idlist):
        self.装备栏 = []
        self.部位装备 = {}
        for i in idlist:
            装备 = equ.get_equ_by_id(i)
            self.部位装备.update({装备.部位: i})
        for k in self.部位装备.keys():
            self.装备栏.append(self.部位装备[k])

    # region 伤害计算相关函数
    def 计算伤害预处理(self):
        self.装备属性计算()
        self.所有属性强化(self.进图属强)
        self.CD倍率计算()
        self.加算冷却计算()
        self.被动倍率计算()
        self.伤害指数计算()

    def 伤害计算(self, skill_set_list):
        data = {}
        sumdamage = 0
        for i in skill_set_list:
            if i['count'] == 0:
                continue
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

    def 装备属性计算(self):
        self.装备基础()
        self.附魔计算()
        self.徽章计算()
        self.装备词条计算()

    def 徽章计算(self):
        idlist = []
        for i in 部位列表:  # ('皮肤', '光环', '武器装扮', )
            if i in self.打造详情.keys():
                temp = self.打造详情[i]
                for j in ['socket_left', 'socket_right']:
                    id = temp.get(j, 0)
                    if id != 0:
                        idlist.append(id)
        for i in idlist:
            func = get_embfunc_by_id(i)
            func(self)
            # 打印相关函数和效果
            #print('{}: {}'.format(func, func(self, text=TRUE)))

    def 附魔计算(self):
        for i in self.部位附魔.keys():
            func = self.部位附魔[i]
            func(self)
            # 打印相关函数和效果
            #print('{}: {}: {}'.format(i, func, func(self, text=TRUE)))

    def 装备基础(self):
        for id in self.装备栏:
            temp = equ.get_equ_by_id(id)
            if '甲' in temp.类型:
                self.防具计算(temp)
            elif temp.类型 == '首饰':
                self.首饰计算(temp)
            elif temp.类型 == '特殊':
                self.特殊计算(temp)
            elif temp.部位 == '武器':
                self.武器计算(temp)
            self.增幅计算(temp)
        pass

    def 防具精通计算(self, temp):
        部位 = temp.部位
        return 精通计算(temp.等级, temp.品质, self.打造详情.get(部位, {}).get('cursed_number', 0), 部位)
        # if temp.所属套装 != '智慧产物':
        #    return 精通计算(temp.等级, temp.品质, self.打造详情.get(部位, {}).get('cursed_number', 0), 部位)
        # else:
        #    return 精通计算(temp.等级, temp.品质, self.打造详情.get(部位, {}).get('wisdom_number', 0), 部位)

    def 防具计算(self, temp):
        self.力量 += temp.力量[self.防具类型]
        self.智力 += temp.智力[self.防具类型]

        精通数值 = self.防具精通计算(temp)
        if '力量' in self.防具精通属性:
            self.力量 += 精通数值
        if '智力' in self.防具精通属性:
            self.智力 += 精通数值

    def 增幅计算(self, temp):
        if self.打造详情.get(temp.部位, {}).get('cursed_type', 0) == 1:
            x = 增幅计算(temp.等级, temp.品质, self.打造详情.get(
                temp.部位, {}).get('cursed_number', 0))
            if '物理' in self.类型 or '力量' in self.类型:
                self.力量 += x
            else:
                self.智力 += x
        # if self.是否增幅[i] and temp.所属套装 != '智慧产物':
        #    x = 增幅计算(temp.等级, temp.品质, self.强化等级[i])

    def 首饰计算(self, temp):
        self.力量 += temp.力量
        self.智力 += temp.智力
        self.物理攻击力 += temp.物理攻击力
        self.魔法攻击力 += temp.魔法攻击力
        self.独立攻击力 += temp.独立攻击力

    def 特殊计算(self, temp):
        self.力量 += temp.力量
        self.智力 += temp.智力
        self.物理攻击力 += temp.物理攻击力
        self.魔法攻击力 += temp.魔法攻击力
        self.独立攻击力 += temp.独立攻击力

        # 耳环
        if temp.部位 == '耳环':
            # if temp.所属套装 != '智慧产物':
            x = 耳环计算(temp.等级, temp.品质, self.打造详情.get(
                temp.部位, {}).get('cursed_number', 0))
            self.物理攻击力 += x
            self.魔法攻击力 += x
            self.独立攻击力 += x

        # 辅助装备、魔法石
        else:
            # if temp.所属套装 != '智慧产物':
            x = 左右计算(temp.等级, temp.品质, self.打造详情.get(
                temp.部位, {}).get('cursed_number', 0))
            self.力量 += x
            self.智力 += x

    def 武器计算(self, temp):
        self.力量 += temp.力量
        self.智力 += temp.智力
        self.物理攻击力 += temp.物理攻击力
        self.魔法攻击力 += temp.魔法攻击力
        self.独立攻击力 += temp.独立攻击力

        # if temp.所属套装 != '智慧产物':
        info = self.打造详情.get(temp.部位, {})
        self.物理攻击力 += 武器强化计算(temp.等级, temp.品质, info.get('cursed_number', 0), temp.类型,
                             '物理')
        self.魔法攻击力 += 武器强化计算(temp.等级, temp.品质, info.get('cursed_number', 0), temp.类型,
                             '魔法')
        self.独立攻击力 += 锻造计算(temp.等级, temp.品质, info.get('dz_number', 0))

    def 装备词条计算(self):
        # 伤害量相关计算
        for i in 部位列表:
            temp = []
            for j in ["growth_First", "growth_Second", "growth_Third", "growth_Fourth"]:
                temp.append(self.打造详情.get(i, {}).get(j, 1))
            self.词条等级[i] = temp
        for 部位, 序号, 基础 in equ.get_damagelist_by_idlist(self.装备栏):
            等级 = self.词条等级[部位][序号]
            self.伤害量加成(成长词条计算(基础, 等级))
        # 词条效果相关计算
        for func, buwei in equ.get_func_list_by_idlist(self.装备栏):
            func(self, bw=buwei)  # 站街效果
            func(self, mode=1, bw=buwei)  # 进图效果
            # 打印相关函数和效果
            #print('{}: {}: {}'.format(buwei, func, func(self, text=TRUE)))

    def 被动倍率计算(self):
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
                i.CD *= (1 - self.加算冷却缩减)

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
        self.属性倍率组.append(1.05 + 0.0045 * int(self.火属性强化 - self.火抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.冰属性强化 - self.冰抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.光属性强化 - self.光抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.暗属性强化 - self.暗抗输入))
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

    def 面板系数计算(self, mode=1):
        # 基础面板 不含百分比力智和百分比三攻
        if mode == 0:
            if self.类型 == '物理百分比':
                return int((self.基础面板力量() / 250 + 1) * self.基础面板物理攻击力())
            elif self.类型 == '魔法百分比':
                return int((self.基础面板智力() / 250 + 1) * self.基础面板魔法攻击力())
            elif self.类型 == '物理固伤':
                return int((self.基础面板力量() / 250 + 1) * self.基础面板独立攻击力())
            elif self.类型 == '魔法固伤':
                return int((self.基础面板智力() / 250 + 1) * self.基础面板独立攻击力())
        # 旧版算法 不含斗神、宠物技能等
        else:
            if self.类型 == '物理百分比':
                return int((self.面板力量() / 250 + 1) * self.基础面板物理攻击力() * (1 + self.百分比三攻))
            elif self.类型 == '魔法百分比':
                return int((self.面板智力() / 250 + 1) * self.基础面板魔法攻击力() * (1 + self.百分比三攻))
            elif self.类型 == '物理固伤':
                return int((self.面板力量() / 250 + 1) * self.基础面板独立攻击力() * (1 + self.百分比三攻))
            elif self.类型 == '魔法固伤':
                return int((self.面板智力() / 250 + 1) * self.基础面板独立攻击力() * (1 + self.百分比三攻))

    def 伤害指数计算(self):

        防御 = max(self.防御输入 - self.固定减防, 0) * (1 - self.百分比减防)
        基准倍率 = 1.5 * self.buff * (1 - 防御 / (防御 + 200 * self.等级))

        # 避免出现浮点数取整BUG
        self.伤害增加 += 0.00000001

        self.属性倍率计算()

        # 基础面板 不含百分比力智和百分比三攻
        基础面板 = self.面板系数计算(mode=0)
        旧版面板 = self.面板系数计算(mode=1)

        新 = self.伤害量 * (1 + self.百分比伤害量) * 0.001
        旧 = 1 + int(self.伤害增加 * 100) / 100
        旧 *= 1 + self.暴击伤害
        旧 *= 1 + self.最终伤害
        旧 *= 1 + self.持续伤害
        旧 *= 1 + self.附加伤害 + self.属性附加 * self.属性倍率

        self.伤害指数 = (新 * 基础面板 + 旧 * 旧版面板) * self.技能攻击力 * self.属性倍率 * 基准倍率

        # 7.8日,伤害数据压缩
        self.伤害指数 /= 1000
    # endregion

    def calc(self, setName):
        info = store.get("/{}/setinfo/{}".format(self.实际名称, setName))

        # 获取打造数据
        self.打造设置(info['forge_set'])
        # 获取装备列表
        self.穿戴装备(info['equip_list'])
        # 获取技能数据
        self.skill_set(info['skill_set'])
        # 获取装备选项数据
        self.equ_chose_set(info['trigger_set'])

        self.计算伤害预处理()

        result = {
            '伤害量': self.伤害量,
            '站街力量': self.站街力量(),
            '站街智力': self.站街智力(),
            '面板力量': self.面板力量(),
            '面板智力': self.面板智力(),
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
        return result
