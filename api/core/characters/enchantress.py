
from copy import deepcopy
from typing import List

from core.baseClass.buffer.property import *
from core.baseClass.character import Character


class 小魔女护石0:
    def __init__(self):
        self.name = '黑魔法大师'
        self.skill = '疯疯熊坠击'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.08)
        pass


class 小魔女护石1:
    def __init__(self):
        self.name = '好的主人！'
        self.skill = '变大吧！疯疯熊'

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


class 小魔女护石2:
    def __init__(self):
        self.name = '黑暗救援'
        self.skill = '哇咔咔！'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.04)


class 小魔女护石3:
    def __init__(self):
        self.name = '完美华尔兹'
        self.skill = '死命召唤'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.04)


class 小魔女护石4:
    def __init__(self):
        self.name = '永恒之舞'
        self.skill = '人偶戏法'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


class 小魔女护石5:
    def __init__(self):
        self.name = '魔女的庭院'
        self.skill = '苦痛庭院'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


class 小魔女护石6:
    def __init__(self):
        self.name = '个人主义者'
        self.skill = '咆哮吧！疯疯熊'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.08)


小魔女护石组合 = (小魔女护石0(), 小魔女护石1(), 小魔女护石2(),
           小魔女护石3(), 小魔女护石4(), 小魔女护石5(), 小魔女护石6())


class 知源·小魔女技能0(辅助职业被动技能):
    名称 = '人偶操纵者'
    所在等级 = 15
    等级精通 = 50
    等级上限 = 60
    学习间隔 = 3
    额外智力 = 0
    站街生效 = 1
    智力 = [0, 69, 73, 77, 81, 85, 90, 95, 100, 106, 112, 118, 124, 130, 137, 144, 152, 160, 168, 176, 184, 193, 202, 212, 221, 231, 241, 252, 262, 273, 284,
          296, 308, 320, 332, 344, 358, 371, 384, 398, 412, 426, 440, 456, 470, 486, 502, 518, 534, 550, 567, 581, 597, 613, 629, 645, 660, 676, 692, 708, 724]

    def 智力加成(self):
        return self.智力[self.等级] + self.额外智力 + self.进图加成

    def 结算统计(self, context: Buffer):
        return [0, 0, self.智力加成(), 0, 0]
        # 力智、三攻、智力、体力、精神


class 知源·小魔女技能1(辅助职业主动技能):
    名称 = '小魔女的偏爱'
    所在等级 = 20
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    增幅倍率 = 0.15

    def 结算统计(self, context: Buffer):
        buff = context.get_skill_by_name('BUFF')
        if buff.是否启用 and hasattr(context, '偏爱独立计算') and context.偏爱独立计算:
            values = buff.结算统计(context)
            return [int(round(i * self.增幅倍率, 3)) for i in values]
        return [0]*5


class 知源·小魔女技能2(辅助职业主动技能):
    名称 = '禁忌诅咒'
    所在等级 = 30
    等级精通 = 10
    等级上限 = 40
    学习间隔 = 3

    BUFF力智per = 1
    BUFF三攻per = 1

    BUFF力智 = 0
    BUFF三攻 = 0

    倍率 = 1.0

    三攻 = [0, 34, 35, 37, 38, 39, 41, 42, 43, 45, 46, 47, 49, 50, 51, 53, 54, 55, 57, 58,
          60, 61, 62, 64, 65, 66, 68, 69, 70, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 87]
    力智 = [0, 131, 140, 149, 158, 167, 175, 184, 193, 202, 211, 220, 229, 238, 247, 256, 264, 273, 282, 291,
          300, 309, 318, 327, 336, 345, 353, 362, 371, 380, 389, 398, 407, 416, 425, 434, 442, 451, 460, 469, 478]

    def 结算统计(self, context: Buffer):
        buffer_power = context.BUFF量()

        新词条倍率 = (((self.适用数值 + 4350) / 665 + 1) *
                 (buffer_power + 3500) * 0.0000379) if buffer_power > 0 else 0

        新词条力智 = 新词条倍率 * (self.力智[self.等级])
        新词条三攻 = 新词条倍率 * (self.三攻[self.等级])

        旧词条力智 = ((self.适用数值)/665 + 1) * \
            (self.力智[self.等级]+self.BUFF力智) * self.BUFF力智per

        旧词条三攻 = ((self.适用数值)/665 + 1) * \
            (self.三攻[self.等级]+self.BUFF三攻) * self.BUFF三攻per

        倍率 = self.倍率

        偏爱 = context.get_skill_by_name('小魔女的偏爱')
        if 偏爱.等级 > 0 and 偏爱.是否启用 and not (hasattr(context, '偏爱独立计算') and context.偏爱独立计算):
            倍率 *= 1 + 偏爱.增幅倍率

        力智 = int((新词条力智 + 旧词条力智) * 倍率)
        三攻 = int((新词条三攻 + 旧词条三攻) * 倍率)

        return [力智, 三攻, 0, 0, 0]
        # 力智、三攻、智力、体力、精神


class 知源·小魔女技能3(辅助职业主动技能):
    名称 = '死命召唤'
    所在等级 = 35
    等级精通 = 50
    等级上限 = 60
    学习间隔 = 3
    增幅倍率 = 0.25

    def 结算统计(self, context: Buffer):
        buff = context.get_skill_by_name('BUFF')
        偏爱 = context.get_skill_by_name('小魔女的偏爱')
        if buff.是否启用:
            values = buff.结算统计(context)

            if 偏爱.等级 > 0 and 偏爱.是否启用 and (hasattr(context, '偏爱独立计算') and context.偏爱独立计算):
                temps = 偏爱.结算统计(context)
                for i in range(len(temps)):
                    values[i] += temps[i]

            return [int(round(i * self.增幅倍率)) for i in values]
        return [0]*5


class 知源·小魔女技能4(辅助职业被动技能):
    名称 = '少女的爱'
    所在等级 = 48
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    额外力智 = 0
    力智 = [0, 14, 37, 59, 82, 104, 127, 149, 172, 194, 217, 239, 262, 284, 307, 329, 352, 374, 397, 419, 442,
          464, 487, 509, 532, 554, 577, 599, 622, 644, 667, 689, 712, 734, 757, 779, 802, 824, 847, 869, 892]

    def 力智加成(self):
        return self.力智[self.等级] + self.额外力智

    def 结算统计(self, context: Buffer):
        return [self.力智加成(), 0, self.力智加成(), 0, 0]
        # 力智、三攻、智力、体力、精神


class 知源·小魔女技能5(辅助职业觉醒技能):
    名称 = '开幕！人偶剧场'
    pass


class 知源·小魔女技能6(辅助职业被动技能):
    名称 = '冥月绽放'
    所在等级 = 75
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    站街生效 = 1
    智力 = [0, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330,
          340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540]

    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self, context: Buffer):
        return [0, 0, self.智力加成(), 0, 0]
        # 力智、三攻、智力、体力、精神


class 知源·小魔女技能7(辅助职业主动技能):
    名称 = '人偶之森'
    所在等级 = 85
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 5

    def 结算统计(self, context: Buffer):
        return [0]*5


class 知源·小魔女技能8(辅助职业被动技能):
    名称 = '不祥的微笑'
    所在等级 = 95
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    站街生效 = 1
    智力 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340,
          350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]

    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self, context: Buffer):
        return [0, 0, self.智力加成(),  0, 0]
        # 力智、三攻、智力、体力、精神


class 知源·小魔女技能9(辅助职业三觉技能):
    名称 = '终幕！人偶剧场'
    关联技能 = ['人偶之森']
    pass


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'enchantress'
        self.名称 = '知源·小魔女'
        self.角色 = '魔法师(女)'
        self.类型 = '辅助'
        self.职业 = '小魔女'
        self.武器选项 = ['扫把']
        self.输出类型选项 = ['魔法固伤']
        self.防具精通属性 = ['智力']
        self.武器类型 = '扫把'
        self.防具类型 = '板甲'
        self.技能序号 = {}
        技能栏 = []
        i = 0
        while i >= 0:
            try:
                skill: 辅助职业技能 = eval("知源·小魔女技能"+str(i)+"()")
                skill.技能序号 = i
                名称 = skill.名称
                self.技能序号[名称] = i
                if skill.所在等级 == 30:
                    名称 = 'BUFF'
                elif skill.所在等级 == 50:
                    名称 = '一次觉醒'
                elif skill.所在等级 == 85:
                    名称 = '二次觉醒'
                elif skill.所在等级 == 100:
                    名称 = '三次觉醒'
                skill.基础等级计算()
                技能栏.append(skill)
                self.技能序号[名称] = i
                i += 1
            except:
                i = -1
        self.技能栏 = 技能栏
        self.buff = 1.70
        self.护石技能 = [i.skill for i in 小魔女护石组合]

        super().__init__()

    def 护石计算(self):
        for 护石 in 小魔女护石组合:
            if 护石.skill in self.护石栏:
                护石.effect(self)

    def 职业特殊计算(self):
        for skill in self.技能栏:
            data = skill.结算统计(self)
            if(data[2] > 0):
                self.skills_passive[skill.名称]['info'] = [{
                    'type': '智力',
                    'info': [data[2]],
                    'percent': False
                }]
        pass
