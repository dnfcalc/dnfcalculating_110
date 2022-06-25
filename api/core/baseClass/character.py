import importlib
from copy import deepcopy
from multiprocessing.sharedctypes import Value
from operator import index
from pickle import TRUE
from pyclbr import Function
from statistics import mode
from tkinter.messagebox import NO
from typing import Dict, List, Union
from uuid import uuid1

from click import option
from core.baseClass.equipment import equ, equipment
from core.baseClass.property import 角色属性
from core.baseClass.skill import 主动技能, 技能, 被动技能
from core.equipment.基础函数 import (增幅计算, 奶成长词条计算, 左右计算, 成长词条计算, 武器强化计算, 精通计算,
                                 耳环计算, 获取基础属性, 部位列表, 锻造四维, 锻造计算)
from core.store import store

from .avatar import 装扮套装, 装扮套装集合, 装扮集合

# from core.baseClass.enchanting import get_encfunc_by_id
# from core.baseClass.emblems import get_embfunc_by_id
# from core.baseClass.jade import get_jadefunc_by_id


class Character(角色属性):
    等级 = 110
    # 辟邪玉属性
    附加伤害增加增幅: float = 1.0
    属性附加伤害增加增幅: float = 1.0
    技能伤害增加增幅: float = 1.0
    暴击伤害增加增幅: float = 1.0
    伤害增加增幅: float = 1.0
    最终伤害增加增幅: float = 1.0
    力量智力增加增幅: float = 1.0
    物理魔法攻击力增加增幅: float = 1.0
    所有属性强化增幅: float = 1.0

    等级: int = 110
    防御输入: int = 506109
    火抗输入: int = 0
    冰抗输入: int = 0
    光抗输入: int = 0
    暗抗输入: int = 0
    打造详情: Dict[str, Dict[str, int]] = {}
    装备栏: List[int] = []  # [装备id]
    部位装备: Dict[str, int] = {}  # {部位: 装备id}
    部位附魔: Dict[str, Function] = {}  # {部位: 附魔函数}
    词条等级: Dict[str, List[int]] = {}  # {部位: [等级1, 2, 3, 4]}

    # 需要职业自定义数据
    实际名称 = ''
    名称 = ''
    角色 = ''
    角色类型 = ''
    职业 = ''
    武器选项: List[str] = []
    输出类型选项: List[str] = []
    防具精通属性: List[str] = []
    排行类型 = '物理百分比'
    适用属性 = '智力'
    适用数值 = 0
    类型 = ''
    武器类型 = ''
    防具类型 = ''
    转职 = ''
    # 技能栏: List[技能 | 主动技能 | 被动技能] = []
    # 技能序号: Dict[int, 技能 | 主动技能 | 被动技能] = {}
    技能栏: List[Union[技能, 主动技能, 被动技能]] = []
    技能序号: Dict[str, int] = {}
    自定义词条: Dict[int, List[int]] = {}
    buff: float = 1.00
    hotkey: List[str] = [""]*14
    技能队列 = []
    护石技能 = []
    护石栏 = []
    符文 = []
    skills_passive: Dict = {}

    装扮栏: Dict[str, int] = {}
    装扮选项: Dict[str, str] = {}

    def __init__(self) -> None:
        # 计算变量 ##########
        self.__基础力量: int = 0
        self.__基础智力: int = 0
        self.__基础体力: int = 0
        self.__基础精神: int = 0

        self.__进图力量: int = 0
        self.__进图智力: int = 0
        self.__进图体力: int = 0
        self.__进图精神: int = 0
        self.__BUFF补正智力: int = 0
        self.__BUFF补正体力: int = 0
        self.__BUFF补正精神: int = 0

        self.__力量: int = 0
        self.__智力: int = 0
        self.__体力: int = 0
        self.__精神: int = 0

        self.系统奶系数: float = 0.0
        self.系统奶基数: float = 0.0
        self.年宠技能 = False
        self.白兔子技能 = False
        self.斗神之吼秘药 = False

        self.辅助对象力智 = 5000
        self.辅助对象三攻 = 3000

        self.__物理攻击力: int = 65
        self.__魔法攻击力: int = 65
        self.__独立攻击力: int = 1134
        self.__火属性强化: float = 13
        self.__冰属性强化: float = 13
        self.__光属性强化: float = 13
        self.__暗属性强化: float = 13

        # 旧词条
        self.__百分比力智: float = 0.0
        self.__百分比三攻: float = 0.0
        self.__伤害增加: float = 0.0
        self.__附加伤害: float = 0.0
        self.__属性附加: float = 0.0
        self.__暴击伤害: float = 0.0
        self.__最终伤害: float = 0.0
        self.__技能攻击力: float = 1.0
        self.__技能攻击力累加: float = 0.0
        self.__持续伤害: float = 0.0
        self.__加算冷却缩减: float = 0.0
        self.__百分比减防: float = 0.0
        self.__固定减防: int = 0
        self.__buff固定力智: int = 0
        self.__buff百分比力智: float = 1.0
        self.__buff固定三攻: int = 0
        self.__buff百分比三攻: float = 1.0

        self.__觉醒固定力智: int = 0
        self.__觉醒百分比力智: float = 1.0

        # 其它词条
        self.__攻击速度: float = 0.00
        self.__移动速度: float = 0.00
        self.__施放速度: float = 0.00
        self.__命中率: float = 0.0
        self.__回避率: float = 0.0
        self.__物理暴击率: float = 0.00
        self.__魔法暴击率: float = 0.00
        self.__火属性抗性: int = 0
        self.__冰属性抗性: int = 0
        self.__光属性抗性: int = 0
        self.__暗属性抗性: int = 0

        # 新属性
        self.__攻击强化: int = 0
        self.__百分比攻击强化: float = 0.0
        self.__buff量: int = 0
        self.__百分比buff量: float = 0.0
        self.__基础精通倍率: float = 1.0
        self.__伤害比例: Dict[str, float] = {
            '直伤': 1.0, '中毒': 0.0, '灼烧': 0.0, '感电': 0.0, '出血': 0.0}
        self.__伤害系数: Dict[str, float] = {
            '中毒': 1.0, '灼烧': 1.0, '感电': 1.0, '出血': 1.0}
        self.__异常抗性: Dict[str, float] = {}
        self.__条件技攻: Dict[str, float] = {}
        self.__条件冷却: Dict[str, float] = {}
        self.__条件冷却恢复: Dict[str, float] = {}
        self.__指令效果: Dict[str, float] = {}
        self.__消耗品效果: float = 1.0
        self.__MP消耗量: float = 1.0

        self.skills_passive = {}

        if self.转职 == '':
            self.转职 = self.职业

        # 设置基础属性
        self.__设置基础属性()

    def __设置基础属性(self):
        temp = 获取基础属性(self.角色, self.职业)
        self.__基础力量 = temp[0]
        self.__基础智力 = temp[1]
        self.__基础体力 = temp[2]
        self.__基础精神 = temp[3]

        self.__力量 = self.__基础力量
        self.__智力 = self.__基础智力
        self.__体力 = self.__基础体力
        self.__精神 = self.__基础精神

    # region 返回前端信息
    def getinfo(self) -> Dict:
        info = {}
        info["alter"] = self.实际名称
        info["name"] = self.名称
        info["character"] = self.职业
        info["role"] = 'buffer' if self.类型 == '辅助' else 'delear'
        info["weapon_types"] = self.武器选项
        info["carry_type_list"] = self.输出类型选项
        info["armor"] = self.防具类型
        info["armor_mastery"] = self.防具精通属性
        info["buff_ratio"] = self.buff
        self.set_skill_info(info)
        self.__set_individuation(info)
        return info

    def 基础属性加成(self,
               物理攻击力=0.00, 魔法攻击力=0.00, 独立攻击力=0.00, 三攻=0,
               力量=0.00, 智力=0, 力智=0, 体力=0, 精神=0, 体精=0, 四维=0,
               物理暴击率=0.00, 魔法暴击率=0.00, 暴击率=0.00,
               攻击速度=0.00, 施放速度=0.00, 移动速度=0.00,   三速=0.00,
               **kwargs):
        self.__物理攻击力 += 物理攻击力 + 三攻
        self.__魔法攻击力 += 魔法攻击力 + 三攻
        self.__独立攻击力 += 独立攻击力 + 三攻
        self.__力量 += 力量 + 力智 + 四维
        self.__智力 += 智力 + 力智 + 四维
        self.__体力 += 体力 + 体精 + 四维
        self.__精神 += 精神 + 体精 + 四维
        self.__物理暴击率 += float(物理暴击率) + float(暴击率)
        self.__魔法暴击率 += float(魔法暴击率) + float(暴击率)
        self.__攻击速度 += float(攻击速度) + float(三速)
        self.__施放速度 += float(施放速度) + float(三速)
        self.__移动速度 += float(移动速度) + float(三速)

    def 属性强化加成(self, 所有属性强化=0.00, 冰属性强化=0.00, 火属性强化=0.00, 暗属性强化=0.00, 光属性强化=0.00):
        self.__火属性强化 += 火属性强化 + 所有属性强化
        self.__冰属性强化 += 冰属性强化 + 所有属性强化
        self.__暗属性强化 += 暗属性强化 + 所有属性强化
        self.__光属性强化 += 光属性强化 + 所有属性强化

    def set_skill_info(self, info, rune_except=[], clothes_pants=[], rune_start_lv=20) -> None:
        skillInfo = []  # 技能
        rune = []  # 符文
        talisman = []  # 护石
        platinum = []  # 白金
        clothes_coat = []  # 时装
        for skill in self.技能栏:
            skill.等级 = skill.基础等级
            skillInfo.append({
                "name": skill.名称,
                "type": skill.是否有伤害,
                "need_level": skill.所在等级,
                "level_master": skill.等级精通,
                "level_max": skill.等级上限,
                "cooldown": 0 if not skill.是否有伤害 else skill.CD,
                "current_level": skill.基础等级,
                "data": 0 if not skill.是否有伤害 else skill.等效百分比(char=self),
                "tp_max": skill.TP上限 if skill.是否有伤害 else None,
                "tp_level": skill.TP等级 if skill.是否有伤害 else None,
                "mode": [] if not skill.是否有伤害 else skill.形态
            })
            # 护石
            if skill.是否有伤害 == 1 and skill.是否有护石 == 1:
                talisman.append(skill.名称)
            # 符文
            if skill.所在等级 >= rune_start_lv and skill.所在等级 <= 80 and skill.所在等级 != 50 and skill.是否有伤害 == 1 and skill.名称 not in rune_except:
                rune.append(skill.名称)
            # 白金
            if skill.所在等级 <= 70 and skill.所在等级 not in [48, 50]:
                platinum.append(skill.名称)
            # 时装
            if skill.所在等级 <= 95:
                clothes_coat.append(skill.名称)
        if self.类型 == '辅助':
            talisman += self.护石技能
        info['skills'] = skillInfo
        info['rune'] = rune
        info['talisman'] = talisman
        info['platinum'] = platinum
        info['clothes_coat'] = clothes_coat
        info['clothes_pants'] = clothes_pants

    def __set_individuation(self, info) -> None:
        pass

    # endregion

    # region 词条属性
    def 基础精通加成(self, x: float) -> None:
        self.__基础精通倍率 += x

    def 百分比防御减少(self, x: float) -> None:
        self.__百分比减防 += x

    def 固定防御减少(self, x: int) -> None:
        self.__固定减防 += x

    def 伤害类型转化(self, 类型1: str, 类型2: str, x: float) -> None:
        # 直伤 中毒 灼烧 感电 出血
        self.__伤害比例[类型1] = self.__伤害比例.get(类型1, 0.0) - x
        self.__伤害比例[类型2] = self.__伤害比例.get(类型2, 0.0) + x

    def 异常增伤(self, 类型: str, x: float) -> None:
        # 中毒 灼烧 感电 出血
        self.__伤害系数[类型] = self.__伤害系数.get(类型, 1.0) + x

    def 异常抗性加成(self, 类型: str, x: float) -> None:
        # 中毒 灼烧 感电 出血 冰冻 减速 眩晕 诅咒 失明 石化 睡眠 混乱 束缚
        self.__异常抗性[类型] = self.__异常抗性.get(类型, 0.0) + x

    def 属性攻击(self, 类型: str) -> None:
        pass

    def 所有异常抗性加成(self, x: float) -> None:
        for 类型 in ['中毒', '灼烧', ' 感电 ', '出血 ', '冰冻 ', '减速 ', '眩晕 ', '诅咒 ', '失明 ', '石化 ', '睡眠 ', '混乱 ', '束缚']:
            self.__异常抗性[类型] = self.__异常抗性.get(类型, 0.0) + x

    def 条件技攻加成(self, 类型: str, x: float) -> None:
        # 消耗无色 不消耗无色
        self.__条件技攻[类型] = self.__条件技攻.get(类型, 1.0) * (1 + x)

    def 条件冷却加成(self, 类型: str, x: float) -> None:
        # 消耗无色 不消耗无色
        self.__条件冷却[类型] = self.__条件冷却.get(类型, 1.0) * (1 - x)

    def 条件冷却恢复加成(self, 类型: str, x: float) -> None:
        self.__条件冷却恢复[类型] = self.__条件冷却恢复.get(类型, 0) + x

    def 指令效果加成(self, 类型: str, x: float) -> None:
        # 所有 消耗无色 不消耗无色  (觉醒技能默认除外)
        self.__指令效果[类型] = self.__指令效果.get(类型, 1.0) * (1 + x)

    def 指令技攻加成(self, x: float, min=1, max=100, exc=[50, 85, 100]) -> None:
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max and i.所在等级 not in exc and i.手搓 == True:
                if i.是否有伤害 == 1:
                    i.倍率 *= (1 + x * self.技能伤害增加增幅)

    # def 指令冷却缩减(self, x: float, min=1, max=100, exc=[50, 85, 100]) -> None:
    #     # 暂未判断是否指令
    #     for i in self.技能栏:
    #         if i.所在等级 >= min and i.所在等级 <= max and i.所在等级 not in exc:
    #             if i.是否有伤害 == 1:
    #                 i.CDR *= (1 - x)

    def 消耗品加成(self, x: float) -> None:
        self.__消耗品效果 += x

    def MP消耗量加成(self, x: float) -> None:
        self.__MP消耗量 += x

    def 攻击强化加成(self, x: float) -> None:
        self.__攻击强化 += x

    def 百分比攻击强化加成(self, x: float) -> None:
        self.__百分比攻击强化 += x

    def buff量加成(self, x: float) -> None:
        self.__buff量 += x

    def 辅助属性加成(self, buff固定力智=0, buff百分比力智=0.0, buff固定三攻=0, buff百分比三攻=0.0, 觉醒固定力智=0, 觉醒百分比力智=0.0, buff量=0, 百分比buff量=0.0):
        self.__buff固定力智 += buff固定力智
        self.__buff百分比力智 *= 1.0 + buff百分比力智
        self.__buff固定三攻 += buff固定三攻
        self.__buff百分比三攻 *= 1.0 + buff百分比三攻
        self.__觉醒固定力智 += 觉醒固定力智
        self.__觉醒百分比力智 *= 1.0 + 觉醒百分比力智
        self.__buff量 += buff量
        self.__百分比buff量 += 百分比buff量

    def 附加伤害加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__附加伤害 += self.附加伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 持续伤害加成(self, x: float) -> None:
        self.__持续伤害 += x

    def 属性附加加成(self, x: float) -> None:
        self.__属性附加 += self.属性附加伤害增加增幅 * x

    def 技能攻击力加成(self, x: float, 辟邪玉加成=1, 适用累加=1) -> None:
        if 辟邪玉加成 == 1:
            if 适用累加 == 0:
                self.__技能攻击力 *= 1 + self.技能伤害增加增幅 * x
            else:
                if self.__技能攻击力累加 > 2:  # 累计已经大于2不再加成
                    self.__技能攻击力 *= 1 + x
                elif self.__技能攻击力累加 + x > 2:  # 此次累计导致大于2，一部分加成，一部分不加成
                    overflow = self.__技能攻击力累加 + x - 2  # 溢出部分
                    self.__技能攻击力 *= 1 + self.技能伤害增加增幅 * \
                        (x - overflow) + overflow
                else:  # 累计后仍小于等于2
                    self.__技能攻击力 *= 1 + self.技能伤害增加增幅 * x
                self.__技能攻击力累加 += x  # 累计计算
        else:
            self.__技能攻击力 *= 1 + x

    def 暴击伤害加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__暴击伤害 += self.暴击伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 伤害增加加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__伤害增加 += self.伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 最终伤害加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__最终伤害 += self.最终伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 百分比力智加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__百分比力智 += self.力量智力增加增幅 * x if 辟邪玉加成 == 1 else x

    def 百分比三攻加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__百分比三攻 += self.物理魔法攻击力增加增幅 * x if 辟邪玉加成 == 1 else x

    def 火属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        if mode == 0:
            self.__火属性强化 += self.所有属性强化增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.__火属性强化 += int(self.所有属性强化增幅 * x)

    def 冰属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        if mode == 0:
            self.__冰属性强化 += self.所有属性强化增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.__冰属性强化 += int(self.所有属性强化增幅 * x)

    def 光属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        if mode == 0:
            self.__光属性强化 += self.所有属性强化增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.__光属性强化 += int(self.所有属性强化增幅 * x)

    def 暗属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        if mode == 0:
            self.__暗属性强化 += self.所有属性强化增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.__暗属性强化 += int(self.所有属性强化增幅 * x)

    def 所有属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        if mode == 0:
            temp = self.所有属性强化增幅 * x if 辟邪玉加成 == 1 else x
        else:
            temp = int(self.所有属性强化增幅 * x)
        self.__所有属性强化(temp)

    def 火属性抗性加成(self, x: int) -> None:
        self.__火属性抗性 += x

    def 冰属性抗性加成(self, x: int) -> None:
        self.__冰属性抗性 += x

    def 光属性抗性加成(self, x: int) -> None:
        self.__光属性抗性 += x

    def 暗属性抗性加成(self, x: int) -> None:
        self.__暗属性抗性 += x

    def 所有属性抗性加成(self, x: int) -> None:
        self.火属性抗性加成(x)
        self.冰属性抗性加成(x)
        self.光属性抗性加成(x)
        self.暗属性抗性加成(x)

    def 攻击速度增加(self, x: float) -> None:
        self.__攻击速度 += x

    def 移动速度增加(self, x: float) -> None:
        self.__移动速度 += x

    def 施放速度增加(self, x: float) -> None:
        self.__施放速度 += x

    def 所有速度增加(self, x: float) -> None:
        self.__攻击速度 += x
        self.__移动速度 += x
        self.__施放速度 += x

    def 命中率增加(self, x: float) -> None:
        self.__命中率 += x

    def 回避率增加(self, x: float) -> None:
        self.__回避率 += x

    def 物理暴击率增加(self, x: float) -> None:
        self.__物理暴击率 += x

    def 魔法暴击率增加(self, x: float) -> None:
        self.__魔法暴击率 += x

    def 暴击率增加(self, x: float) -> None:
        self.物理暴击率增加(x)
        self.魔法暴击率增加(x)

    def buff技能等级加成(self, LV: int, lv: int) -> None:
        # LV级 buff技能等级 + lv
        pass

    def 武器装扮等级加成(self, Lv: int, lv: int) -> None:
        for i in self.技能栏:
            if i.所在等级 == Lv and i.是否主动 == 1 and i.名称 not in ["念兽龙虎啸", "风雷啸", "圣灵符文", "神圣之光"]:
                i.等级加成(lv)

    def 技能获取(self, min: int, max: int, exc=[]) -> None:
        temp = []
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max and i.是否主动 == 1 and i.名称 not in exc:
                temp.append(i.名称)
        return temp

    def 技能等级加成(self, 加成类型: str, min: int, max: int, lv: int, exc=[int]) -> None:
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max and i.所在等级 not in exc:
                if 加成类型 == '所有':
                    i.等级加成(lv)
                else:
                    if i.是否主动 == 1:
                        i.等级加成(lv)

    def 技能冷却缩减(self, min: int, max: int, x: float, exc=[int]) -> None:
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max and i.所在等级 not in exc:
                if i.是否有伤害 == 1:
                    i.CDR *= (1 - x)

    def 加算冷却缩减(self, x: float) -> None:
        self.__加算冷却缩减 += x

    def 技能恢复加成(self, min: int, max: int, x: float, exc=[int]) -> None:
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max and i.所在等级 not in exc:
                if i.是否有伤害 == 1:
                    i.恢复 += x

    def 技能倍率加成(self, min: int, max: int, x: float, exc=[int]) -> None:
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max and i.所在等级 not in exc:
                if i.是否有伤害 == 1:
                    i.倍率 *= (1 + x * self.技能伤害增加增幅)

    def 单技能加成(self, 名称: str, 倍率=1.0, CD=1.0, lv=0) -> None:
        i = self.get_skill_by_name(名称)
        i.等级加成(lv)
        if i.是否有伤害 == 1:
            i.倍率 *= 倍率
            i.CDR *= CD

    def __所有属性强化(self, x: float) -> None:
        self.__火属性强化 += x
        self.__冰属性强化 += x
        self.__光属性强化 += x
        self.__暗属性强化 += x

    # endregion

    # region 面板相关函数

    # 基础力量智力(站街力量智力)
    def 站街力量(self) -> int:
        return int(self.__力量)

    def 站街智力(self) -> int:
        return int(self.__智力)

    def MP消耗倍率(self) -> float:
        return self.__MP消耗量

    def 火属性强化(self) -> float:
        return self.__火属性强化

    def 冰属性强化(self) -> float:
        return self.__冰属性强化

    def 光属性强化(self) -> float:
        return self.__光属性强化

    def 暗属性强化(self) -> float:
        return self.__暗属性强化

    def 火属性抗性(self) -> float:
        return self.__火属性抗性

    def 冰属性抗性(self) -> float:
        return self.__冰属性抗性

    def 光属性抗性(self) -> float:
        return self.__光属性抗性

    def 暗属性抗性(self) -> float:
        return self.__暗属性抗性
    # 新词条计算的力量智力

    def __基础面板力量(self) -> float:
        return (self.__力量 + int((self.__力量 - self.__基础力量) * self.系统奶系数 + self.系统奶基数))

    def __基础面板智力(self) -> float:
        return (self.__智力 + int((self.__智力 - self.__基础智力) * self.系统奶系数 + self.系统奶基数))

    # 旧词条计算的力量智力(图内力量智力)

    def 面板力量(self) -> float:
        return self.__基础面板力量() * (1 + self.__百分比力智)

    def 面板智力(self) -> float:
        return self.__基础面板智力() * (1 + self.__百分比力智)

    # 站街生效的技能三攻倍率

    def __站街物理攻击力倍率(self) -> float:
        站街物理攻击倍率 = 1.0
        for i in self.技能栏:
            if hasattr(i, '物理攻击力倍率'):
                倍率 = i.物理攻击力倍率(self.武器类型)
                if 倍率 != 1 and 倍率 is not None:
                    站街物理攻击倍率 *= 倍率
        return 站街物理攻击倍率

    def __站街魔法攻击力倍率(self) -> float:
        站街魔法攻击倍率 = 1.0
        for i in self.技能栏:
            if hasattr(i, '魔法攻击力倍率'):
                倍率 = i.魔法攻击力倍率(self.武器类型)
                if 倍率 != 1 and 倍率 is not None:
                    站街魔法攻击倍率 *= 倍率
        return 站街魔法攻击倍率

    def __站街独立攻击力倍率(self) -> float:
        站街独立攻击倍率 = 1.0
        for i in self.技能栏:
            if hasattr(i, '独立攻击力倍率'):
                倍率 = i.独立攻击力倍率(self.武器类型)
                if 倍率 != 1 and 倍率 is not None:
                    站街独立攻击倍率 *= 倍率
        return 站街独立攻击倍率

    # 站街三攻

    def 站街物理攻击力(self) -> float:
        return self.__物理攻击力 * self.__站街物理攻击力倍率()

    def 站街魔法攻击力(self) -> float:
        return self.__魔法攻击力 * self.__站街魔法攻击力倍率()

    def 站街独立攻击力(self) -> float:
        return self.__独立攻击力 * self.__站街独立攻击力倍率()

    # 新词条计算的三攻(旧词条需要额外乘百分比三攻)

    def __基础面板物理攻击力(self) -> float:
        面板物理攻击 = self.__物理攻击力
        for i in self.技能栏:
            面板物理攻击 *= i.物理攻击力倍率进图(self.武器类型)
        return 面板物理攻击 * self.__站街物理攻击力倍率()

    def __基础面板魔法攻击力(self) -> float:
        面板魔法攻击 = self.__魔法攻击力
        for i in self.技能栏:
            面板魔法攻击 *= i.魔法攻击力倍率进图(self.武器类型)
        return 面板魔法攻击 * self.__站街魔法攻击力倍率()

    def __基础面板独立攻击力(self) -> float:
        面板独立攻击 = self.__独立攻击力
        for i in self.技能栏:
            面板独立攻击 *= i.独立攻击力倍率进图(self.武器类型)
        return 面板独立攻击 * self.__站街独立攻击力倍率()

    # 图内显示的三攻(不参与伤害计算)

    def 面板物理攻击力(self) -> float:
        面板物理攻击 = self.__基础面板物理攻击力() * (1 + self.__百分比三攻) * (
            1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        return 面板物理攻击

    def 面板魔法攻击力(self) -> float:
        面板魔法攻击 = self.__基础面板魔法攻击力() * (1 + self.__百分比三攻) * (
            1 + self.年宠技能 * 0.10 + self.斗神之吼秘药 * 0.12 + self.白兔子技能 * 0.20)
        return 面板魔法攻击

    def 面板独立攻击力(self) -> float:
        面板独立攻击 = self.__基础面板独立攻击力() * (1 + self.__百分比三攻)
        return 面板独立攻击
    # endregion

    # region 其它函数
    #     def get_skill_by_name(self, name) -> 技能 | 主动技能 | 被动技能:
    def get_skill_by_name(self, name) -> Union[技能, 主动技能, 被动技能]:
        return self.技能栏[self.技能序号.get(name, 0)]

    def 已穿戴神话(self):
        for i in self.装备栏:
            temp = equ.get_equ_by_id(i)
            if temp.品质 == '神话':
                return True
        return False

    def 穿戴低于105(self):
        for i in self.装备栏:
            temp = equ.get_equ_by_id(i)
            if temp.等级 < 105 and temp.部位 not in ['称号', '宠物']:
                return True
        return False

    def 获取强化等级(self, part=[]):
        num = 0
        temp = part
        if len(temp) == 0:
            temp += 部位列表
        for i in temp:
            num += self.打造详情.get(i, {}).get('cursed_number', 0)
        return num

    def 获取改造等级(self, part=[]):
        num = 0
        temp = part
        if len(temp) == 0:
            temp += 部位列表
        for i in temp:
            num += self.打造详情.get(i, {}).get('wisdom_number', 0)
        return num
    # endregion

    # 打造设置

    def __打造设置(self, setinfo):
        self.打造详情 = setinfo
        for i in 部位列表 + ('称号', '宠物', '光环', '武器装扮', '皮肤', '宠物装备-红', '宠物装备-绿', '宠物装备-蓝', '快捷装备'):
            from core.baseClass.enchanting import get_encfunc_by_id
            id = setinfo.get(i, {}).get('enchanting', 0)
            self.部位附魔[i] = get_encfunc_by_id(id)

    def __技能队列设置(self, setinfo):
        self.技能队列 = []
        for item in setinfo:
            self.技能队列.append({
                '名称': item['name'],
                '无色消耗': self.get_skill_by_name(item['name']).无色消耗,
                '倍率': 1.0,
                '等级变化': 0,
                'CDR': 1.0,
                '形态': item.get('mode', '')
            })

    # 设置技能相关参数
    def __skill_set(self, setinfo):
        for i in setinfo:
            k = self.get_skill_by_name(i['name'])
            k.等级 = i['level']
            k.TP等级 = i['tp']
            k.手搓 = i['direct']
            k.手搓指令数 = i['directNumber']
            k.count = i['count']

    # 设置装备选项参数
    def __equ_chose_set(self, setinfo):
        equ.set_func_chose(setinfo)
        # for i in setinfo:
        #    equ.set_func_chose({i['id']: i['select']})

    def __hotkey_set(self, setinfo):
        self.hotkey = setinfo

    def __set_char(self, info):
        self.类型 = info['carry_type'] if self.类型 != '辅助' else self.类型
        self.buff = info['buff_ratio'] / 100 + 1
        self.护石栏 = info['talisman_set']
        self.符文 = info['rune_set']
        pass

    # 设置穿戴的装备

    def __穿戴装备(self, idlist):
        self.装备栏 = []
        self.部位装备 = {}
        for i in idlist:
            装备 = equ.get_equ_by_id(i)
            self.部位装备.update({装备.部位: i})
        for k in self.部位装备.keys():
            self.装备栏.append(self.部位装备[k])

    def __穿戴装扮(self, info):
        self.装扮栏 = {}
        self.装扮选项 = {}
        for i in info:
            self.装扮栏[i] = info[i].get('id', 0)
            self.装扮选项[i] = info[i].get('option', 0)
        # print(len(self.装扮栏))

    # region 伤害计算相关函数
    def __计算前预处理(self):
        self.__辟邪玉计算()
        self.护石计算()
        self.__符文计算()
        self.__装备属性计算()
        self.skills_passive = {}
        for i in self.技能栏:
            self.skills_passive[i.名称] = {
                "info": [],
                "lv": i.等级
            }
        self.职业特殊计算()
        if self.类型 != '辅助':
            self.__CD倍率计算()
            self.__加算冷却计算()
            self.__被动倍率计算()
            self.伤害指数计算()

    def 适用数值计算(self):
        进图智力 = 0
        进图体力 = 0
        进图精神 = 0
        for skill in self.技能栏:
            if skill.是否启用:
                结算 = skill.结算统计(self)
                if skill.站街生效:
                    self.__智力 += 结算[2]
                    self.__体力 += 结算[3]
                    self.__精神 += 结算[4]
                    print('zhanjie', self.__体力)
                else:
                    进图智力 += 结算[2]
                    进图体力 += 结算[3]
                    进图精神 += 结算[4]
                    print('jintu', 进图体力)

        进图 = 0
        BUFF补正 = 0

        if self.适用属性 == '体力':
            进图 = self.__体力 + 进图体力
            BUFF补正 = self.__BUFF补正体力
        elif self.适用属性 == '精神':
            进图 = self.__精神 + 进图精神
            BUFF补正 = self.__BUFF补正精神
        else:
            进图 = self.__智力 + 进图智力
            BUFF补正 = self.__BUFF补正智力

        awake = self.get_skill_by_name('一次觉醒')
        buff = self.get_skill_by_name('BUFF')

        awake.适用数值 = 进图
        awake.一觉力智 = self.__觉醒固定力智
        awake.一觉力智per = self.__觉醒百分比力智

        buff.适用数值 = 进图 + BUFF补正
        buff.BUFF力智per = self.__buff百分比力智
        buff.BUFF力智 = self.__buff固定力智
        buff.BUFF三攻per = self.__buff百分比三攻
        buff.BUFF三攻 = self.__buff固定三攻

        self.适用数值 = 进图
        print('copaosee:', self.适用数值, [
              self.__智力, self.__体力, self.__精神], 进图, BUFF补正)

    def 站街系数(self):
        if self.适用属性 == '体力':
            return self.__体力
        elif self.适用属性 == '精神':
            return self.__精神
        return self.__智力

    def 提升率计算(self, 总数据):

        力智合计 = 0
        三攻合计 = 0

        for i in 总数据:
            力智合计 += i[0]
            三攻合计 += i[1]

        x1 = (
            (self.辅助对象力智 +
             (self.辅助对象力智 - 950) * self.系统奶系数 + self.系统奶基数) / 250 + 1) * self.辅助对象三攻

        x2 = ((self.辅助对象力智 +
               (self.辅助对象力智 - 950) * self.系统奶系数 + self.系统奶基数 + 力智合计) / 250 +
              1) * (self.辅助对象三攻 + 三攻合计)
        return [x2 / x1 * 100, int(self.站街系数()), 力智合计, 三攻合计]

    def BUFF量(self):
        return self.__buff量 * (1 + self.__百分比buff量)

    def 辅助计算(self):
        self.适用数值计算()
        data = {}
        data['无色消耗'] = 0

        skills = {}

        values = []

        for i in self.技能栏:
            rs = i.结算统计(self)[:2]
            k = {}
            k['name'] = i.名称
            k['data'] = rs

            if hasattr(i, '适用数值'):
                k['apply_status'] = i.适用数值
            if sum(rs) > 0:
                values.append(rs)
                skills[i.名称] = {'name': i.名称, 'level': i.等级, 'data': rs}

        结果 = self.提升率计算(values)

        data['total_data'] = 结果[0]
        data['buffer_addition'] = 结果
        data['skills'] = skills

        return data

    def 结果计算(self):
        if self.类型 == '辅助':
            return self.辅助计算()
        else:
            return self.伤害计算()

    def 职业特殊计算(self):
        pass

    def 伤害计算(self):
        data = {}
        total_data = 0

        skill_dict = {}
        无色消耗 = 0
        for i in self.技能队列:
            k = self.get_skill_by_name(i['名称'])
            if k.是否有伤害 == 1:
                temp = skill_dict.get(k.名称, {})
                if k.名称 not in data.keys():
                    temp['rate'] = k.被动倍率
                    temp['cd'] = k.等效CD(
                        武器类型=self.武器类型, 输出类型=self.类型, 额外CDR=i['CDR'])
                    temp['mp'] = k.MP消耗(
                        武器类型=self.武器类型, 输出类型=self.类型, 额外倍率=self.__MP消耗量)
                    temp['atk_rate'] = k.等效百分比(武器类型=self.武器类型)
                    temp['cosume_cube_frag'] = k.无色消耗
                    temp['level'] = k.等级
                直伤 = k.等效百分比(
                    武器类型=self.武器类型, 额外等级=i['等级变化'], 额外倍率=i['倍率'], 伤害类型="直伤", 形态=i['形态'], char=self)

                # 直伤处理：直伤伤害*比例*系数
                damage = 直伤 * self.伤害指数 * k.被动倍率 * \
                    (self.__伤害比例.get("直伤", 0.0)) / 100
                for item in ['中毒', '灼烧', '感电', '出血']:
                    系数 = self.__伤害系数.get(item, 0.0)
                    # 出血 叠层 1层1%出血伤害 满10%
                    if item == '出血':
                        系数 *= 1.1
                    # 直伤转换的异常处理：直伤伤害*异常比例*异常系数
                    damage += 直伤 * self.伤害指数 * k.被动倍率 * \
                        (self.__伤害比例.get(item, 0.0) * 系数) / 100
                    # 异常伤害处理：异常伤害*异常系数
                    damage += k.等效百分比(
                        武器类型=self.武器类型,  额外等级=i['等级变化'], 额外倍率=i['倍率'], 伤害类型=item, 形态=i['形态'], char=self) * self.伤害指数 * k.被动倍率*系数 / 100
                total_data += damage
                temp['name'] = k.名称
                temp['damage'] = temp.get('damage', 0) + damage
                temp['count'] = temp.get('count', 0) + 1
                skill_dict[k.名称] = temp
                if k.名称 not in ['爆裂弹', '杀意波动', '万毒噬心诀']:
                    无色消耗 += i['无色消耗']
        data['skills_passive'] = {}
        for i in self.技能栏:
            if i.关联技能 != ['无'] or i.冷却关联技能 != ['无']:
                temp = {}
                temp['lv'] = i.等级
                temp['name'] = i.名称
                data['skills_passive'][i.名称] = temp
        data['skills'] = skill_dict
        data['total_data'] = total_data
        data['无色消耗'] = 无色消耗
        return data

    def __装备属性计算(self):
        self.__装备基础()
        self.__时装基础()
        self.__附魔计算()
        self.__杂项计算()
        self.__徽章计算()
        self.__装备词条计算()

    def __时装基础(self):
        时装品级列表 = {}
        for 部位 in self.装扮栏:
            id = self.装扮栏[部位]
            时装 = 装扮集合[id]
            时装.效果(角色=self, 选项=self.装扮选项[部位])
            时装品级列表[时装.套装] = 时装品级列表.get(时装.套装, 0) + 1

        套装集合: List[装扮套装] = []

        for 套装 in 装扮套装集合:
            数量 = 时装品级列表.get(套装.名称, 0)
            if 数量 > 0:
                if 数量 >= 套装.所需数量:
                    查找 = len([i for i in 套装集合 if hasattr(i, '兼容于') and i.兼容于 ==
                              套装.名称 and i.所需数量 == 套装.所需数量])
                    if 查找 == 0:
                        套装集合.append(套装)
                else:
                    if hasattr(套装, '兼容于') and 套装.兼容于 is not None:
                        数量 += 时装品级列表.get(套装.兼容于, 0)
                        时装品级列表[套装.兼容于] = 数量
                        时装品级列表.pop(套装.名称)
        for 套装 in 套装集合:
            套装.效果(self)

        pass

    def __辟邪玉计算(self):
        if 'jade' not in self.打造详情.keys():
            return
        setinfo = self.打造详情['jade']
        for i in ['jade_First', 'jade_Second', 'jade_Third', 'jade_Fourth']:
            if i + '_type' in setinfo.keys():
                try:
                    id = setinfo[i + '_type']
                    value = float(setinfo[i + '_value'])
                except:
                    id = 0
                    value = 0
                from core.baseClass.jade import get_jadefunc_by_id
                func = get_jadefunc_by_id(id)
                func(self, value=value)
                # 打印相关函数和效果

    def 护石计算(self):
        for item in self.护石栏:
            try:
                if not item is None and item != '' and item != '无':
                    self.get_skill_by_name(item).装备护石()
            except:
                pass

    def __符文计算(self):
        for item in self.符文:
            if not item is None and item != '':
                skill_name: str = item[0:-1]
                type = item[-1]
                skill = self.get_skill_by_name(skill_name)

                if skill is not None:
                    # 紫
                    if type == "1":
                        skill.倍率 *= 1.04
                        # 红
                    if type == "2":
                        skill.倍率 *= 1.06
                        skill.CDR *= 1.04
                        # 绿
                    if type == "3":
                        skill.倍率 *= 0.96
                        skill.CDR *= 0.93
                        # 蓝
                    if type == "4":
                        skill.CDR *= 0.95
                else:
                    print("skill not found {skill_name}".format(skill_name))
            pass

    def __杂项计算(self, mode=0):
        if 'others' not in self.打造详情.keys():
            return
        setinfo = self.打造详情['others']
        # 收集箱
        try:
            from core.baseClass.sundry import get_sundriesfunc_by_id
            func = get_sundriesfunc_by_id(setinfo['SJX_TYPE'])
            # print(func)
            func(self, 0, False, setinfo['SJX_XY'], setinfo['SJX_SQ'])
        except:
            pass
        # 勋章
        try:
            from core.baseClass.sundry import get_sundriesfunc_by_id
            func = get_sundriesfunc_by_id(setinfo['XZ_TYPE'])
            func(self, 0, False, setinfo['XZ_SHZ'], setinfo['XZ_QH'])
        except:
            pass
        for i in setinfo.keys():
            if i.startswith('SJX') or i.startswith('XZ'):
                pass
            else:
                try:
                    id = setinfo[i]
                    from core.baseClass.sundry import get_sundriesfunc_by_id
                    func = get_sundriesfunc_by_id(id)
                    # 站街
                    func(self)
                    # 进图
                    func(self, mode=1)
                except:
                    pass

    def __徽章计算(self):
        idlist = []
        for i in 部位列表:  # ('皮肤', '光环', '武器装扮', )
            if i in self.打造详情.keys():
                temp = self.打造详情[i]
                for j in ['socket_left', 'socket_right']:
                    id = temp.get(j, 0)
                    if id == 0:
                        pass
                    elif str(id).isdigit():
                        idlist.append(id)
                    else:
                        # 白金技能等级加成处理 id:技能名称
                        self.get_skill_by_name(id).等级 += 1
                        self.基础属性加成(四维=8)
                        pass
        for i in idlist:
            from core.baseClass.emblems import get_embfunc_by_id
            func = get_embfunc_by_id(i)
            func(self)
            # 打印相关函数和效果
            # print('{}: {}'.format(func, func(self, text=TRUE)))

    def __附魔计算(self):
        for i in self.部位附魔.keys():
            func = self.部位附魔[i]
            func(self)
            func(self, mode=1)
            # 打印相关函数和效果
            # print('{}: {}: {}'.format(i, func, func(self, text=TRUE)))

    def __装备基础(self):
        for id in self.装备栏:
            temp = equ.get_equ_by_id(id)
            if '甲' in temp.类型:
                self.__防具计算(temp)
            elif temp.类型 == '首饰':
                self.__首饰计算(temp)
            elif temp.类型 == '特殊装备':
                self.__特殊装备计算(temp)
            elif temp.部位 == '武器':
                self.__武器计算(temp)
            elif temp.部位 in ['称号', '宠物']:
                self.__称号宠物计算(temp)
            self.__增幅计算(temp)
        pass

    def __防具精通计算(self, temp: equipment) -> float:
        部位 = temp.部位
        return 精通计算(temp.等级, temp.品质, self.打造详情.get(部位, {}).get('cursed_number', 0), 部位)
        # if temp.所属套装 != '智慧产物':
        #    return 精通计算(temp.等级, temp.品质, self.打造详情.get(部位, {}).get('cursed_number', 0), 部位)
        # else:
        #    return 精通计算(temp.等级, temp.品质, self.打造详情.get(部位, {}).get('wisdom_number', 0), 部位)

    def __防具计算(self, temp: equipment) -> None:
        力量 = temp.力量[self.防具类型]
        智力 = temp.智力[self.防具类型]

        精通数值 = self.__防具精通计算(temp)
        if '力量' in self.防具精通属性:
            力量 += 精通数值
        if '智力' in self.防具精通属性:
            智力 += 精通数值

        if temp.等级 == 105:

            if self.类型 == '辅助':
                self.技能等级加成('主动', 30, 30, 1)
                self.技能等级加成('主动', 50, 50, 1)
        self.基础属性加成(力量=力量, 智力=智力)

    def __增幅计算(self, temp: equipment) -> None:
        if self.打造详情.get(temp.部位, {}).get('cursed_type', 1) == 1:
            x = 增幅计算(temp.等级, temp.品质, self.打造详情.get(
                temp.部位, {}).get('cursed_number', 0))
            if self.类型 == '物理百分比' or self.类型 == '物理固伤':
                self.基础属性加成(力量=x)
            elif self.类型 == '魔法百分比' or self.类型 == '魔法固伤':
                self.基础属性加成(智力=x)
            elif self.类型 == '辅助':
                if self.适用属性 == '体力':
                    self.基础属性加成(体力=x)
                elif self.适用属性 == '精神':
                    self.基础属性加成(精神=x)
                else:
                    self.基础属性加成(智力=x)
        # if self.是否增幅[i] and temp.所属套装 != '智慧产物':
        #    x = 增幅计算(temp.等级, temp.品质, self.强化等级[i])

    def __称号宠物计算(self, temp: equipment) -> None:
        self.基础属性加成(**temp.__dict__)

    def __首饰计算(self, temp: equipment) -> None:
        self.基础属性加成(**temp.__dict__)
        if temp.等级 == 105 and self.类型 == '辅助':
            self.技能等级加成('主动', 30, 30, 1)
            self.技能等级加成('主动', 50, 50, 1)

    def __特殊装备计算(self, temp: equipment) -> None:
        self.基础属性加成(**temp.__dict__)
        if temp.等级 == 105 and self.类型 == '辅助':
            self.技能等级加成('主动', 30, 30, 1)
            self.技能等级加成('主动', 50, 50, 1)
            if temp.品质 == '史诗' and temp.部位 == '魔法石':
                self.技能等级加成('主动', 50, 50, 1)
        # 耳环
        if temp.部位 == '耳环':
            # if temp.所属套装 != '智慧产物':
            x = 耳环计算(temp.等级, temp.品质, self.打造详情.get(
                temp.部位, {}).get('cursed_number', 0))
            self.基础属性加成(三攻=x)
        # 辅助装备、魔法石
        else:
            # if temp.所属套装 != '智慧产物':
            x = 左右计算(temp.等级, temp.品质, self.打造详情.get(
                temp.部位, {}).get('cursed_number', 0))
            self.基础属性加成(四维=x)

    def __武器计算(self, temp: equipment) -> None:
        self.基础属性加成(**temp.__dict__)
        if temp.等级 == 105 and self.类型 == '辅助':
            self.技能等级加成('主动', 30, 30, 3)
            self.技能等级加成('主动', 50, 50, 2)
            if temp.品质 == '史诗':
                self.技能等级加成('主动', 50, 50, 1)
        # if temp.所属套装 != '智慧产物':
        info = self.打造详情.get(temp.部位, {})
        物理攻击力 = 武器强化计算(temp.等级, temp.品质, info.get('cursed_number', 0), temp.类型,
                       '物理')
        魔法攻击力 = 武器强化计算(temp.等级, temp.品质, info.get('cursed_number', 0), temp.类型,
                       '魔法')
        独立攻击力 = 锻造计算(temp.等级, temp.品质, info.get('dz_number', 0))

        四维 = 0
        if self.类型 == '辅助':
            四维 = 锻造四维(temp.等级, temp.品质, info.get('dz_number', 0))

        self.基础属性加成(物理攻击力=物理攻击力, 魔法攻击力=魔法攻击力, 独立攻击力=独立攻击力, 四维=四维)

    def 职业装备特殊计算(self) -> None:
        pass

    def __装备词条计算(self):
        # 攻击强化相关计算
        for i in 部位列表:
            temp = []
            for j in ["growth_first", "growth_second", "growth_third", "growth_fourth"]:
                temp.append(self.打造详情.get(i, {}).get(j, 1))
            self.词条等级[i] = temp
        成长词条组合 = equ.get_damagelist_by_idlist(self.装备栏, self.自定义词条)

        for 部位, 序号, atk, buff in 成长词条组合:
            等级 = self.词条等级[部位][序号]
            self.攻击强化加成(成长词条计算(atk, 等级))
            self.buff量加成(奶成长词条计算(buff, 等级))
        # 词条效果相关计算
        for func, 部位, 序号 in equ.get_func_list_by_idlist(self.装备栏, self.自定义词条):
            if 序号 >= 0:
                等级 = self.词条等级[部位][序号]
            else:
                等级 = 0
            func(self, part=部位, lv=等级)  # 站街效果
            func(self, mode=1, part=部位, lv=等级)  # 进图效果
            # 打印相关函数和效果
            # print('{}(lv.{}): {} {}'.format(部位, 等级, func, func(self, text=TRUE)))

    def __被动倍率计算(self):
        for i in self.技能栏:
            i.被动倍率 = 1
        for i in self.技能栏:
            for index in range(0, 4):
                index = "" if index == 0 else str(index+1)
                关联技能 = getattr(i, "关联技能"+index, ["无"])
                非关联技能 = getattr(i, "非关联技能"+index, ["无"])
                try:
                    加成倍率 = eval("i.加成倍率"+index+"(self.武器类型)")
                except:
                    加成倍率 = 1.0
                try:
                    if 加成倍率 != 1:
                        self.skills_passive[i.名称]['info'].append({
                            "type": "倍率",
                            "info": eval("i.加成描述"+index+"(self.武器类型)")})
                except:
                    pass
                if 关联技能 != ['无']:
                    if 关联技能 == ['所有']:
                        for j in self.技能栏:
                            if j.是否有伤害 == 1:
                                j.被动倍率 *= 加成倍率
                    else:
                        # print(self.技能序号)
                        for k in 关联技能:
                            self.技能栏[self.技能序号[k]
                                     ].被动倍率 *= 加成倍率
                if 非关联技能 != ['无']:
                    if 非关联技能 == ['所有']:
                        for j in self.技能栏:
                            if j.是否有伤害 == 1:
                                j.被动倍率 /= 加成倍率
                    else:
                        for k in 非关联技能:
                            self.技能栏[self.技能序号[k]].被动倍率 /= 加成倍率

            # if i.关联技能 != ['无']:
            #     if i.关联技能 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.被动倍率 *= i.加成倍率(self.武器类型)
            #     else:
            #         for k in i.关联技能:
            #             self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率(self.武器类型)
            # if i.非关联技能 != ['无']:
            #     if i.非关联技能 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.被动倍率 /= i.加成倍率(self.武器类型)
            #     else:
            #         for k in i.非关联技能:
            #             self.技能栏[self.技能序号[k]].被动倍率 /= i.加成倍率(self.武器类型)

            # if i.关联技能2 != ['无']:
            #     if i.关联技能2 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.被动倍率 *= i.加成倍率2(self.武器类型)
            #     else:
            #         for k in i.关联技能2:
            #             self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率2(self.武器类型)

            # if i.非关联技能2 != ['无']:
            #     if i.非关联技能2 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.被动倍率 /= i.加成倍率2(self.武器类型)
            #     else:
            #         for k in i.非关联技能2:
            #             self.技能栏[self.技能序号[k]].被动倍率 /= i.加成倍率2(self.武器类型)

            # if i.关联技能3 != ['无']:
            #     if i.关联技能3 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.被动倍率 *= i.加成倍率3(self.武器类型)
            #     else:
            #         for k in i.关联技能3:
            #             self.技能栏[self.技能序号[k]].被动倍率 *= i.加成倍率3(self.武器类型)

            # if i.非关联技能3 != ['无']:
            #     if i.非关联技能3 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.被动倍率 /= i.加成倍率3(self.武器类型)
            #     else:
            #         for k in i.非关联技能3:
            #             self.技能栏[self.技能序号[k]].被动倍率 /= i.加成倍率3(self.武器类型)

    def __加算冷却计算(self):
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                i.CDR *= (1 - self.__加算冷却缩减)

    def __CD倍率计算(self):
        for i in self.技能栏:
            for index in range(0, 4):
                index = "" if index == 0 else str(index+1)
                关联技能 = getattr(i, "冷却关联技能"+index, ["无"])
                非关联技能 = getattr(i, "非冷却关联技能"+index, ["无"])
                try:
                    加成倍率 = eval("i.CD缩减倍率"+index+"(self.武器类型)")
                except:
                    加成倍率 = 1.0
                try:
                    if 加成倍率 != 1:
                        self.skills_passive[i.名称]['info'].append({
                            "type": "CDR",
                            "info": eval(
                                "i.CD缩减描述"+index+"(self.武器类型)")
                        })
                except:
                    pass
                if 关联技能 != ['无']:
                    if 关联技能 == ['所有']:
                        for j in self.技能栏:
                            if j.是否有伤害 == 1:
                                j.CDR *= 加成倍率
                    else:
                        for k in 关联技能:
                            self.技能栏[self.技能序号[k]
                                     ].CDR *= 加成倍率
                if 非关联技能 != ['无']:
                    if 非关联技能 == ['所有']:
                        for j in self.技能栏:
                            if j.是否有伤害 == 1:
                                j.CDR /= 加成倍率
                    else:
                        for k in 非关联技能:
                            self.技能栏[self.技能序号[k]].CDR /= 加成倍率
            # if i.冷却关联技能 != ['无']:
            #     if i.冷却关联技能 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.CDR *= i.CD缩减倍率(self.武器类型)
            #     else:
            #         for k in i.冷却关联技能:
            #             self.技能栏[self.技能序号[k]].CDR *= i.CD缩减倍率(self.武器类型)
            # if i.非冷却关联技能 != ['无']:
            #     if i.非冷却关联技能 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.CDR /= i.CD缩减倍率(self.武器类型)
            #     else:
            #         for k in i.非冷却关联技能:
            #             self.技能栏[self.技能序号[k]].CDR /= i.CD缩减倍率(self.武器类型)
            # if i.冷却关联技能2 != ['无']:
            #     if i.冷却关联技能2 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.CDR *= i.CD缩减倍率2(self.武器类型)
            #     else:
            #         for k in i.冷却关联技能2:
            #             self.技能栏[self.技能序号[k]].CDR *= i.CD缩减倍率2(self.武器类型)
            # if i.非冷却关联技能2 != ['无']:
            #     if i.非冷却关联技能2 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.CDR /= i.CD缩减倍率2(self.武器类型)
            #     else:
            #         for k in i.非冷却关联技能2:
            #             self.技能栏[self.技能序号[k]].CDR /= i.CD缩减倍率2(self.武器类型)
            # if i.冷却关联技能3 != ['无']:
            #     if i.冷却关联技能3 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.CDR *= i.CD缩减倍率3(self.武器类型)
            #     else:
            #         for k in i.冷却关联技能3:
            #             self.技能栏[self.技能序号[k]].CDR *= i.CD缩减倍率3(self.武器类型)
            # if i.非冷却关联技能3 != ['无']:
            #     if i.非冷却关联技能3 == ['所有']:
            #         for j in self.技能栏:
            #             if j.是否有伤害 == 1:
            #                 j.CDR /= i.CD缩减倍率3(self.武器类型)
            #     else:
            #         for k in i.非冷却关联技能3:
            #             self.技能栏[self.技能序号[k]].CDR /= i.CD缩减倍率3(self.武器类型)

    def __属性倍率计算(self):
        # 火、冰、光、暗
        self.属性倍率组 = []
        self.属性倍率组.append(1.05 + 0.0045 * int(self.__火属性强化 - self.火抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.__冰属性强化 - self.冰抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.__光属性强化 - self.光抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.__暗属性强化 - self.暗抗输入))
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

    def __面板系数计算(self, mode=1):
        # 基础面板 不含百分比力智和百分比三攻
        if mode == 0:
            if self.类型 == '物理百分比':
                return int((self.__基础面板力量() / 250 + 1) * self.__基础面板物理攻击力())
            elif self.类型 == '魔法百分比':
                return int((self.__基础面板智力() / 250 + 1) * self.__基础面板魔法攻击力())
            elif self.类型 == '物理固伤':
                return int((self.__基础面板力量() / 250 + 1) * self.__基础面板独立攻击力())
            elif self.类型 == '魔法固伤':
                return int((self.__基础面板智力() / 250 + 1) * self.__基础面板独立攻击力())
        # 旧版算法 不含斗神、宠物技能等
        else:
            if self.类型 == '物理百分比':
                return int((self.面板力量() / 250 + 1) * self.__基础面板物理攻击力() * (1 + self.__百分比三攻))
            elif self.类型 == '魔法百分比':
                return int((self.面板智力() / 250 + 1) * self.__基础面板魔法攻击力() * (1 + self.__百分比三攻))
            elif self.类型 == '物理固伤':
                return int((self.面板力量() / 250 + 1) * self.__基础面板独立攻击力() * (1 + self.__百分比三攻))
            elif self.类型 == '魔法固伤':
                return int((self.面板智力() / 250 + 1) * self.__基础面板独立攻击力() * (1 + self.__百分比三攻))

    def 伤害指数计算(self):

        防御 = max(self.防御输入 - self.__固定减防, 0) * (1 - self.__百分比减防)

        基准倍率 = 1.5 * self.buff * (1 - 防御 / (防御 + 200 * self.等级))

        self.__属性倍率计算()

        # 基础面板 不含百分比力智和百分比三攻
        基础面板 = self.__面板系数计算(mode=0)
        旧版面板 = self.__面板系数计算(mode=1)

        新 = self.__攻击强化 * (1 + self.__百分比攻击强化) * 0.001
        旧 = 1 + int((self.__伤害增加 + 0.00000001) * 100) / 100  # 避免出现浮点数取整BUG
        旧 *= 1 + self.__暴击伤害
        旧 *= 1 + self.__最终伤害
        旧 *= 1 + self.__持续伤害
        旧 *= 1 + self.__附加伤害 + self.__属性附加 * self.属性倍率

        self.伤害指数 = (新 * 基础面板 + 旧 * 旧版面板) * self.__技能攻击力 * self.属性倍率 * 基准倍率

        # 7.8日,伤害数据压缩
        self.伤害指数 /= 1000
    # endregion

    def calc_init(self, info, equipList: List[int] = []):
        # 获取打造数据
        self.__打造设置(info['forge_set'])
        self.__技能队列设置(info['skill_que'])
        # 设置职业信息
        self.__set_char(info)
        # 自定义词条部分
        self.自定义词条 = info['customize']
        #  时装设置
        self.__穿戴装扮(info['dress_set'])
        # 获取装备列表
        self.__穿戴装备(equipList)
        # 获取技能数据
        self.__skill_set(info['skill_set'])
        # 获取装备选项数据
        self.__equ_chose_set(info['trigger_set'])

        self.__hotkey_set(info['hotkey_set'])

    def jade_upgrade(self):
        temp = []
        from core.baseClass.jade import get_jade_setinfo, get_jadefunc_by_id
        for jade in get_jade_setinfo():
            if jade["id"] > 26001 and jade["id"] < 26200:
                char = deepcopy(self)
                func = get_jadefunc_by_id(jade["id"])
                func(char, value=jade["max"])
                char.__计算前预处理()
                temp.append({
                    "id": jade["id"],
                    "name": jade["props"] + "  " + ("" if jade["max"] == 1 else("+" + str(jade["max"]))) + jade["unit"],
                    "damage": round(char.伤害计算()["total_data"], 2)
                })
        return temp

    def calc(self, setName: str = 'set', equipList: List[int] = [], withJade=False):
        info = store.get("/{}/setinfo/{}".format(self.实际名称, setName))
        self.calc_init(info, equipList)
        jade = []
        if withJade and self.类型 != '辅助':
            jade = self.jade_upgrade()
        self.__计算前预处理()
        temp = self.结果计算()
        calc_info = {}

        if self.类型 == '辅助':
            calc_info[self.适用属性] = self.站街系数()
        # print(self.skills_passive)
        elif self.类型 == '物理百分比':
            calc_info['力量'] = self.站街力量()
            calc_info['物理攻击'] = self.站街物理攻击力()
        elif self.类型 == '魔法百分比':
            calc_info['智力'] = self.站街智力()
            calc_info['魔法攻击'] = self.站街魔法攻击力()
        elif self.类型 == '物理固伤':
            calc_info['力量'] = self.站街力量()
            calc_info['独立攻击'] = self.站街独立攻击力()
        elif self.类型 == '魔法固伤':
            calc_info['智力'] = self.站街智力()
            calc_info['独立攻击'] = self.站街独立攻击力()
        calc_info['火'] = self.火属性强化()
        calc_info['冰'] = self.冰属性强化()
        calc_info['光'] = self.光属性强化()
        calc_info['暗'] = self.暗属性强化()

        for i in self.技能栏:
            倍率 = i.独立攻击力倍率(self.武器类型)
            if i.名称 not in self.skills_passive:
                continue
        if 倍率 != 1:
            self.skills_passive[i.名称]['info'].append({
                "type": "独立攻击力",
                "info": [round((倍率-1)*100), '所有', '']
            })
        倍率 = i.魔法攻击力倍率(self.武器类型)
        if 倍率 != 1:
            self.skills_passive[i.名称]['info'].append({
                "type": "魔法攻击力",
                "info": [round((倍率-1)*100), '所有', '']
            })
        倍率 = i.物理攻击力倍率(self.武器类型)
        if 倍率 != 1:
            self.skills_passive[i.名称]['info'].append({
                "type": "物理攻击力",
                "info": [round((倍率-1)*100), '所有', '']
            })
        buff = self.get_skill_by_name('BUFF')
        awake = self.get_skill_by_name('一次觉醒')
        result = {
            'id': uuid1().hex,
            'alter': self.实际名称,
            'name': self.名称,
            'role': 'buffer' if self.类型 == '辅助' else 'delear',
            'forget_set': info['forge_set'],
            'equips': list(map(lambda x: equ.get_json(x), self.装备栏)),
            'info': {
                # 站街
                '站街': calc_info,
                # 进图
                # '进图': {
                #     'liliang': self.站街力量(),
                #     'zhili': self.站街智力(),
                #     'wuligongji': self.站街物理攻击力(),
                #     'mofagongji': self.站街魔法攻击力(),
                #     'duligongji': self.站街独立攻击力(),
                #     'huo': 0,
                #     'bing': 0,
                #     'guang': 0,
                #     'an': 0
                # },
                # 词条
                'properties': {
                    # 攻击强化
                    '攻击强化': round(self.__攻击强化, 0),
                    'buffer_power': round(self.BUFF量(), 0),
                    'buffer_power_value': round(self.__buff量, 0),
                    'buffer_power_per': round(self.__百分比buff量*100, 2),
                    '技能攻击力': round(100*(self.__技能攻击力-1), 2),
                    '百分比攻击强化': round(self.__百分比攻击强化*100, 1),
                    'MP消耗量': round(self.__MP消耗量*100-100, 2),
                    '伤害比例': [self.__伤害比例.get('直伤', 1), self.__伤害比例.get('中毒', 0), self.__伤害比例.get('灼烧', 0), self.__伤害比例.get('感电', 0), self.__伤害比例.get('出血', 0)],
                    '伤害系数': [self.__伤害系数.get('直伤', 1), self.__伤害系数.get('中毒', 1)-1, self.__伤害系数.get('灼烧', 1)-1, self.__伤害系数.get('感电',  1)-1, self.__伤害系数.get('出血',  1)-1],
                    '无色消耗': temp['无色消耗'],
                    '条件冷却': self.__条件冷却,
                    "条件恢复": self.__条件冷却恢复,
                    'apply_value': self.适用数值,
                    'buff_level': buff.等级,
                    'buff_name': buff.名称,
                    'awake_level': awake.等级,
                    'awake_name': awake.名称,
                    'buff_intstr_per': self.__buff百分比力智,
                    'buff_intstr': self.__buff固定力智,
                    'buff_attack_per': self.__buff百分比三攻,
                    'buff_attack': self.__buff固定三攻,
                    'awake_intstr_per': self.__觉醒百分比力智,
                    'awake_intstr': self.__觉醒固定力智
                    # 其他老词条·····
                }
            },
            # '面板力量': self.面板力量(),
            # '面板智力': self.面板智力(),
            # '面板物理攻击力': self.面板物理攻击力(),
            # '面板魔法攻击力': self.面板魔法攻击力(),
            # '面板独立攻击力': self.面板独立攻击力(),
            'total_data': temp['buffer_addition'] if 'buffer_addition' in temp else [temp['total_data'], 0, 0, 0],
            "skills": temp["skills"],
            "skills_passive": self.skills_passive,
            "jade": jade
        }
        return result
