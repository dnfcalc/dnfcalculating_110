from unittest import result
from core.baseClass.skill import 技能
from core.store import store
from core.equipment.基础函数 import 基础属性输入


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
    武器类型 = ''
    weaponType = []
    # 输出类型选择，默认类型为第一个
    carryType = []
    # 防具类型
    armor = ''
    # 防具类型精通，智力、力量
    armor_mastery = []
    # buff倍率
    buff_ratio = 1.0
    # 技能列表
    技能栏 = []
    技能字典 = {}
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
        return self.技能栏[self.技能字典.get(name, 0)]

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

    def calc(self, setName):
        self.detail = Detail(self.character, self.classChange)
        info = store.get("/{}/setinfo/{}".format(self.alter, setName))
        for i in info['skill_set']:
            k = self.get_skill_by_name(i['name'])
            k.等级 = i['level']

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
        }
        print(result)
        return info
