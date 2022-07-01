from typing import Union

from core.baseClass.skill import 主动技能, 技能, 被动技能


class 角色属性:

    评分: float = 0

    类型: str

    适用属性: str = "智力"

    def 基础属性加成(self,
               物理攻击力=0.00, 魔法攻击力=0.00, 独立攻击力=0.00, 三攻=0.00,
               力量=0.00, 智力=0.00, 力智=0.00, 体力=0.00, 精神=0.00, 体精=0.00, 四维=0.00,
               物理暴击率=0.00, 魔法暴击率=0.00, 暴击率=0.00,
               攻击速度=0.00, 施放速度=0.00, 移动速度=0.00,   三速=0.00, **kwargs):
        物理攻击力 += 三攻
        魔法攻击力 += 三攻
        独立攻击力 += 三攻

        力量 += 力智 + 四维
        智力 += 力智 + 四维
        体力 += 体精 + 四维
        精神 += 体精 + 四维

        物理暴击率 += 暴击率
        魔法暴击率 += 暴击率

        if(self.类型 == "辅助"):
            if(self.适用属性 == '体力'):
                if(体力 > 0):
                    self.评分 += 体力 * 2
            elif(self.适用属性 == '精神'):
                if(精神 > 0):
                    self.评分 += 精神 * 2
            elif(self.适用属性 == '智力'):
                if(智力 > 0):
                    self.评分 += 智力 * 2
        elif (self.类型 == "物理百分比"):
            if 力量 > 0:
                self.评分 += 力量 * 2
            if 物理攻击力 > 0:
                self.评分 += 物理攻击力 * 2
            if 物理暴击率 > 0:
                self.评分 += 物理暴击率
        elif (self.类型 == "魔法百分比"):
            if 智力 > 0:
                self.评分 += 智力 * 2
            if 魔法攻击力 > 0:
                self.评分 += 魔法攻击力 * 2
            if 魔法暴击率 > 0:
                self.评分 += 魔法暴击率
        elif (self.类型 == "物理固伤"):
            if 力量 > 0:
                self.评分 += 力量 * 2
            if 独立攻击力 > 0:
                self.评分 += 独立攻击力 * 2
            if 物理暴击率 > 0:
                self.评分 += 物理暴击率
        elif self.类型 == "魔法固伤":
            if 智力 > 0:
                self.评分 += 智力 * 2
            if 独立攻击力 > 0:
                self.评分 += 独立攻击力 * 10
            if 魔法暴击率 > 0:
                self.评分 += 魔法暴击率
        pass

    def 攻击强化加成(self, x=0):
        if self.类型 != "辅助":
            self.评分 += x * 1000
        pass

    def 百分比攻击强化加成(self, x=0.0):
        if self.类型 != "辅助":
            self.评分 = (self.评分 + 2000) * (1 + x * 1000)

    def 技能攻击力加成(self, x=0):
        if self.类型 != "辅助":
            self.评分 = (self.评分 + 2000) * (1 + x * 2000)

    def 辅助属性加成(self, buff固定力智=0, buff百分比力智=0.0, buff固定三攻=0, buff百分比三攻=0.0, 觉醒固定力智=0, 觉醒百分比力智=0.0, buff量=0, 百分比buff量=0.0):
        if self.类型 == '辅助':
            self.评分 += buff固定力智
            self.评分 *= 1.0 + buff百分比力智
            self.评分 += buff固定三攻
            self.评分 *= 1.0 + buff百分比三攻
            self.评分 += 觉醒固定力智
            self.评分 *= 1.0 + 觉醒百分比力智

    def 技能等级加成(self, 加成类型: str, min: int, max: int, lv: int, exc=[int]) -> None:
        if self.类型 == "辅助":
            if 加成类型 == '主动':
                if min < 30 and max >= 30:
                    self.评分 += 2000 * (lv + 1)
                if min <= 50 and max >= 50:
                    self.评分 += 1000 * (lv + 1)

        if 加成类型 == '所有':
            self.评分 += 1000 * (lv + 1)

        self.评分 += 100 * (lv + 1)
        pass

    def 属性强化加成(self, 所有属性强化=0.00, 冰属性强化=0.00, 火属性强化=0.00, 暗属性强化=0.00, 光属性强化=0.00):
        光属性强化 += 所有属性强化
        暗属性强化 += 所有属性强化
        火属性强化 += 所有属性强化
        冰属性强化 += 所有属性强化

        if self.类型 != '辅助':
            self.评分 += max(光属性强化, 暗属性强化, 火属性强化, 冰属性强化) * 20
        pass

    # region 其它函数
    #     def get_skill_by_name(self, name) -> 技能 | 主动技能 | 被动技能:
    def get_skill_by_name(self, name) -> Union[技能, 主动技能, 被动技能]:
        pass
