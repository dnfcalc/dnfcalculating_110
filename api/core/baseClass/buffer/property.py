
from core.baseClass.property import 角色属性
from core.baseClass.skill import 技能


class Buffer(角色属性):

    def BUFF量():
        return 0

    def 辅助属性加成(self, buff固定力智=0, buff百分比力智=0.0, buff固定三攻=0, buff百分比三攻=0.0, 觉醒固定力智=0, 觉醒百分比力智=0.0, buff量=0, 百分比buff量=0.0):
        pass
    pass


class 辅助职业技能(技能):
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    等级间隔 = 3
    等级 = 0
    基础等级 = 0
    是否主动 = 0
    站街生效 = 0
    等级溢出 = 0

    是否启用 = 1
    技能序号 = 0

    是否有伤害 = 0

    def 等级加成(self, x):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                if self.基础等级 != self.等级上限:
                    self.等级溢出 = 1
            else:
                self.等级 += x

    def 结算统计(self, context=None):
        return [0, 0, 0, 0]
        # 力智 三攻 智力 体精


class 辅助职业被动技能(辅助职业技能):
    是否主动 = 0
    进图加成 = 0


class 辅助职业主动技能(辅助职业技能):
    是否主动 = 1
    适用数值 = 0


class 辅助职业觉醒技能(辅助职业主动技能):
    所在等级 = 50
    等级精通 = 30
    等级上限 = 40
    基础等级 = 14
    一觉力智 = 0
    一觉力智per = 1.0
    # 28 原力智 941  测试修改为 939
    力智 = [
        0, 43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346,
        379, 414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888, 939,
        993, 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668
    ]

    def 结算统计(self, context: Buffer, compute_3rd_awake=False):
        buffer_power = context.BUFF量()

        三次觉醒 = context.get_skill_by_name("三次觉醒")

        if not compute_3rd_awake and self.名称 in 三次觉醒.关联技能:
            return [0] * 4
        旧词条力智 = ((self.适用数值/750 + 1) *
                 self.力智[self.等级] + self.一觉力智)*self.一觉力智per

        新词条力智 = (((self.适用数值 + 5250) / 750 + 1) *
                 (buffer_power + 5000) * 0.000025 * self.力智[self.等级]) if buffer_power > 0 else 0
        力智 = 旧词条力智 + 新词条力智
        return [力智, 0, 0, 0]
        # 力智 三攻 智力 体精


class 辅助职业三觉技能(辅助职业主动技能):
    所在等级 = 100
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 5
    绑定一觉力智per = 1.08
    绑定二觉力智per = 0.23
    关联技能 = []

    def 结算统计(self, context: Buffer):
        awake = context.get_skill_by_name('一次觉醒')
        if awake.是否启用:
            values = awake.结算统计(context, True)
            倍率 = self.加成倍率(awake.名称 in self.关联技能)
            return [int(round(i * 倍率)) for i in values]
        return [0] * 4

    def 加成倍率(self, bind_awake):
        if bind_awake:
            return round(1.08 + self.等级 * 0.01, 2)
        else:
            return round(0.23 + self.等级 * 0.01, 2)


BUFF影响技能 = ['勇气祝福', '勇气圣歌', '荣誉祝福', '禁忌诅咒', '死命召唤']
