from core.baseClass.character import Character
enchanting_func_list = {}

# 名望 部位 描述
index = ("maxFame", "position", "props")

# region 正常部位 20000~21000


def enchanting_20000(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '', '无附魔')"
    if mode == 0:
        pass
    if mode == 1:
        pass


def enchanting_20001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '物攻(25)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '魔攻(25)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20003(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '所有属性强化(5)')"
    if mode == 0:
        char.所有属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20004(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '智(38)')"
    if mode == 0:
        char.基础属性加成(智力=38 * rate)
    if mode == 1:
        pass


def enchanting_20005(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '力(38)')"
    if mode == 0:
        char.基础属性加成(力量=38 * rate)
    if mode == 1:
        pass


def enchanting_20006(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(5)')"
    if mode == 0:
        char.所有属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20007(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '火强(3)')"
    if mode == 0:
        char.火属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20008(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '火强(4)')"
    if mode == 0:
        char.火属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20009(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '火强(5)')"
    if mode == 0:
        char.火属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20010(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '火强(6)')"
    if mode == 0:
        char.火属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20011(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '冰强(3)')"
    if mode == 0:
        char.冰属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20012(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '冰强(4)')"
    if mode == 0:
        char.冰属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20013(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '冰强(5)')"
    if mode == 0:
        char.冰属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20014(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '冰强(6)')"
    if mode == 0:
        char.冰属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20015(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '暗强(3)')"
    if mode == 0:
        char.暗属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20016(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '暗强(4)')"
    if mode == 0:
        char.暗属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20017(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '暗强(5)')"
    if mode == 0:
        char.暗属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20018(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '暗强(6)')"
    if mode == 0:
        char.暗属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20019(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '光强(3)')"
    if mode == 0:
        char.光属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20020(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '光强(4)')"
    if mode == 0:
        char.光属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20021(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '光强(5)')"
    if mode == 0:
        char.光属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20022(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '光强(6)')"
    if mode == 0:
        char.光属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20023(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(15)')"
    if mode == 0:
        char.基础属性加成(力量=15 * rate)
    if mode == 1:
        pass


def enchanting_20024(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(16)')"
    if mode == 0:
        char.基础属性加成(力量=16 * rate)
    if mode == 1:
        pass


def enchanting_20025(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(17)')"
    if mode == 0:
        char.基础属性加成(力量=17 * rate)
    if mode == 1:
        pass


def enchanting_20026(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(18)')"
    if mode == 0:
        char.基础属性加成(力量=18 * rate)
    if mode == 1:
        pass


def enchanting_20027(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(19)')"
    if mode == 0:
        char.基础属性加成(力量=19 * rate)
    if mode == 1:
        pass


def enchanting_20028(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(20)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20029(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(21)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
    if mode == 1:
        pass


def enchanting_20030(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(22)')"
    if mode == 0:
        char.基础属性加成(力量=22 * rate)
    if mode == 1:
        pass


def enchanting_20031(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(5)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=5 * rate)
    if mode == 1:
        pass


def enchanting_20032(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(6)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=6 * rate)
    if mode == 1:
        pass


def enchanting_20033(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(7)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=7 * rate)
    if mode == 1:
        pass


def enchanting_20034(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(8)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=8 * rate)
    if mode == 1:
        pass


def enchanting_20035(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(9)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=9 * rate)
    if mode == 1:
        pass


def enchanting_20036(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩', '物暴(2%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.02 * rate)
    if mode == 1:
        pass


def enchanting_20037(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', '物暴(3%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20038(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(26)')"
    if mode == 0:
        char.基础属性加成(智力=26 * rate)
    if mode == 1:
        pass


def enchanting_20039(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(27)')"
    if mode == 0:
        char.基础属性加成(智力=27 * rate)
    if mode == 1:
        pass


def enchanting_20040(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(28)')"
    if mode == 0:
        char.基础属性加成(智力=28 * rate)
    if mode == 1:
        pass


def enchanting_20041(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(29)')"
    if mode == 0:
        char.基础属性加成(智力=29 * rate)
    if mode == 1:
        pass


def enchanting_20042(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '所有属性抗性(5)')"
    if mode == 0:
        char.所有属性抗性加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20043(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '所有属性抗性(6)')"
    if mode == 0:
        char.所有属性抗性加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20044(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '所有属性抗性(7)')"
    if mode == 0:
        char.所有属性抗性加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20045(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(35)')"
    if mode == 0:
        char.基础属性加成(精神=35 * rate)
    if mode == 1:
        pass


def enchanting_20046(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(3)')"
    if mode == 0:
        char.暗属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20047(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(4)')"
    if mode == 0:
        char.暗属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20048(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(5)')"
    if mode == 0:
        char.暗属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20049(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(3)')"
    if mode == 0:
        char.光属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20050(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(4)')"
    if mode == 0:
        char.光属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20051(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(5)')"
    if mode == 0:
        char.光属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20052(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '火抗(4)')"
    if mode == 0:
        char.火属性抗性加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20053(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '火抗(5)')"
    if mode == 0:
        char.火属性抗性加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20054(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '火抗(6)')"
    if mode == 0:
        char.火属性抗性加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20055(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '火抗(7)')"
    if mode == 0:
        char.火属性抗性加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20056(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '火抗(8)')"
    if mode == 0:
        char.火属性抗性加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20057(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '火抗(9)')"
    if mode == 0:
        char.火属性抗性加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20058(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '火抗(10)')"
    if mode == 0:
        char.火属性抗性加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20059(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(26)')"
    if mode == 0:
        char.基础属性加成(力量=26 * rate)
    if mode == 1:
        pass


def enchanting_20060(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(27)')"
    if mode == 0:
        char.基础属性加成(力量=27 * rate)
    if mode == 1:
        pass


def enchanting_20061(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(28)')"
    if mode == 0:
        char.基础属性加成(力量=28 * rate)
    if mode == 1:
        pass


def enchanting_20062(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(29)')"
    if mode == 0:
        char.基础属性加成(力量=29 * rate)
    if mode == 1:
        pass


def enchanting_20063(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '光抗(2)')"
    if mode == 0:
        char.光属性抗性加成(2 * rate)
    if mode == 1:
        pass


def enchanting_20064(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '光抗(3)')"
    if mode == 0:
        char.光属性抗性加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20065(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '光抗(4)')"
    if mode == 0:
        char.光属性抗性加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20066(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '光抗(5)')"
    if mode == 0:
        char.光属性抗性加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20067(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '光抗(6)')"
    if mode == 0:
        char.光属性抗性加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20068(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '光抗(7)')"
    if mode == 0:
        char.光属性抗性加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20069(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '光抗(8)')"
    if mode == 0:
        char.光属性抗性加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20070(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '光抗(9)')"
    if mode == 0:
        char.光属性抗性加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20071(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '光抗(10)')"
    if mode == 0:
        char.光属性抗性加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20072(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '独立(11)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=11 * rate)
    if mode == 1:
        pass


def enchanting_20073(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(15)')"
    if mode == 0:
        char.基础属性加成(精神=15 * rate)
    if mode == 1:
        pass


def enchanting_20074(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(16)')"
    if mode == 0:
        char.基础属性加成(精神=16 * rate)
    if mode == 1:
        pass


def enchanting_20075(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(17)')"
    if mode == 0:
        char.基础属性加成(精神=17 * rate)
    if mode == 1:
        pass


def enchanting_20076(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(18)')"
    if mode == 0:
        char.基础属性加成(精神=18 * rate)
    if mode == 1:
        pass


def enchanting_20077(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(19)')"
    if mode == 0:
        char.基础属性加成(精神=19 * rate)
    if mode == 1:
        pass


def enchanting_20078(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(20)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
    if mode == 1:
        pass


def enchanting_20079(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(21)')"
    if mode == 0:
        char.基础属性加成(精神=21 * rate)
    if mode == 1:
        pass


def enchanting_20080(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(8)')"
    if mode == 0:
        char.基础属性加成(力量=8 * rate)
    if mode == 1:
        pass


def enchanting_20081(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(9)')"
    if mode == 0:
        char.基础属性加成(力量=9 * rate)
    if mode == 1:
        pass


def enchanting_20082(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(10)')"
    if mode == 0:
        char.基础属性加成(力量=10 * rate)
    if mode == 1:
        pass


def enchanting_20083(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(11)')"
    if mode == 0:
        char.基础属性加成(力量=11 * rate)
    if mode == 1:
        pass


def enchanting_20084(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(12)')"
    if mode == 0:
        char.基础属性加成(力量=12 * rate)
    if mode == 1:
        pass


def enchanting_20085(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(13)')"
    if mode == 0:
        char.基础属性加成(力量=13 * rate)
    if mode == 1:
        pass


def enchanting_20086(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(14)')"
    if mode == 0:
        char.基础属性加成(力量=14 * rate)
    if mode == 1:
        pass


def enchanting_20087(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '施放速度(0.4%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.004 * rate)
    if mode == 1:
        pass


def enchanting_20088(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '施放速度(0.5%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.005 * rate)
    if mode == 1:
        pass


def enchanting_20089(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '施放速度(0.6%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.006 * rate)
    if mode == 1:
        pass


def enchanting_20090(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '施放速度(0.7%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.007 * rate)
    if mode == 1:
        pass


def enchanting_20091(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '施放速度(0.8%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.008 * rate)
    if mode == 1:
        pass


def enchanting_20092(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '施放速度(0.9%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.009 * rate)
    if mode == 1:
        pass


def enchanting_20093(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(12)')"
    if mode == 0:
        char.冰属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20094(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(13)')"
    if mode == 0:
        char.冰属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20095(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(14)')"
    if mode == 0:
        char.冰属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20096(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '冰强(15)')"
    if mode == 0:
        char.冰属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20097(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(23)')"
    if mode == 0:
        char.基础属性加成(精神=23 * rate)
    if mode == 1:
        pass


def enchanting_20098(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(24)')"
    if mode == 0:
        char.基础属性加成(精神=24 * rate)
    if mode == 1:
        pass


def enchanting_20099(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(25)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
    if mode == 1:
        pass


def enchanting_20100(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(9)')"
    if mode == 0:
        char.冰属性强化加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20101(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(10)')"
    if mode == 0:
        char.冰属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20102(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(11)')"
    if mode == 0:
        char.冰属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_20103(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(10)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_20104(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(11)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=11 * rate)
    if mode == 1:
        pass


def enchanting_20105(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(12)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=12 * rate)
    if mode == 1:
        pass


def enchanting_20106(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(13)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=13 * rate)
    if mode == 1:
        pass


def enchanting_20107(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(14)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=14 * rate)
    if mode == 1:
        pass


def enchanting_20108(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(6)')"
    if mode == 0:
        char.暗属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20109(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(7)')"
    if mode == 0:
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20110(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(5)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=5 * rate)
    if mode == 1:
        pass


def enchanting_20111(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(6)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=6 * rate)
    if mode == 1:
        pass


def enchanting_20112(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(7)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=7 * rate)
    if mode == 1:
        pass


def enchanting_20113(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(8)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=8 * rate)
    if mode == 1:
        pass


def enchanting_20114(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(9)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=9 * rate)
    if mode == 1:
        pass


def enchanting_20115(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(8)')"
    if mode == 0:
        char.基础属性加成(智力=8 * rate)
    if mode == 1:
        pass


def enchanting_20116(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(9)')"
    if mode == 0:
        char.基础属性加成(智力=9 * rate)
    if mode == 1:
        pass


def enchanting_20117(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(10)')"
    if mode == 0:
        char.基础属性加成(智力=10 * rate)
    if mode == 1:
        pass


def enchanting_20118(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(11)')"
    if mode == 0:
        char.基础属性加成(智力=11 * rate)
    if mode == 1:
        pass


def enchanting_20119(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(12)')"
    if mode == 0:
        char.基础属性加成(智力=12 * rate)
    if mode == 1:
        pass


def enchanting_20120(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(13)')"
    if mode == 0:
        char.基础属性加成(智力=13 * rate)
    if mode == 1:
        pass


def enchanting_20121(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(14)')"
    if mode == 0:
        char.基础属性加成(智力=14 * rate)
    if mode == 1:
        pass


def enchanting_20122(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '智(4)')"
    if mode == 0:
        char.基础属性加成(智力=4 * rate)
    if mode == 1:
        pass


def enchanting_20123(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '智(5)')"
    if mode == 0:
        char.基础属性加成(智力=5 * rate)
    if mode == 1:
        pass


def enchanting_20124(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '智(6)')"
    if mode == 0:
        char.基础属性加成(智力=6 * rate)
    if mode == 1:
        pass


def enchanting_20125(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '智(7)')"
    if mode == 0:
        char.基础属性加成(智力=7 * rate)
    if mode == 1:
        pass


def enchanting_20126(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '力(4)')"
    if mode == 0:
        char.基础属性加成(力量=4 * rate)
    if mode == 1:
        pass


def enchanting_20127(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '力(5)')"
    if mode == 0:
        char.基础属性加成(力量=5 * rate)
    if mode == 1:
        pass


def enchanting_20128(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '力(6)')"
    if mode == 0:
        char.基础属性加成(力量=6 * rate)
    if mode == 1:
        pass


def enchanting_20129(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '力(7)')"
    if mode == 0:
        char.基础属性加成(力量=7 * rate)
    if mode == 1:
        pass


def enchanting_20130(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(0.3%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.003 * rate)
    if mode == 1:
        pass


def enchanting_20131(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(0.4%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.004 * rate)
    if mode == 1:
        pass


def enchanting_20132(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(0.5%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.005 * rate)
    if mode == 1:
        pass


def enchanting_20133(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(0.6%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.006 * rate)
    if mode == 1:
        pass


def enchanting_20134(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(0.7%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.007 * rate)
    if mode == 1:
        pass


def enchanting_20135(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(0.8%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.008 * rate)
    if mode == 1:
        pass


def enchanting_20136(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '暗抗(4)')"
    if mode == 0:
        char.暗属性抗性加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20137(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '暗抗(5)')"
    if mode == 0:
        char.暗属性抗性加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20138(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '暗抗(6)')"
    if mode == 0:
        char.暗属性抗性加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20139(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '暗抗(7)')"
    if mode == 0:
        char.暗属性抗性加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20140(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '暗抗(8)')"
    if mode == 0:
        char.暗属性抗性加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20141(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '暗抗(9)')"
    if mode == 0:
        char.暗属性抗性加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20142(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '暗抗(10)')"
    if mode == 0:
        char.暗属性抗性加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20143(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '施放速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20144(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '施放速度(1.1%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.011 * rate)
    if mode == 1:
        pass


def enchanting_20145(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '施放速度(1.2%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.012 * rate)
    if mode == 1:
        pass


def enchanting_20146(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '施放速度(1.3%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.013 * rate)
    if mode == 1:
        pass


def enchanting_20147(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '施放速度(1.4%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.014 * rate)
    if mode == 1:
        pass


def enchanting_20148(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '鞋', '移动速度(0.9%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.009 * rate)
    if mode == 1:
        pass


def enchanting_20149(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '鞋', '移动速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20150(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '鞋', '移动速度(1.1%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.011 * rate)
    if mode == 1:
        pass


def enchanting_20151(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '鞋', '移动速度(1.2%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.012 * rate)
    if mode == 1:
        pass


def enchanting_20152(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(0.9%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.009 * rate)
    if mode == 1:
        pass


def enchanting_20153(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20154(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(1.1%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.011 * rate)
    if mode == 1:
        pass


def enchanting_20155(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', '魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20156(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', '魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20157(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(10)')"
    if mode == 0:
        char.所有属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20158(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(2)')"
    if mode == 0:
        char.所有属性强化加成(2 * rate)
    if mode == 1:
        pass


def enchanting_20159(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(3)')"
    if mode == 0:
        char.所有属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20160(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(4)')"
    if mode == 0:
        char.所有属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20161(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(6)')"
    if mode == 0:
        char.所有属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20162(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(7)')"
    if mode == 0:
        char.所有属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20163(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(8)')"
    if mode == 0:
        char.所有属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20164(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(9)')"
    if mode == 0:
        char.所有属性强化加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20165(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(8)|暗强(8)')"
    if mode == 0:
        char.光属性强化加成(8 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20166(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(8)|冰强(8)')"
    if mode == 0:
        char.火属性强化加成(8 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20167(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(8)|光强(8)')"
    if mode == 0:
        char.火属性强化加成(8 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20168(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(10)|暗强(10)')"
    if mode == 0:
        char.光属性强化加成(10 * rate)
        char.暗属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20169(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(10)|冰强(10)')"
    if mode == 0:
        char.火属性强化加成(10 * rate)
        char.冰属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20170(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(10)|光强(10)')"
    if mode == 0:
        char.火属性强化加成(10 * rate)
        char.光属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20171(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '所有属性抗性(12)')"
    if mode == 0:
        char.所有属性抗性加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20172(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '光强(18)')"
    if mode == 0:
        char.光属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20173(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '光强(19)')"
    if mode == 0:
        char.光属性强化加成(19 * rate)
    if mode == 1:
        pass


def enchanting_20174(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '鞋', '移动速度(4.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20175(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '火强(16)|独立(10)')"
    if mode == 0:
        char.火属性强化加成(16 * rate)
        char.基础属性加成(独立攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_20176(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '火抗(18)')"
    if mode == 0:
        char.火属性抗性加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20177(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '魔暴(10%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20178(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力智(45)')"
    if mode == 0:
        char.基础属性加成(力智=45 * rate)
    if mode == 1:
        pass


def enchanting_20179(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣', '力(65)')"
    if mode == 0:
        char.基础属性加成(力量=65 * rate)
    if mode == 1:
        pass


def enchanting_20180(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '力(50)|物攻(20)')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20181(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '暗强(20)')"
    if mode == 0:
        char.暗属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20182(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '魔攻(45)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=45 * rate)
    if mode == 1:
        pass


def enchanting_20183(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '独立(60)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_20184(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '独立(62)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=62 * rate)
    if mode == 1:
        pass


def enchanting_20185(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '独立(64)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=64 * rate)
    if mode == 1:
        pass


def enchanting_20186(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '智(55)')"
    if mode == 0:
        char.基础属性加成(智力=55 * rate)
    if mode == 1:
        pass


def enchanting_20187(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(4.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20188(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '精(65)')"
    if mode == 0:
        char.基础属性加成(精神=65 * rate)
    if mode == 1:
        pass


def enchanting_20189(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩', '施放速度(4.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20190(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '魔法石', '所有属性强化(12)')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20191(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '魔法石', '所有属性强化(13)')"
    if mode == 0:
        char.所有属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20192(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '魔法石', '所有属性强化(14)')"
    if mode == 0:
        char.所有属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20193(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '魔法石', '所有属性强化(15)')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20194(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '物攻(20)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20195(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '魔攻(20)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20196(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '独立(85)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=85 * rate)
    if mode == 1:
        pass


def enchanting_20197(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '物暴(2%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.02 * rate)
    if mode == 1:
        pass


def enchanting_20198(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '魔暴(2%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.02 * rate)
    if mode == 1:
        pass


def enchanting_20199(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '力(25)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
    if mode == 1:
        pass


def enchanting_20200(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '智(25)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
    if mode == 1:
        pass


def enchanting_20201(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '体(25)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
    if mode == 1:
        pass


def enchanting_20202(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '精(25)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
    if mode == 1:
        pass


def enchanting_20203(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '火强(7)')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20204(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '冰强(7)')"
    if mode == 0:
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20205(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '暗强(7)')"
    if mode == 0:
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20206(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '光强(7)')"
    if mode == 0:
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20207(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '物攻(10)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_20208(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '魔攻(10)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_20209(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '独立(15)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20210(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '物攻(15)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20211(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '魔攻(15)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20212(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '独立(20)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20213(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '物攻(42)|独立(42)|物暴(2%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=42 * rate)
        char.基础属性加成(独立攻击力=42 * rate)
        char.基础属性加成(物理暴击率=0.02 * rate)
    if mode == 1:
        pass


def enchanting_20214(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '魔攻(42)|独立(42)|魔暴(2%)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=42 * rate)
        char.基础属性加成(独立攻击力=42 * rate)
        char.基础属性加成(魔法暴击率=0.02 * rate)
    if mode == 1:
        pass


def enchanting_20215(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '四维(55)')"
    if mode == 0:
        char.基础属性加成(四维=55 * rate)
    if mode == 1:
        pass


def enchanting_20216(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '物暴(5%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20217(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '魔暴(5%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20218(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(6)')"
    if mode == 0:
        char.光属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20219(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(6)')"
    if mode == 0:
        char.冰属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20220(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(6)')"
    if mode == 0:
        char.火属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20221(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '魔暴(5%)|物暴(5%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20222(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '力(45)|体(-25)')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
        char.基础属性加成(体力=-25 * rate)
    if mode == 1:
        pass


def enchanting_20223(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '智(45)|精(-25)')"
    if mode == 0:
        char.基础属性加成(智力=45 * rate)
        char.基础属性加成(精神=-25 * rate)
    if mode == 1:
        pass


def enchanting_20224(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '体(40)|精(-25)')"
    if mode == 0:
        char.基础属性加成(体力=40 * rate)
        char.基础属性加成(精神=-25 * rate)
    if mode == 1:
        pass


def enchanting_20225(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '精(40)|体(-25)')"
    if mode == 0:
        char.基础属性加成(精神=40 * rate)
        char.基础属性加成(体力=-25 * rate)
    if mode == 1:
        pass


def enchanting_20226(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '物攻(10)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_20227(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '物攻(15)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20228(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '魔攻(10)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_20229(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '魔攻(15)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20230(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '独立(15)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20231(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '独立(20)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20232(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '独立(25)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20233(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(15)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20234(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(17)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=17 * rate)
    if mode == 1:
        pass


def enchanting_20235(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(19)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=19 * rate)
    if mode == 1:
        pass


def enchanting_20236(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(21)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=21 * rate)
    if mode == 1:
        pass


def enchanting_20237(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(23)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=23 * rate)
    if mode == 1:
        pass


def enchanting_20238(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '物攻(25)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20239(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(15)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20240(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(17)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=17 * rate)
    if mode == 1:
        pass


def enchanting_20241(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(19)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=19 * rate)
    if mode == 1:
        pass


def enchanting_20242(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(21)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=21 * rate)
    if mode == 1:
        pass


def enchanting_20243(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(23)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=23 * rate)
    if mode == 1:
        pass


def enchanting_20244(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '魔攻(25)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20245(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(9)')"
    if mode == 0:
        char.火属性强化加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20246(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(10)')"
    if mode == 0:
        char.火属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20247(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(11)')"
    if mode == 0:
        char.火属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_20248(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(12)')"
    if mode == 0:
        char.火属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20249(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(9)')"
    if mode == 0:
        char.暗属性强化加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20250(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(10)')"
    if mode == 0:
        char.暗属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20251(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(11)')"
    if mode == 0:
        char.暗属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_20252(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(12)')"
    if mode == 0:
        char.暗属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20253(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(9)')"
    if mode == 0:
        char.光属性强化加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20254(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(10)')"
    if mode == 0:
        char.光属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20255(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(11)')"
    if mode == 0:
        char.光属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_20256(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(12)')"
    if mode == 0:
        char.光属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20257(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(7)')"
    if mode == 0:
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20258(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(8)')"
    if mode == 0:
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20259(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '施放速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20260(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(7)')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20261(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(8)')"
    if mode == 0:
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20262(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(18)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=18 * rate)
    if mode == 1:
        pass


def enchanting_20263(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(18)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=18 * rate)
    if mode == 1:
        pass


def enchanting_20264(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '鞋', '移动速度(3.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20265(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(38)')"
    if mode == 0:
        char.基础属性加成(体力=38 * rate)
    if mode == 1:
        pass


def enchanting_20266(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(39)')"
    if mode == 0:
        char.基础属性加成(体力=39 * rate)
    if mode == 1:
        pass


def enchanting_20267(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(40)')"
    if mode == 0:
        char.基础属性加成(体力=40 * rate)
    if mode == 1:
        pass


def enchanting_20268(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '力(40)')"
    if mode == 0:
        char.基础属性加成(力量=40 * rate)
    if mode == 1:
        pass


def enchanting_20269(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '力(41)')"
    if mode == 0:
        char.基础属性加成(力量=41 * rate)
    if mode == 1:
        pass


def enchanting_20270(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '力(42)')"
    if mode == 0:
        char.基础属性加成(力量=42 * rate)
    if mode == 1:
        pass


def enchanting_20271(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '力(43)')"
    if mode == 0:
        char.基础属性加成(力量=43 * rate)
    if mode == 1:
        pass


def enchanting_20272(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '力(44)')"
    if mode == 0:
        char.基础属性加成(力量=44 * rate)
    if mode == 1:
        pass


def enchanting_20273(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '力(45)')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
    if mode == 1:
        pass


def enchanting_20274(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(40)')"
    if mode == 0:
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_20275(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(41)')"
    if mode == 0:
        char.基础属性加成(智力=41 * rate)
    if mode == 1:
        pass


def enchanting_20276(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(42)')"
    if mode == 0:
        char.基础属性加成(智力=42 * rate)
    if mode == 1:
        pass


def enchanting_20277(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(43)')"
    if mode == 0:
        char.基础属性加成(智力=43 * rate)
    if mode == 1:
        pass


def enchanting_20278(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(44)')"
    if mode == 0:
        char.基础属性加成(智力=44 * rate)
    if mode == 1:
        pass


def enchanting_20279(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(45)')"
    if mode == 0:
        char.基础属性加成(智力=45 * rate)
    if mode == 1:
        pass


def enchanting_20280(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(38)')"
    if mode == 0:
        char.基础属性加成(精神=38 * rate)
    if mode == 1:
        pass


def enchanting_20281(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(39)')"
    if mode == 0:
        char.基础属性加成(精神=39 * rate)
    if mode == 1:
        pass


def enchanting_20282(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(40)')"
    if mode == 0:
        char.基础属性加成(精神=40 * rate)
    if mode == 1:
        pass


def enchanting_20283(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '物暴(7%)|魔暴(7%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.07 * rate)
        char.基础属性加成(魔法暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20284(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', '物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20285(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '火强(2)')"
    if mode == 0:
        char.火属性强化加成(2 * rate)
    if mode == 1:
        pass


def enchanting_20286(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '冰强(2)')"
    if mode == 0:
        char.冰属性强化加成(2 * rate)
    if mode == 1:
        pass


def enchanting_20287(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '暗强(2)')"
    if mode == 0:
        char.暗属性强化加成(2 * rate)
    if mode == 1:
        pass


def enchanting_20288(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '光强(2)')"
    if mode == 0:
        char.光属性强化加成(2 * rate)
    if mode == 1:
        pass


def enchanting_20289(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '所有属性强化(4)')"
    if mode == 0:
        char.所有属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20290(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '所有属性强化(3)')"
    if mode == 0:
        char.所有属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20291(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '所有属性强化(2)')"
    if mode == 0:
        char.所有属性强化加成(2 * rate)
    if mode == 1:
        pass


def enchanting_20292(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(13)')"
    if mode == 0:
        char.火属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20293(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(14)')"
    if mode == 0:
        char.火属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20294(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '火强(15)')"
    if mode == 0:
        char.火属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20295(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(20)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20296(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(22)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=22 * rate)
    if mode == 1:
        pass


def enchanting_20297(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '物攻(24)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=24 * rate)
    if mode == 1:
        pass


def enchanting_20298(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '智(35)')"
    if mode == 0:
        char.基础属性加成(智力=35 * rate)
    if mode == 1:
        pass


def enchanting_20299(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '智(36)')"
    if mode == 0:
        char.基础属性加成(智力=36 * rate)
    if mode == 1:
        pass


def enchanting_20300(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '智(37)')"
    if mode == 0:
        char.基础属性加成(智力=37 * rate)
    if mode == 1:
        pass


def enchanting_20301(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(35)')"
    if mode == 0:
        char.基础属性加成(体力=35 * rate)
    if mode == 1:
        pass


def enchanting_20302(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(13)')"
    if mode == 0:
        char.光属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20303(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(14)')"
    if mode == 0:
        char.光属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20304(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '光强(15)')"
    if mode == 0:
        char.光属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20305(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(20)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20306(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(22)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=22 * rate)
    if mode == 1:
        pass


def enchanting_20307(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '魔攻(24)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=24 * rate)
    if mode == 1:
        pass


def enchanting_20308(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(35)')"
    if mode == 0:
        char.基础属性加成(力量=35 * rate)
    if mode == 1:
        pass


def enchanting_20309(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(36)')"
    if mode == 0:
        char.基础属性加成(力量=36 * rate)
    if mode == 1:
        pass


def enchanting_20310(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(37)')"
    if mode == 0:
        char.基础属性加成(力量=37 * rate)
    if mode == 1:
        pass


def enchanting_20311(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(38)')"
    if mode == 0:
        char.基础属性加成(智力=38 * rate)
    if mode == 1:
        pass


def enchanting_20312(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(39)')"
    if mode == 0:
        char.基础属性加成(智力=39 * rate)
    if mode == 1:
        pass


def enchanting_20313(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '力(38)')"
    if mode == 0:
        char.基础属性加成(力量=38 * rate)
    if mode == 1:
        pass


def enchanting_20314(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '力(39)')"
    if mode == 0:
        char.基础属性加成(力量=39 * rate)
    if mode == 1:
        pass


def enchanting_20315(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(26)')"
    if mode == 0:
        char.基础属性加成(精神=26 * rate)
    if mode == 1:
        pass


def enchanting_20316(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(27)')"
    if mode == 0:
        char.基础属性加成(精神=27 * rate)
    if mode == 1:
        pass


def enchanting_20317(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(28)')"
    if mode == 0:
        char.基础属性加成(精神=28 * rate)
    if mode == 1:
        pass


def enchanting_20318(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(29)')"
    if mode == 0:
        char.基础属性加成(精神=29 * rate)
    if mode == 1:
        pass


def enchanting_20319(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(30)')"
    if mode == 0:
        char.基础属性加成(精神=30 * rate)
    if mode == 1:
        pass


def enchanting_20320(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(31)')"
    if mode == 0:
        char.基础属性加成(精神=31 * rate)
    if mode == 1:
        pass


def enchanting_20321(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(32)')"
    if mode == 0:
        char.基础属性加成(精神=32 * rate)
    if mode == 1:
        pass


def enchanting_20322(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(33)')"
    if mode == 0:
        char.基础属性加成(精神=33 * rate)
    if mode == 1:
        pass


def enchanting_20323(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(34)')"
    if mode == 0:
        char.基础属性加成(精神=34 * rate)
    if mode == 1:
        pass


def enchanting_20324(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '属性攻击(暗)')"
    if mode == 0:
        char.属性攻击('暗')
    if mode == 1:
        pass


def enchanting_20325(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '属性攻击(冰)')"
    if mode == 0:
        char.属性攻击('冰')
    if mode == 1:
        pass


def enchanting_20326(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '属性攻击(火)')"
    if mode == 0:
        char.属性攻击('火')
    if mode == 1:
        pass


def enchanting_20327(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '属性攻击(光)')"
    if mode == 0:
        char.属性攻击('光')
    if mode == 1:
        pass


def enchanting_20328(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '物攻(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20329(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '魔攻(30)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20330(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '火强(9)')"
    if mode == 0:
        char.火属性强化加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20331(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '火强(10)')"
    if mode == 0:
        char.火属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20332(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '火强(11)')"
    if mode == 0:
        char.火属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_20333(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '火强(12)')"
    if mode == 0:
        char.火属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20334(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '冰强(9)')"
    if mode == 0:
        char.冰属性强化加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20335(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '冰强(10)')"
    if mode == 0:
        char.冰属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20336(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '冰强(11)')"
    if mode == 0:
        char.冰属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_20337(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '冰强(12)')"
    if mode == 0:
        char.冰属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20338(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '独立(18)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=18 * rate)
    if mode == 1:
        pass


def enchanting_20339(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '所有属性强化(15)')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20340(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '所有属性强化(18)')"
    if mode == 0:
        char.所有属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20341(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '力(50)')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
    if mode == 1:
        pass


def enchanting_20342(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '力(55)')"
    if mode == 0:
        char.基础属性加成(力量=55 * rate)
    if mode == 1:
        pass


def enchanting_20343(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩, 腰带, 鞋', '精(50)')"
    if mode == 0:
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20344(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩, 腰带, 鞋', '精(55)')"
    if mode == 0:
        char.基础属性加成(精神=55 * rate)
    if mode == 1:
        pass


def enchanting_20345(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '冰强(20)')"
    if mode == 0:
        char.冰属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20346(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '火强(18)|暗强(18)')"
    if mode == 0:
        char.火属性强化加成(18 * rate)
        char.暗属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20347(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '火强(20)|暗强(20)')"
    if mode == 0:
        char.火属性强化加成(20 * rate)
        char.暗属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20348(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '火强(18)|光强(18)')"
    if mode == 0:
        char.火属性强化加成(18 * rate)
        char.光属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20349(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '火强(20)|光强(20)')"
    if mode == 0:
        char.火属性强化加成(20 * rate)
        char.光属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20350(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(25)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
    if mode == 1:
        pass


def enchanting_20351(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(30)')"
    if mode == 0:
        char.基础属性加成(体力=30 * rate)
    if mode == 1:
        pass


def enchanting_20352(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '鞋', '移动速度(5.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20353(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '鞋', '移动速度(7.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20354(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '物攻(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20355(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '物攻(35)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=35 * rate)
    if mode == 1:
        pass


def enchanting_20356(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '光强(18)|暗强(18)')"
    if mode == 0:
        char.光属性强化加成(18 * rate)
        char.暗属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20357(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '光强(20)|暗强(20)')"
    if mode == 0:
        char.光属性强化加成(20 * rate)
        char.暗属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20358(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩, 腰带, 鞋', '体(50)')"
    if mode == 0:
        char.基础属性加成(体力=50 * rate)
    if mode == 1:
        pass


def enchanting_20359(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩, 腰带, 鞋', '体(55)')"
    if mode == 0:
        char.基础属性加成(体力=55 * rate)
    if mode == 1:
        pass


def enchanting_20360(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(25)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
    if mode == 1:
        pass


def enchanting_20361(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(30)')"
    if mode == 0:
        char.基础属性加成(智力=30 * rate)
    if mode == 1:
        pass


def enchanting_20362(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '物暴(8%)|魔暴(8%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.08 * rate)
        char.基础属性加成(魔法暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20363(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(20)|物攻(15)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20364(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '力(30)|物攻(20)')"
    if mode == 0:
        char.基础属性加成(力量=30 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20365(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(20)|魔攻(15)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20366(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(30)|魔攻(20)')"
    if mode == 0:
        char.基础属性加成(智力=30 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20367(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(6.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20368(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(8.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20369(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '光强(20)')"
    if mode == 0:
        char.光属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20370(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '物攻(25)|攻击速度(3.0%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=25 * rate)
        char.基础属性加成(攻击速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20371(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '物攻(30)|攻击速度(5.0%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(攻击速度=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20372(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '冰强(18)|暗强(18)')"
    if mode == 0:
        char.冰属性强化加成(18 * rate)
        char.暗属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20373(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '冰强(20)|暗强(20)')"
    if mode == 0:
        char.冰属性强化加成(20 * rate)
        char.暗属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20374(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(25)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
    if mode == 1:
        pass


def enchanting_20375(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(30)')"
    if mode == 0:
        char.基础属性加成(力量=30 * rate)
    if mode == 1:
        pass


def enchanting_20376(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '智(50)')"
    if mode == 0:
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_20377(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '耳环', '四维(50)')"
    if mode == 0:
        char.基础属性加成(四维=50 * rate)
    if mode == 1:
        pass


def enchanting_20378(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(8)')"
    if mode == 0:
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20379(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '独立(35)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=35 * rate)
    if mode == 1:
        pass


def enchanting_20380(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '独立(37)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=37 * rate)
    if mode == 1:
        pass


def enchanting_20381(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '独立(39)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=39 * rate)
    if mode == 1:
        pass


def enchanting_20382(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '魔暴(6%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20383(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '冰强(18)|光强(18)')"
    if mode == 0:
        char.冰属性强化加成(18 * rate)
        char.光属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20384(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '冰强(20)|光强(20)')"
    if mode == 0:
        char.冰属性强化加成(20 * rate)
        char.光属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20385(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', '物暴(4%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20386(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '物暴(6%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20387(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(8)')"
    if mode == 0:
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20388(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '物攻(25)|攻击速度(3.0%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=25 * rate)
        char.基础属性加成(攻击速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20389(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '耳环', '四维(75)')"
    if mode == 0:
        char.基础属性加成(四维=75 * rate)
    if mode == 1:
        pass


def enchanting_20390(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '耳环', '四维(100)')"
    if mode == 0:
        char.基础属性加成(四维=100 * rate)
    if mode == 1:
        pass


def enchanting_20391(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '耳环', '四维(125)')"
    if mode == 0:
        char.基础属性加成(四维=125 * rate)
    if mode == 1:
        pass


def enchanting_20392(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(10)|智(30)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=10 * rate)
        char.基础属性加成(智力=30 * rate)
    if mode == 1:
        pass


def enchanting_20393(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '魔攻(15)|智(40)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_20394(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '魔攻(20)|智(50)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_20395(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '耳环', '四维(5)')"
    if mode == 0:
        char.基础属性加成(四维=5 * rate)
    if mode == 1:
        pass


def enchanting_20396(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '魔法石', '所有属性强化(5)')"
    if mode == 0:
        char.所有属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20397(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(116, '宠物', '四维(15)')"
    if mode == 0:
        char.基础属性加成(四维=15 * rate)
    if mode == 1:
        pass


def enchanting_20398(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(116, '宠物', '四维(30)')"
    if mode == 0:
        char.基础属性加成(四维=30 * rate)
    if mode == 1:
        pass


def enchanting_20399(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(116, '宠物', '四维(45)')"
    if mode == 0:
        char.基础属性加成(四维=45 * rate)
    if mode == 1:
        pass


def enchanting_20400(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(116, '宠物', '所有属性强化(6)')"
    if mode == 0:
        char.所有属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20401(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(116, '宠物', '所有属性强化(8)')"
    if mode == 0:
        char.所有属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20402(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(116, '宠物', '所有属性强化(10)')"
    if mode == 0:
        char.所有属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20403(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(116, '宠物', '魔暴(6%)|物暴(6%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.06 * rate)
        char.基础属性加成(物理暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20404(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(116, '宠物', '魔暴(8%)|物暴(8%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.08 * rate)
        char.基础属性加成(物理暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20405(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(116, '宠物', '魔暴(10%)|物暴(10%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.1 * rate)
        char.基础属性加成(物理暴击率=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20406(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '力(40)')"
    if mode == 0:
        char.基础属性加成(力量=40 * rate)
    if mode == 1:
        pass


def enchanting_20407(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '智(40)')"
    if mode == 0:
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_20408(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '精(35)')"
    if mode == 0:
        char.基础属性加成(精神=35 * rate)
    if mode == 1:
        pass


def enchanting_20409(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '体(35)')"
    if mode == 0:
        char.基础属性加成(体力=35 * rate)
    if mode == 1:
        pass


def enchanting_20410(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '耳环', '魔暴(3%)|物暴(3%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20411(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '力智(32)|体精(28)')"
    if mode == 0:
        char.基础属性加成(力智=32 * rate)
        char.基础属性加成(体精=28 * rate)
    if mode == 1:
        pass


def enchanting_20412(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '力智(24)|体精(21)')"
    if mode == 0:
        char.基础属性加成(力智=24 * rate)
        char.基础属性加成(体精=21 * rate)
    if mode == 1:
        pass


def enchanting_20413(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '力(45)')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
    if mode == 1:
        pass


def enchanting_20414(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '智(45)')"
    if mode == 0:
        char.基础属性加成(智力=45 * rate)
    if mode == 1:
        pass


def enchanting_20415(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '体(45)')"
    if mode == 0:
        char.基础属性加成(体力=45 * rate)
    if mode == 1:
        pass


def enchanting_20416(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '精(45)')"
    if mode == 0:
        char.基础属性加成(精神=45 * rate)
    if mode == 1:
        pass


def enchanting_20417(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '光强(12)')"
    if mode == 0:
        char.光属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20418(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '暗强(12)')"
    if mode == 0:
        char.暗属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20419(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '魔法石', '所有属性强化(10)')"
    if mode == 0:
        char.所有属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20420(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '暗强(15)')"
    if mode == 0:
        char.暗属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20421(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '所有属性强化(7)')"
    if mode == 0:
        char.所有属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20422(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '光强(9)')"
    if mode == 0:
        char.光属性强化加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20423(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '暗强(9)')"
    if mode == 0:
        char.暗属性强化加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20424(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '所有属性强化(10)')"
    if mode == 0:
        char.所有属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20425(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '独立(45)|力(15)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=45 * rate)
        char.基础属性加成(力量=15 * rate)
    if mode == 1:
        pass


def enchanting_20426(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '独立(50)|力(20)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20427(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(11)')"
    if mode == 0:
        char.所有属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_20428(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(12)')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20429(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '魔暴(9%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.09 * rate)
    if mode == 1:
        pass


def enchanting_20430(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力(70)')"
    if mode == 0:
        char.基础属性加成(力量=70 * rate)
    if mode == 1:
        pass


def enchanting_20431(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力(75)')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
    if mode == 1:
        pass


def enchanting_20432(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '物暴(9%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.09 * rate)
    if mode == 1:
        pass


def enchanting_20433(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '物暴(10%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20434(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '精(70)')"
    if mode == 0:
        char.基础属性加成(精神=70 * rate)
    if mode == 1:
        pass


def enchanting_20435(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '精(75)')"
    if mode == 0:
        char.基础属性加成(精神=75 * rate)
    if mode == 1:
        pass


def enchanting_20436(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '独立(45)|智(15)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=45 * rate)
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_20437(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '独立(50)|智(20)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20438(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '物攻(45)|力(15)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=45 * rate)
        char.基础属性加成(力量=15 * rate)
    if mode == 1:
        pass


def enchanting_20439(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '物攻(50)|力(20)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20440(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '辅助装备', '四维(45)')"
    if mode == 0:
        char.基础属性加成(四维=45 * rate)
    if mode == 1:
        pass


def enchanting_20441(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '辅助装备', '四维(50)')"
    if mode == 0:
        char.基础属性加成(四维=50 * rate)
    if mode == 1:
        pass


def enchanting_20442(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '智(70)')"
    if mode == 0:
        char.基础属性加成(智力=70 * rate)
    if mode == 1:
        pass


def enchanting_20443(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '智(75)')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20444(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '魔攻(45)|智(15)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=45 * rate)
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_20445(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '魔攻(50)|智(20)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20446(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '魔暴(5%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20447(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '魔暴(7%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20448(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '体(70)')"
    if mode == 0:
        char.基础属性加成(体力=70 * rate)
    if mode == 1:
        pass


def enchanting_20449(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '体(75)')"
    if mode == 0:
        char.基础属性加成(体力=75 * rate)
    if mode == 1:
        pass


def enchanting_20450(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(32)')"
    if mode == 0:
        char.基础属性加成(力量=32 * rate)
    if mode == 1:
        pass


def enchanting_20451(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(34)')"
    if mode == 0:
        char.基础属性加成(力量=34 * rate)
    if mode == 1:
        pass


def enchanting_20452(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '辅助装备', '魔攻(34)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=34 * rate)
    if mode == 1:
        pass


def enchanting_20453(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '辅助装备', '魔攻(38)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=38 * rate)
    if mode == 1:
        pass


def enchanting_20454(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '魔攻(42)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=42 * rate)
    if mode == 1:
        pass


def enchanting_20455(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '物暴(5%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20456(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '物暴(7%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20457(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(32)')"
    if mode == 0:
        char.基础属性加成(智力=32 * rate)
    if mode == 1:
        pass


def enchanting_20458(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(34)')"
    if mode == 0:
        char.基础属性加成(智力=34 * rate)
    if mode == 1:
        pass


def enchanting_20459(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(36)')"
    if mode == 0:
        char.基础属性加成(智力=36 * rate)
    if mode == 1:
        pass


def enchanting_20460(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '独立(21)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=21 * rate)
    if mode == 1:
        pass


def enchanting_20461(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '独立(23)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=23 * rate)
    if mode == 1:
        pass


def enchanting_20462(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '独立(25)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20463(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '辅助装备', '物攻(34)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=34 * rate)
    if mode == 1:
        pass


def enchanting_20464(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '辅助装备', '物攻(38)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=38 * rate)
    if mode == 1:
        pass


def enchanting_20465(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '物攻(42)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=42 * rate)
    if mode == 1:
        pass


def enchanting_20466(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(32)')"
    if mode == 0:
        char.基础属性加成(体力=32 * rate)
    if mode == 1:
        pass


def enchanting_20467(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(34)')"
    if mode == 0:
        char.基础属性加成(体力=34 * rate)
    if mode == 1:
        pass


def enchanting_20468(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(36)')"
    if mode == 0:
        char.基础属性加成(体力=36 * rate)
    if mode == 1:
        pass


def enchanting_20469(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(36)')"
    if mode == 0:
        char.基础属性加成(精神=36 * rate)
    if mode == 1:
        pass


def enchanting_20470(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(13)')"
    if mode == 0:
        char.暗属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20471(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '辅助装备', '独立(34)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=34 * rate)
    if mode == 1:
        pass


def enchanting_20472(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '辅助装备', '独立(38)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=38 * rate)
    if mode == 1:
        pass


def enchanting_20473(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '独立(42)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=42 * rate)
    if mode == 1:
        pass


def enchanting_20474(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '耳环', '四维(25)')"
    if mode == 0:
        char.基础属性加成(四维=25 * rate)
    if mode == 1:
        pass


def enchanting_20475(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '魔法石', '所有属性强化(8)')"
    if mode == 0:
        char.所有属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20476(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '所有属性强化(19)')"
    if mode == 0:
        char.所有属性强化加成(19 * rate)
    if mode == 1:
        pass


def enchanting_20477(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '所有属性强化(21)')"
    if mode == 0:
        char.所有属性强化加成(21 * rate)
    if mode == 1:
        pass


def enchanting_20478(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '所有属性强化(23)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20479(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '冰强(21)|光强(21)')"
    if mode == 0:
        char.冰属性强化加成(21 * rate)
        char.光属性强化加成(21 * rate)
    if mode == 1:
        pass


def enchanting_20480(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '冰强(23)|光强(23)')"
    if mode == 0:
        char.冰属性强化加成(23 * rate)
        char.光属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20481(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '冰强(25)|光强(25)')"
    if mode == 0:
        char.冰属性强化加成(25 * rate)
        char.光属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20482(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '火强(21)|暗强(21)')"
    if mode == 0:
        char.火属性强化加成(21 * rate)
        char.暗属性强化加成(21 * rate)
    if mode == 1:
        pass


def enchanting_20483(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '火强(23)|暗强(23)')"
    if mode == 0:
        char.火属性强化加成(23 * rate)
        char.暗属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20484(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '火强(25)|暗强(25)')"
    if mode == 0:
        char.火属性强化加成(25 * rate)
        char.暗属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20485(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '力智(34)|体精(30)')"
    if mode == 0:
        char.基础属性加成(力智=34 * rate)
        char.基础属性加成(体精=30 * rate)
    if mode == 1:
        pass


def enchanting_20486(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '力智(38)|体精(34)')"
    if mode == 0:
        char.基础属性加成(力智=38 * rate)
        char.基础属性加成(体精=34 * rate)
    if mode == 1:
        pass


def enchanting_20487(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '力智(42)|体精(38)')"
    if mode == 0:
        char.基础属性加成(力智=42 * rate)
        char.基础属性加成(体精=38 * rate)
    if mode == 1:
        pass


def enchanting_20488(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '四维(28)')"
    if mode == 0:
        char.基础属性加成(四维=28 * rate)
    if mode == 1:
        pass


def enchanting_20489(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '四维(28)')"
    if mode == 0:
        char.基础属性加成(四维=28 * rate)
    if mode == 1:
        pass


def enchanting_20490(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '火强(18)')"
    if mode == 0:
        char.火属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20491(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '冰强(18)')"
    if mode == 0:
        char.冰属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20492(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '暗强(18)')"
    if mode == 0:
        char.暗属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20493(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '魔攻(30)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20494(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '独立(30)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20495(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '物攻(40)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_20496(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '物攻(45)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=45 * rate)
    if mode == 1:
        pass


def enchanting_20497(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩', '施放速度(5.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20498(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩', '施放速度(7.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20499(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '独立(40)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_20500(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '独立(45)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=45 * rate)
    if mode == 1:
        pass


def enchanting_20501(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '魔攻(40)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_20502(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '体精(60)')"
    if mode == 0:
        char.基础属性加成(体精=60 * rate)
    if mode == 1:
        pass


def enchanting_20503(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '体精(65)')"
    if mode == 0:
        char.基础属性加成(体精=65 * rate)
    if mode == 1:
        pass


def enchanting_20504(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(14)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=14 * rate)
    if mode == 1:
        pass


def enchanting_20505(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(18)')"
    if mode == 0:
        char.基础属性加成(智力=18 * rate)
    if mode == 1:
        pass


def enchanting_20506(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '物暴(3%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20507(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '独立(14)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=14 * rate)
    if mode == 1:
        pass


def enchanting_20508(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20509(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(16)')"
    if mode == 0:
        char.基础属性加成(体力=16 * rate)
    if mode == 1:
        pass


def enchanting_20510(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '物暴(1%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20511(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '魔暴(1%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20512(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '独立(7)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=7 * rate)
    if mode == 1:
        pass


def enchanting_20513(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(10)')"
    if mode == 0:
        char.基础属性加成(体力=10 * rate)
    if mode == 1:
        pass


def enchanting_20514(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩, 腰带, 鞋', '精(10)')"
    if mode == 0:
        char.基础属性加成(精神=10 * rate)
    if mode == 1:
        pass


def enchanting_20515(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '魔法石', '所有属性强化(16)')"
    if mode == 0:
        char.所有属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_20516(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '所有属性强化(18)')"
    if mode == 0:
        char.所有属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20517(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '所有属性强化(20)')"
    if mode == 0:
        char.所有属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20518(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '四维(50)')"
    if mode == 0:
        char.基础属性加成(四维=50 * rate)
    if mode == 1:
        pass


def enchanting_20519(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '四维(55)')"
    if mode == 0:
        char.基础属性加成(四维=55 * rate)
    if mode == 1:
        pass


def enchanting_20520(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '四维(60)')"
    if mode == 0:
        char.基础属性加成(四维=60 * rate)
    if mode == 1:
        pass


def enchanting_20521(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '三攻(50)')"
    if mode == 0:
        char.基础属性加成(三攻=50 * rate)
    if mode == 1:
        pass


def enchanting_20522(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '三攻(60)')"
    if mode == 0:
        char.基础属性加成(三攻=60 * rate)
    if mode == 1:
        pass


def enchanting_20523(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '三攻(70)')"
    if mode == 0:
        char.基础属性加成(三攻=70 * rate)
    if mode == 1:
        pass


def enchanting_20524(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '四维(60)')"
    if mode == 0:
        char.基础属性加成(四维=60 * rate)
    if mode == 1:
        pass


def enchanting_20525(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '四维(70)')"
    if mode == 0:
        char.基础属性加成(四维=70 * rate)
    if mode == 1:
        pass


def enchanting_20526(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '四维(80)')"
    if mode == 0:
        char.基础属性加成(四维=80 * rate)
    if mode == 1:
        pass


def enchanting_20527(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '火强(23)')"
    if mode == 0:
        char.火属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20528(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '火强(25)')"
    if mode == 0:
        char.火属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20529(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '冰强(23)')"
    if mode == 0:
        char.冰属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20530(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '冰强(25)')"
    if mode == 0:
        char.冰属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20531(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '光强(23)')"
    if mode == 0:
        char.光属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20532(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '光强(25)')"
    if mode == 0:
        char.光属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20533(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '暗强(23)')"
    if mode == 0:
        char.暗属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20534(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '暗强(25)')"
    if mode == 0:
        char.暗属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20535(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '物攻(25)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20536(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '物攻(26)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=26 * rate)
    if mode == 1:
        pass


def enchanting_20537(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '物攻(27)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=27 * rate)
    if mode == 1:
        pass


def enchanting_20538(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '物攻(28)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=28 * rate)
    if mode == 1:
        pass


def enchanting_20539(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '物攻(29)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=29 * rate)
    if mode == 1:
        pass


def enchanting_20540(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '物攻(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20541(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '魔攻(25)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20542(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '魔攻(26)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=26 * rate)
    if mode == 1:
        pass


def enchanting_20543(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '魔攻(27)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=27 * rate)
    if mode == 1:
        pass


def enchanting_20544(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '魔攻(28)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=28 * rate)
    if mode == 1:
        pass


def enchanting_20545(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '魔攻(29)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=29 * rate)
    if mode == 1:
        pass


def enchanting_20546(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '魔攻(30)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20547(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '力智(30)')"
    if mode == 0:
        char.基础属性加成(力智=30 * rate)
    if mode == 1:
        pass


def enchanting_20548(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '火强(20)')"
    if mode == 0:
        char.火属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20549(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '力智(40)|体精(35)')"
    if mode == 0:
        char.基础属性加成(力智=40 * rate)
        char.基础属性加成(体精=35 * rate)
    if mode == 1:
        pass


def enchanting_20550(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '魔法石', '四维(30)')"
    if mode == 0:
        char.基础属性加成(四维=30 * rate)
    if mode == 1:
        pass


def enchanting_20551(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '三攻(48)')"
    if mode == 0:
        char.基础属性加成(三攻=48 * rate)
    if mode == 1:
        pass


def enchanting_20552(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '施放速度(7.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20553(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '力智(34)|体精(30)')"
    if mode == 0:
        char.基础属性加成(力智=34 * rate)
        char.基础属性加成(体精=30 * rate)
    if mode == 1:
        pass


def enchanting_20554(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体精(25)')"
    if mode == 0:
        char.基础属性加成(体精=25 * rate)
    if mode == 1:
        pass


def enchanting_20555(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体精(45)')"
    if mode == 0:
        char.基础属性加成(体精=45 * rate)
    if mode == 1:
        pass


def enchanting_20556(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力智(25)')"
    if mode == 0:
        char.基础属性加成(力智=25 * rate)
    if mode == 1:
        pass


def enchanting_20557(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '魔攻(35)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=35 * rate)
    if mode == 1:
        pass


def enchanting_20558(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '独立(35)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=35 * rate)
    if mode == 1:
        pass


def enchanting_20559(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '耳环', '四维(150)')"
    if mode == 0:
        char.基础属性加成(四维=150 * rate)
    if mode == 1:
        pass


def enchanting_20560(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '暗强(12)|火强(12)')"
    if mode == 0:
        char.暗属性强化加成(12 * rate)
        char.火属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20561(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '光强(12)|冰强(12)')"
    if mode == 0:
        char.光属性强化加成(12 * rate)
        char.冰属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20562(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '力智(42)|体精(38)')"
    if mode == 0:
        char.基础属性加成(力智=42 * rate)
        char.基础属性加成(体精=38 * rate)
    if mode == 1:
        pass


def enchanting_20563(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体精(50)')"
    if mode == 0:
        char.基础属性加成(体精=50 * rate)
    if mode == 1:
        pass


def enchanting_20564(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '三攻(30)')"
    if mode == 0:
        char.基础属性加成(三攻=30 * rate)
    if mode == 1:
        pass


def enchanting_20565(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '物暴(5%)|魔暴(5%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20566(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '三攻(42)')"
    if mode == 0:
        char.基础属性加成(三攻=42 * rate)
    if mode == 1:
        pass


def enchanting_20567(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '冰强(26)|暗强(26)')"
    if mode == 0:
        char.冰属性强化加成(26 * rate)
        char.暗属性强化加成(26 * rate)
    if mode == 1:
        pass


def enchanting_20568(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '冰强(28)|暗强(28)')"
    if mode == 0:
        char.冰属性强化加成(28 * rate)
        char.暗属性强化加成(28 * rate)
    if mode == 1:
        pass


def enchanting_20569(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '冰强(30)|暗强(30)')"
    if mode == 0:
        char.冰属性强化加成(30 * rate)
        char.暗属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20570(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '火强(26)|光强(26)')"
    if mode == 0:
        char.火属性强化加成(26 * rate)
        char.光属性强化加成(26 * rate)
    if mode == 1:
        pass


def enchanting_20571(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '火强(28)|光强(28)')"
    if mode == 0:
        char.火属性强化加成(28 * rate)
        char.光属性强化加成(28 * rate)
    if mode == 1:
        pass


def enchanting_20572(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '火强(30)|光强(30)')"
    if mode == 0:
        char.火属性强化加成(30 * rate)
        char.光属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20573(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '四维(50)')"
    if mode == 0:
        char.基础属性加成(四维=50 * rate)
    if mode == 1:
        pass


def enchanting_20574(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '四维(60)')"
    if mode == 0:
        char.基础属性加成(四维=60 * rate)
    if mode == 1:
        pass


def enchanting_20575(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '四维(70)')"
    if mode == 0:
        char.基础属性加成(四维=70 * rate)
    if mode == 1:
        pass


def enchanting_20576(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '三攻(45)')"
    if mode == 0:
        char.基础属性加成(三攻=45 * rate)
    if mode == 1:
        pass


def enchanting_20577(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '三攻(50)')"
    if mode == 0:
        char.基础属性加成(三攻=50 * rate)
    if mode == 1:
        pass


def enchanting_20578(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '力智(65)')"
    if mode == 0:
        char.基础属性加成(力智=65 * rate)
    if mode == 1:
        pass


def enchanting_20579(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力智(70)')"
    if mode == 0:
        char.基础属性加成(力智=70 * rate)
    if mode == 1:
        pass


def enchanting_20580(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '所有属性强化(20)')"
    if mode == 0:
        char.所有属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20581(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '所有属性强化(22)')"
    if mode == 0:
        char.所有属性强化加成(22 * rate)
    if mode == 1:
        pass


def enchanting_20582(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '体精(70)')"
    if mode == 0:
        char.基础属性加成(体精=70 * rate)
    if mode == 1:
        pass


def enchanting_20583(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '耳环', '四维(90)')"
    if mode == 0:
        char.基础属性加成(四维=90 * rate)
    if mode == 1:
        pass


def enchanting_20584(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '光强(13)')"
    if mode == 0:
        char.光属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20585(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '光强(14)')"
    if mode == 0:
        char.光属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20586(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '光强(15)')"
    if mode == 0:
        char.光属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20587(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '火强(13)')"
    if mode == 0:
        char.火属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20588(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '火强(14)')"
    if mode == 0:
        char.火属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20589(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '火强(15)')"
    if mode == 0:
        char.火属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20590(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '暗强(13)')"
    if mode == 0:
        char.暗属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20591(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '暗强(14)')"
    if mode == 0:
        char.暗属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20592(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '暗强(15)')"
    if mode == 0:
        char.暗属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20593(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '冰强(13)')"
    if mode == 0:
        char.冰属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20594(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '冰强(14)')"
    if mode == 0:
        char.冰属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20595(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '冰强(15)')"
    if mode == 0:
        char.冰属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20596(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '耳环', '四维(55)')"
    if mode == 0:
        char.基础属性加成(四维=55 * rate)
    if mode == 1:
        pass


def enchanting_20597(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '耳环', '四维(60)')"
    if mode == 0:
        char.基础属性加成(四维=60 * rate)
    if mode == 1:
        pass


def enchanting_20598(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '所有属性强化(13)')"
    if mode == 0:
        char.所有属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20599(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '所有属性强化(14)')"
    if mode == 0:
        char.所有属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20600(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '四维(21)')"
    if mode == 0:
        char.基础属性加成(四维=21 * rate)
    if mode == 1:
        pass


def enchanting_20601(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '四维(23)')"
    if mode == 0:
        char.基础属性加成(四维=23 * rate)
    if mode == 1:
        pass


def enchanting_20602(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '四维(25)')"
    if mode == 0:
        char.基础属性加成(四维=25 * rate)
    if mode == 1:
        pass


def enchanting_20603(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '魔法石', '所有属性强化(11)')"
    if mode == 0:
        char.所有属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_20604(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '魔法石', '四维(16)')"
    if mode == 0:
        char.基础属性加成(四维=16 * rate)
    if mode == 1:
        pass


def enchanting_20605(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '魔法石', '四维(18)')"
    if mode == 0:
        char.基础属性加成(四维=18 * rate)
    if mode == 1:
        pass


def enchanting_20606(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '魔法石', '四维(20)')"
    if mode == 0:
        char.基础属性加成(四维=20 * rate)
    if mode == 1:
        pass


def enchanting_20607(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力智(30)')"
    if mode == 0:
        char.基础属性加成(力智=30 * rate)
    if mode == 1:
        pass


def enchanting_20608(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体精(30)')"
    if mode == 0:
        char.基础属性加成(体精=30 * rate)
    if mode == 1:
        pass


def enchanting_20609(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '所有属性抗性(10)')"
    if mode == 0:
        char.所有属性抗性加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20610(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '三攻(30)')"
    if mode == 0:
        char.基础属性加成(三攻=30 * rate)
    if mode == 1:
        pass


def enchanting_20611(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '三攻(55)')"
    if mode == 0:
        char.基础属性加成(三攻=55 * rate)
    if mode == 1:
        pass


def enchanting_20612(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '四维(65)')"
    if mode == 0:
        char.基础属性加成(四维=65 * rate)
    if mode == 1:
        pass


def enchanting_20613(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '所有属性强化(24)')"
    if mode == 0:
        char.所有属性强化加成(24 * rate)
    if mode == 1:
        pass


def enchanting_20614(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '所有属性强化(25)')"
    if mode == 0:
        char.所有属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20615(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '火强(14)|光强(14)')"
    if mode == 0:
        char.火属性强化加成(14 * rate)
        char.光属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20616(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '火强(15)|光强(15)')"
    if mode == 0:
        char.火属性强化加成(15 * rate)
        char.光属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20617(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '冰强(14)|暗强(14)')"
    if mode == 0:
        char.冰属性强化加成(14 * rate)
        char.暗属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20618(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '冰强(15)|暗强(15)')"
    if mode == 0:
        char.冰属性强化加成(15 * rate)
        char.暗属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20619(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '力(45)')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
    if mode == 1:
        pass


def enchanting_20620(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '力(50)')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
    if mode == 1:
        pass


def enchanting_20621(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '智(45)')"
    if mode == 0:
        char.基础属性加成(智力=45 * rate)
    if mode == 1:
        pass


def enchanting_20622(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '智(50)')"
    if mode == 0:
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_20623(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '体(45)')"
    if mode == 0:
        char.基础属性加成(体力=45 * rate)
    if mode == 1:
        pass


def enchanting_20624(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '体(50)')"
    if mode == 0:
        char.基础属性加成(体力=50 * rate)
    if mode == 1:
        pass


def enchanting_20625(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '精(45)')"
    if mode == 0:
        char.基础属性加成(精神=45 * rate)
    if mode == 1:
        pass


def enchanting_20626(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '精(50)')"
    if mode == 0:
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20627(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '物暴(5%)|力(20)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20628(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '物暴(6%)|力(25)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
        char.基础属性加成(力量=25 * rate)
    if mode == 1:
        pass


def enchanting_20629(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '魔暴(5%)|智(20)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20630(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '魔暴(6%)|智(25)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.06 * rate)
        char.基础属性加成(智力=25 * rate)
    if mode == 1:
        pass


def enchanting_20631(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '腰带, 鞋', '物暴(2%)|力(20)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.02 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20632(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带, 鞋', '物暴(3%)|力(25)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(力量=25 * rate)
    if mode == 1:
        pass


def enchanting_20633(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '腰带, 鞋', '魔暴(2%)|智(20)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.02 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20634(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带, 鞋', '魔暴(3%)|智(25)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.基础属性加成(智力=25 * rate)
    if mode == 1:
        pass


def enchanting_20635(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '独立(60)|力(30)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=60 * rate)
        char.基础属性加成(力量=30 * rate)
    if mode == 1:
        pass


def enchanting_20636(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '独立(65)|力(35)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=65 * rate)
        char.基础属性加成(力量=35 * rate)
    if mode == 1:
        pass


def enchanting_20637(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '独立(70)|力(40)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=70 * rate)
        char.基础属性加成(力量=40 * rate)
    if mode == 1:
        pass


def enchanting_20638(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '独立(60)|智(30)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=60 * rate)
        char.基础属性加成(智力=30 * rate)
    if mode == 1:
        pass


def enchanting_20639(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '独立(65)|智(35)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=65 * rate)
        char.基础属性加成(智力=35 * rate)
    if mode == 1:
        pass


def enchanting_20640(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '独立(70)|智(40)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=70 * rate)
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_20641(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '体(80)')"
    if mode == 0:
        char.基础属性加成(体力=80 * rate)
    if mode == 1:
        pass


def enchanting_20642(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '体(90)')"
    if mode == 0:
        char.基础属性加成(体力=90 * rate)
    if mode == 1:
        pass


def enchanting_20643(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '体(100)')"
    if mode == 0:
        char.基础属性加成(体力=100 * rate)
    if mode == 1:
        pass


def enchanting_20644(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '精(80)')"
    if mode == 0:
        char.基础属性加成(精神=80 * rate)
    if mode == 1:
        pass


def enchanting_20645(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '精(90)')"
    if mode == 0:
        char.基础属性加成(精神=90 * rate)
    if mode == 1:
        pass


def enchanting_20646(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '精(100)')"
    if mode == 0:
        char.基础属性加成(精神=100 * rate)
    if mode == 1:
        pass


def enchanting_20647(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力(80)')"
    if mode == 0:
        char.基础属性加成(力量=80 * rate)
    if mode == 1:
        pass


def enchanting_20648(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力(90)')"
    if mode == 0:
        char.基础属性加成(力量=90 * rate)
    if mode == 1:
        pass


def enchanting_20649(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '力(100)')"
    if mode == 0:
        char.基础属性加成(力量=100 * rate)
    if mode == 1:
        pass


def enchanting_20650(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '智(80)')"
    if mode == 0:
        char.基础属性加成(智力=80 * rate)
    if mode == 1:
        pass


def enchanting_20651(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '智(90)')"
    if mode == 0:
        char.基础属性加成(智力=90 * rate)
    if mode == 1:
        pass


def enchanting_20652(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '智(100)')"
    if mode == 0:
        char.基础属性加成(智力=100 * rate)
    if mode == 1:
        pass


def enchanting_20653(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '魔攻(60)|智(30)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=60 * rate)
        char.基础属性加成(智力=30 * rate)
    if mode == 1:
        pass


def enchanting_20654(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '魔攻(65)|智(35)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=65 * rate)
        char.基础属性加成(智力=35 * rate)
    if mode == 1:
        pass


def enchanting_20655(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '魔攻(70)|智(40)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=70 * rate)
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_20656(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '物攻(60)|力(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=60 * rate)
        char.基础属性加成(力量=30 * rate)
    if mode == 1:
        pass


def enchanting_20657(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '物攻(65)|力(35)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=65 * rate)
        char.基础属性加成(力量=35 * rate)
    if mode == 1:
        pass


def enchanting_20658(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '物攻(70)|力(40)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=70 * rate)
        char.基础属性加成(力量=40 * rate)
    if mode == 1:
        pass


def enchanting_20659(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '四维(45)')"
    if mode == 0:
        char.基础属性加成(四维=45 * rate)
    if mode == 1:
        pass


def enchanting_20660(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '四维(55)')"
    if mode == 0:
        char.基础属性加成(四维=55 * rate)
    if mode == 1:
        pass


def enchanting_20661(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '力(35)')"
    if mode == 0:
        char.基础属性加成(力量=35 * rate)
    if mode == 1:
        pass


def enchanting_20662(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '力(40)')"
    if mode == 0:
        char.基础属性加成(力量=40 * rate)
    if mode == 1:
        pass


def enchanting_20663(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '智(35)')"
    if mode == 0:
        char.基础属性加成(智力=35 * rate)
    if mode == 1:
        pass


def enchanting_20664(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '智(40)')"
    if mode == 0:
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_20665(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '所有属性强化(11)')"
    if mode == 0:
        char.所有属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_20666(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '所有属性强化(13)')"
    if mode == 0:
        char.所有属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20667(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '火强(25)|光强(25)')"
    if mode == 0:
        char.火属性强化加成(25 * rate)
        char.光属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20668(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '冰强(25)|暗强(25)')"
    if mode == 0:
        char.冰属性强化加成(25 * rate)
        char.暗属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20669(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '力智(35)|物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(力智=35 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20670(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '体精(35)')"
    if mode == 0:
        char.基础属性加成(体精=35 * rate)
    if mode == 1:
        pass


def enchanting_20671(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '力智(20)|物暴(5%)|魔暴(5%)')"
    if mode == 0:
        char.基础属性加成(力智=20 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20672(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '腰带, 鞋', '力智(20)')"
    if mode == 0:
        char.基础属性加成(力智=20 * rate)
    if mode == 1:
        pass


def enchanting_20673(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '体精(20)')"
    if mode == 0:
        char.基础属性加成(体精=20 * rate)
    if mode == 1:
        pass


def enchanting_20674(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '所有属性强化(26)')"
    if mode == 0:
        char.所有属性强化加成(26 * rate)
    if mode == 1:
        pass


def enchanting_20675(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '所有属性强化(28)')"
    if mode == 0:
        char.所有属性强化加成(28 * rate)
    if mode == 1:
        pass


def enchanting_20676(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '魔法石', '四维(35)')"
    if mode == 0:
        char.基础属性加成(四维=35 * rate)
    if mode == 1:
        pass


def enchanting_20677(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '魔法石', '四维(40)')"
    if mode == 0:
        char.基础属性加成(四维=40 * rate)
    if mode == 1:
        pass


def enchanting_20678(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '四维(45)')"
    if mode == 0:
        char.基础属性加成(四维=45 * rate)
    if mode == 1:
        pass


def enchanting_20679(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '所有属性强化(17)')"
    if mode == 0:
        char.所有属性强化加成(17 * rate)
    if mode == 1:
        pass


def enchanting_20680(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '三攻(45)')"
    if mode == 0:
        char.基础属性加成(三攻=45 * rate)
    if mode == 1:
        pass


def enchanting_20681(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '火强(24)|光强(24)')"
    if mode == 0:
        char.火属性强化加成(24 * rate)
        char.光属性强化加成(24 * rate)
    if mode == 1:
        pass


def enchanting_20682(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '冰强(24)|暗强(24)')"
    if mode == 0:
        char.冰属性强化加成(24 * rate)
        char.暗属性强化加成(24 * rate)
    if mode == 1:
        pass


def enchanting_20683(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(10.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20684(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '施放速度(15.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.15 * rate)
    if mode == 1:
        pass


def enchanting_20685(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '鞋', '移动速度(10.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20686(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '辅助装备', '三攻(110)')"
    if mode == 0:
        char.基础属性加成(三攻=110 * rate)
    if mode == 1:
        pass


def enchanting_20687(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '辅助装备', '四维(100)')"
    if mode == 0:
        char.基础属性加成(四维=100 * rate)
    if mode == 1:
        pass


def enchanting_20688(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '魔法石', '所有属性强化(25)')"
    if mode == 0:
        char.所有属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20689(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '魔法石', '四维(80)')"
    if mode == 0:
        char.基础属性加成(四维=80 * rate)
    if mode == 1:
        pass


def enchanting_20690(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(158, '头肩', '四维(40)|三攻(10)|物暴(5%)|魔暴(5%)|技攻(2%)')"
    if mode == 0:
        char.基础属性加成(四维=40 * rate)
        char.基础属性加成(三攻=10 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
        char.技能攻击力加成(0.02 * rate)
    if mode == 1:
        pass


def enchanting_20691(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '物攻(15)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20692(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '物攻(17)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=17 * rate)
    if mode == 1:
        pass


def enchanting_20693(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '物攻(19)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=19 * rate)
    if mode == 1:
        pass


def enchanting_20694(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '物攻(21)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=21 * rate)
    if mode == 1:
        pass


def enchanting_20695(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '物攻(23)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=23 * rate)
    if mode == 1:
        pass


def enchanting_20696(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '魔攻(15)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20697(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '魔攻(17)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=17 * rate)
    if mode == 1:
        pass


def enchanting_20698(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '魔攻(19)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=19 * rate)
    if mode == 1:
        pass


def enchanting_20699(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '魔攻(21)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=21 * rate)
    if mode == 1:
        pass


def enchanting_20700(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '魔攻(23)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=23 * rate)
    if mode == 1:
        pass


def enchanting_20701(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '物暴(1%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20702(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '魔暴(1%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20703(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩', '魔暴(2%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.02 * rate)
    if mode == 1:
        pass


def enchanting_20704(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(35)')"
    if mode == 0:
        char.基础属性加成(智力=35 * rate)
    if mode == 1:
        pass


def enchanting_20705(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(45)')"
    if mode == 0:
        char.基础属性加成(体力=45 * rate)
    if mode == 1:
        pass


def enchanting_20706(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(45)')"
    if mode == 0:
        char.基础属性加成(精神=45 * rate)
    if mode == 1:
        pass


def enchanting_20707(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装, 鞋', '移动速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20708(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装, 鞋', '移动速度(2.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.02 * rate)
    if mode == 1:
        pass


def enchanting_20709(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装, 鞋', '移动速度(3.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20710(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '下装, 鞋', '移动速度(4.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20711(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装, 鞋', '施放速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20712(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装, 鞋', '施放速度(2.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.02 * rate)
    if mode == 1:
        pass


def enchanting_20713(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装, 鞋', '施放速度(3.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20714(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装, 鞋', '施放速度(4.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20715(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(2.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.02 * rate)
    if mode == 1:
        pass


def enchanting_20716(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(3.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20717(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '腰带', '四维(30)|Lv1~30主动+1')"
    if mode == 0:
        char.基础属性加成(四维=30 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 30, 1)
    if mode == 1:
        pass


def enchanting_20718(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '腰带, 头肩, 鞋', '力(15)')"
    if mode == 0:
        char.基础属性加成(力量=15 * rate)
    if mode == 1:
        pass


def enchanting_20719(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '腰带, 头肩, 鞋', '智(15)')"
    if mode == 0:
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_20720(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '体精(10)')"
    if mode == 0:
        char.基础属性加成(体精=10 * rate)
    if mode == 1:
        pass


def enchanting_20721(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(10)|暗强(10)')"
    if mode == 0:
        char.冰属性强化加成(10 * rate)
        char.暗属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20722(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '独立(40)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_20723(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '力(10)|物攻(10)')"
    if mode == 0:
        char.基础属性加成(力量=10 * rate)
        char.基础属性加成(物理攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_20724(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '智(10)|魔攻(10)')"
    if mode == 0:
        char.基础属性加成(智力=10 * rate)
        char.基础属性加成(魔法攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_20725(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '体精(10)')"
    if mode == 0:
        char.基础属性加成(体精=10 * rate)
    if mode == 1:
        pass


def enchanting_20726(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '腰带', 'Lv15~15主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 15, 15, 1)
    if mode == 1:
        pass


def enchanting_20727(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '腰带', 'Lv20~20主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 20, 20, 1)
    if mode == 1:
        pass


def enchanting_20728(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '腰带', 'Lv25~25主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 25, 25, 1)
    if mode == 1:
        pass


def enchanting_20729(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '腰带', 'Lv30~30主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 30, 30, 1)
    if mode == 1:
        pass


def enchanting_20730(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', '所有属性强化(15)|物攻(30)|魔攻(30)|独立(40)|Lv1~50主动+1')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(独立攻击力=40 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20731(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '鞋', '四维(30)|Lv1~30主动+1')"
    if mode == 0:
        char.基础属性加成(四维=30 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 30, 1)
    if mode == 1:
        pass


def enchanting_20732(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '所有属性强化(12)|物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20733(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '魔法石', '四维(30)|物攻(30)|魔攻(30)|独立(40)')"
    if mode == 0:
        char.基础属性加成(四维=30 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(独立攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_20734(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '力(42)')"
    if mode == 0:
        char.基础属性加成(力量=42 * rate)
    if mode == 1:
        pass


def enchanting_20735(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力智(21)')"
    if mode == 0:
        char.基础属性加成(力智=21 * rate)
    if mode == 1:
        pass


def enchanting_20736(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(21)|体(21)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.基础属性加成(体力=21 * rate)
    if mode == 1:
        pass


def enchanting_20737(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(21)|精(21)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.基础属性加成(精神=21 * rate)
    if mode == 1:
        pass


def enchanting_20738(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(21)|物攻(16)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.基础属性加成(物理攻击力=16 * rate)
    if mode == 1:
        pass


def enchanting_20739(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(21)|魔攻(16)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.基础属性加成(魔法攻击力=16 * rate)
    if mode == 1:
        pass


def enchanting_20740(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(21)|独立(26)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.基础属性加成(独立攻击力=26 * rate)
    if mode == 1:
        pass


def enchanting_20741(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(21)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20742(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(21)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20743(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(21)|火强(8)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20744(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(21)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20745(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(21)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20746(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(21)|光强(8)')"
    if mode == 0:
        char.基础属性加成(力量=21 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20747(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(42)')"
    if mode == 0:
        char.基础属性加成(智力=42 * rate)
    if mode == 1:
        pass


def enchanting_20748(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(21)|体(21)')"
    if mode == 0:
        char.基础属性加成(智力=21 * rate)
        char.基础属性加成(体力=21 * rate)
    if mode == 1:
        pass


def enchanting_20749(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(21)|精(21)')"
    if mode == 0:
        char.基础属性加成(智力=21 * rate)
        char.基础属性加成(精神=21 * rate)
    if mode == 1:
        pass


def enchanting_20750(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(21)|物攻(16)')"
    if mode == 0:
        char.基础属性加成(智力=21 * rate)
        char.基础属性加成(物理攻击力=16 * rate)
    if mode == 1:
        pass


def enchanting_20751(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(21)|魔攻(16)')"
    if mode == 0:
        char.基础属性加成(智力=21 * rate)
        char.基础属性加成(魔法攻击力=16 * rate)
    if mode == 1:
        pass


def enchanting_20752(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(21)|独立(26)')"
    if mode == 0:
        char.基础属性加成(智力=21 * rate)
        char.基础属性加成(独立攻击力=26 * rate)
    if mode == 1:
        pass


def enchanting_20753(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(21)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(智力=21 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20754(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(21)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(智力=21 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20755(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(21)|火强(8)')"
    if mode == 0:
        char.基础属性加成(智力=21 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20756(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(20)|冰强(7)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20757(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(20)|暗强(7)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20758(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(20)|光强(7)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20759(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(40)')"
    if mode == 0:
        char.基础属性加成(体力=40 * rate)
    if mode == 1:
        pass


def enchanting_20760(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体精(20)')"
    if mode == 0:
        char.基础属性加成(体精=20 * rate)
    if mode == 1:
        pass


def enchanting_20761(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(20)|物攻(15)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20762(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(20)|魔攻(15)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20763(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(20)|独立(25)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20764(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体(20)|物暴(3%)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20765(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体(20)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20766(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(20)|火强(7)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20767(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(20)|冰强(7)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20768(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(20)|暗强(7)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20769(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(20)|光强(7)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20770(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(40)')"
    if mode == 0:
        char.基础属性加成(精神=40 * rate)
    if mode == 1:
        pass


def enchanting_20771(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(20)|物攻(15)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20772(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(20)|魔攻(15)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20773(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(20)|独立(25)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20774(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '精(20)|物暴(3%)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20775(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '精(20)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20776(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(20)|火强(7)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20777(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(20)|冰强(7)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20778(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(20)|暗强(7)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20779(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(20)|光强(7)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20780(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20781(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(15)|魔攻(15)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20782(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(15)|独立(25)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20783(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(15)|物暴(3%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20784(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(15)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20785(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(15)|火强(7)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20786(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(15)|冰强(7)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20787(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(15)|暗强(7)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20788(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(15)|光强(7)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20789(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(30)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20790(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔攻(15)|独立(25)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20791(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔攻(15)|物暴(3%)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20792(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔攻(15)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20793(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(15)|火强(7)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20794(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(15)|冰强(7)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20795(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(15)|暗强(7)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20796(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(15)|光强(7)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20797(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '独立(50)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
    if mode == 1:
        pass


def enchanting_20798(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '独立(25)|物暴(3%)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20799(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '独立(25)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20800(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '独立(25)|火强(7)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20801(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '独立(25)|冰强(7)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20802(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '独立(25)|暗强(7)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20803(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '独立(25)|光强(7)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20804(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(6%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20805(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20806(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(3%)|火强(7)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20807(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(3%)|冰强(7)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20808(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(3%)|暗强(7)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20809(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(3%)|光强(7)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20810(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔暴(6%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20811(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔暴(3%)|火强(7)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20812(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔暴(3%)|冰强(7)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20813(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔暴(3%)|暗强(7)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20814(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔暴(3%)|光强(7)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20815(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '火强(14)')"
    if mode == 0:
        char.火属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20816(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '火强(7)|冰强(7)')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20817(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '火强(7)|暗强(7)')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20818(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '火强(7)|光强(7)')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20819(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '冰强(14)')"
    if mode == 0:
        char.冰属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20820(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '冰强(7)|暗强(7)')"
    if mode == 0:
        char.冰属性强化加成(7 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20821(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '冰强(7)|光强(7)')"
    if mode == 0:
        char.冰属性强化加成(7 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20822(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '暗强(14)')"
    if mode == 0:
        char.暗属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20823(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '暗强(7)|光强(7)')"
    if mode == 0:
        char.暗属性强化加成(7 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20824(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '光强(14)')"
    if mode == 0:
        char.光属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20825(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '独立(25)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20826(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(20)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20827(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔攻(15)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20828(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '精(20)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
    if mode == 1:
        pass


def enchanting_20829(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '光强(7)')"
    if mode == 0:
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20830(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体(20)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
    if mode == 1:
        pass


def enchanting_20831(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '冰强(7)')"
    if mode == 0:
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20832(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20833(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(15)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20834(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(20)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20835(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '火强(7)')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20836(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(3%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20837(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '暗强(7)')"
    if mode == 0:
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20838(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '魔攻(41)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=41 * rate)
    if mode == 1:
        pass


def enchanting_20839(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '魔攻(43)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=43 * rate)
    if mode == 1:
        pass


def enchanting_20840(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '物攻(41)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=41 * rate)
    if mode == 1:
        pass


def enchanting_20841(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '物攻(43)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=43 * rate)
    if mode == 1:
        pass


def enchanting_20842(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '体(60)')"
    if mode == 0:
        char.基础属性加成(体力=60 * rate)
    if mode == 1:
        pass


def enchanting_20843(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '体(65)')"
    if mode == 0:
        char.基础属性加成(体力=65 * rate)
    if mode == 1:
        pass


def enchanting_20844(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '腰带, 鞋', '精(32)')"
    if mode == 0:
        char.基础属性加成(精神=32 * rate)
    if mode == 1:
        pass


def enchanting_20845(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(35)|精(30)')"
    if mode == 0:
        char.基础属性加成(体力=35 * rate)
        char.基础属性加成(精神=30 * rate)
    if mode == 1:
        pass


def enchanting_20846(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩, 腰带, 鞋', '精(60)')"
    if mode == 0:
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20847(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '力(60)')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
    if mode == 1:
        pass


def enchanting_20848(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '力(65)')"
    if mode == 0:
        char.基础属性加成(力量=65 * rate)
    if mode == 1:
        pass


def enchanting_20849(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '智(60)')"
    if mode == 0:
        char.基础属性加成(智力=60 * rate)
    if mode == 1:
        pass


def enchanting_20850(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '智(65)')"
    if mode == 0:
        char.基础属性加成(智力=65 * rate)
    if mode == 1:
        pass


def enchanting_20851(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性抗性(20)')"
    if mode == 0:
        char.所有属性抗性加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20852(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '所有属性强化(8)')"
    if mode == 0:
        char.所有属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20853(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '所有属性强化(9)')"
    if mode == 0:
        char.所有属性强化加成(9 * rate)
    if mode == 1:
        pass


def enchanting_20854(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '所有属性强化(10)')"
    if mode == 0:
        char.所有属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20855(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '所有属性强化(12)')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20856(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '物攻(26)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=26 * rate)
    if mode == 1:
        pass


def enchanting_20857(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '物攻(27)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=27 * rate)
    if mode == 1:
        pass


def enchanting_20858(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '物攻(28)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=28 * rate)
    if mode == 1:
        pass


def enchanting_20859(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '物攻(29)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=29 * rate)
    if mode == 1:
        pass


def enchanting_20860(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '魔攻(26)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=26 * rate)
    if mode == 1:
        pass


def enchanting_20861(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '魔攻(27)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=27 * rate)
    if mode == 1:
        pass


def enchanting_20862(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '魔攻(28)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=28 * rate)
    if mode == 1:
        pass


def enchanting_20863(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '魔攻(29)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=29 * rate)
    if mode == 1:
        pass


def enchanting_20864(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '四维(10)|物暴(5%)|魔暴(5%)|城镇移动速度(0.1)')"
    if mode == 0:
        char.基础属性加成(四维=10 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20865(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '物暴(8%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20866(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '魔暴(8%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20867(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '物攻(21)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=21 * rate)
    if mode == 1:
        pass


def enchanting_20868(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '物攻(22)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=22 * rate)
    if mode == 1:
        pass


def enchanting_20869(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '物攻(23)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=23 * rate)
    if mode == 1:
        pass


def enchanting_20870(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '上衣, 下装', '物攻(24)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=24 * rate)
    if mode == 1:
        pass


def enchanting_20871(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '魔攻(21)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=21 * rate)
    if mode == 1:
        pass


def enchanting_20872(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '力(32)')"
    if mode == 0:
        char.基础属性加成(力量=32 * rate)
    if mode == 1:
        pass


def enchanting_20873(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '智(32)')"
    if mode == 0:
        char.基础属性加成(智力=32 * rate)
    if mode == 1:
        pass


def enchanting_20874(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '智(41)')"
    if mode == 0:
        char.基础属性加成(智力=41 * rate)
    if mode == 1:
        pass


def enchanting_20875(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '智(42)')"
    if mode == 0:
        char.基础属性加成(智力=42 * rate)
    if mode == 1:
        pass


def enchanting_20876(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '智(43)')"
    if mode == 0:
        char.基础属性加成(智力=43 * rate)
    if mode == 1:
        pass


def enchanting_20877(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '智(44)')"
    if mode == 0:
        char.基础属性加成(智力=44 * rate)
    if mode == 1:
        pass


def enchanting_20878(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '智(45)')"
    if mode == 0:
        char.基础属性加成(智力=45 * rate)
    if mode == 1:
        pass


def enchanting_20879(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '智(46)')"
    if mode == 0:
        char.基础属性加成(智力=46 * rate)
    if mode == 1:
        pass


def enchanting_20880(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '智(47)')"
    if mode == 0:
        char.基础属性加成(智力=47 * rate)
    if mode == 1:
        pass


def enchanting_20881(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '智(48)')"
    if mode == 0:
        char.基础属性加成(智力=48 * rate)
    if mode == 1:
        pass


def enchanting_20882(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '智(49)')"
    if mode == 0:
        char.基础属性加成(智力=49 * rate)
    if mode == 1:
        pass


def enchanting_20883(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '上衣, 下装', '智(50)')"
    if mode == 0:
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_20884(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '腰带, 鞋', '体(32)')"
    if mode == 0:
        char.基础属性加成(体力=32 * rate)
    if mode == 1:
        pass


def enchanting_20885(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣, 下装', '物攻(40)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_20886(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣, 下装', '魔攻(40)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_20887(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣, 下装', '独立(40)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_20888(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '上衣, 下装', '智(55)')"
    if mode == 0:
        char.基础属性加成(智力=55 * rate)
    if mode == 1:
        pass


def enchanting_20889(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv15~15主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 15, 15, 1)
    if mode == 1:
        pass


def enchanting_20890(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv20~20主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 20, 20, 1)
    if mode == 1:
        pass


def enchanting_20891(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv25~25主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 25, 25, 1)
    if mode == 1:
        pass


def enchanting_20892(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv30~30主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 30, 30, 1)
    if mode == 1:
        pass


def enchanting_20893(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv35~35主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 35, 35, 1)
    if mode == 1:
        pass


def enchanting_20894(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '四维(30)')"
    if mode == 0:
        char.基础属性加成(四维=30 * rate)
    if mode == 1:
        pass


def enchanting_20895(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '四维(35)')"
    if mode == 0:
        char.基础属性加成(四维=35 * rate)
    if mode == 1:
        pass


def enchanting_20896(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '四维(40)')"
    if mode == 0:
        char.基础属性加成(四维=40 * rate)
    if mode == 1:
        pass


def enchanting_20897(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '四维(45)')"
    if mode == 0:
        char.基础属性加成(四维=45 * rate)
    if mode == 1:
        pass


def enchanting_20898(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '四维(50)')"
    if mode == 0:
        char.基础属性加成(四维=50 * rate)
    if mode == 1:
        pass


def enchanting_20899(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '上衣, 下装', '三攻(30)')"
    if mode == 0:
        char.基础属性加成(三攻=30 * rate)
    if mode == 1:
        pass


def enchanting_20900(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '力智(50)')"
    if mode == 0:
        char.基础属性加成(力智=50 * rate)
    if mode == 1:
        pass


def enchanting_20901(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体精(35)')"
    if mode == 0:
        char.基础属性加成(体精=35 * rate)
    if mode == 1:
        pass


def enchanting_20902(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '力智(32)|体精(28)')"
    if mode == 0:
        char.基础属性加成(力智=32 * rate)
        char.基础属性加成(体精=28 * rate)
    if mode == 1:
        pass


def enchanting_20903(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力智(15)|独立(45)')"
    if mode == 0:
        char.基础属性加成(力智=15 * rate)
        char.基础属性加成(独立攻击力=45 * rate)
    if mode == 1:
        pass


def enchanting_20904(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装, 武器', '物攻(45)|力(15)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=45 * rate)
        char.基础属性加成(力量=15 * rate)
    if mode == 1:
        pass


def enchanting_20905(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装, 武器', '魔攻(45)|智(15)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=45 * rate)
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_20906(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装, 武器', '独立(45)|力(15)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=45 * rate)
        char.基础属性加成(力量=15 * rate)
    if mode == 1:
        pass


def enchanting_20907(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装, 武器', '独立(45)|智(15)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=45 * rate)
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_20908(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '耳环', '四维(80)')"
    if mode == 0:
        char.基础属性加成(四维=80 * rate)
    if mode == 1:
        pass


def enchanting_20909(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '腰带', 'Lv1~35主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 35, 1)
    if mode == 1:
        pass


def enchanting_20910(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '四维(20)|所有属性强化(10)|所有属性抗性(10)')"
    if mode == 0:
        char.基础属性加成(四维=20 * rate)
        char.所有属性强化加成(10 * rate)
        char.所有属性抗性加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20911(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv1~35主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 35, 1)
    if mode == 1:
        pass


def enchanting_20912(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '鞋', 'Lv1~35主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 35, 1)
    if mode == 1:
        pass


def enchanting_20913(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '所有属性强化(12)')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20914(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv1~10主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 10, 1)
    if mode == 1:
        pass


def enchanting_20915(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv10~20主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 10, 20, 1)
    if mode == 1:
        pass


def enchanting_20916(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv20~30主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 20, 30, 1)
    if mode == 1:
        pass


def enchanting_20917(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv30~40主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 30, 40, 1)
    if mode == 1:
        pass


def enchanting_20918(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv40~50主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 40, 50, 1)
    if mode == 1:
        pass


def enchanting_20919(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv1~20主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 20, 1)
    if mode == 1:
        pass


def enchanting_20920(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv10~30主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 10, 30, 1)
    if mode == 1:
        pass


def enchanting_20921(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv20~40主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 20, 40, 1)
    if mode == 1:
        pass


def enchanting_20922(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', 'Lv30~50主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 30, 50, 1)
    if mode == 1:
        pass


def enchanting_20923(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', 'Lv1~50主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20924(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', 'Lv1~10主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 10, 1)
    if mode == 1:
        pass


def enchanting_20925(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', 'Lv10~20主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 10, 20, 1)
    if mode == 1:
        pass


def enchanting_20926(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', 'Lv20~30主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 20, 30, 1)
    if mode == 1:
        pass


def enchanting_20927(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', 'Lv30~40主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 30, 40, 1)
    if mode == 1:
        pass


def enchanting_20928(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', 'Lv40~50主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 40, 50, 1)
    if mode == 1:
        pass


def enchanting_20929(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', 'Lv1~20主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 20, 1)
    if mode == 1:
        pass


def enchanting_20930(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', 'Lv10~30主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 10, 30, 1)
    if mode == 1:
        pass


def enchanting_20931(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', 'Lv20~40主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 20, 40, 1)
    if mode == 1:
        pass


def enchanting_20932(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', 'Lv30~50主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 30, 50, 1)
    if mode == 1:
        pass


def enchanting_20933(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '称号', 'Lv1~50主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20934(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '所有属性强化(30)')"
    if mode == 0:
        char.所有属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20935(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '魔法石', '精(30)')"
    if mode == 0:
        char.基础属性加成(精神=30 * rate)
    if mode == 1:
        pass


def enchanting_20936(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '三攻(35)')"
    if mode == 0:
        char.基础属性加成(三攻=35 * rate)
    if mode == 1:
        pass


def enchanting_20937(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '三攻(42)|物暴(2%)|魔暴(2%)')"
    if mode == 0:
        char.基础属性加成(三攻=42 * rate)
        char.基础属性加成(物理暴击率=0.02 * rate)
        char.基础属性加成(魔法暴击率=0.02 * rate)
    if mode == 1:
        pass


def enchanting_20938(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '上衣, 下装', '物攻(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20939(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '上衣, 下装', '魔攻(30)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20940(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '上衣, 下装', '独立(30)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20941(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '体精(75)')"
    if mode == 0:
        char.基础属性加成(体精=75 * rate)
    if mode == 1:
        pass


def enchanting_20942(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '物攻(50)|力(20)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20943(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '魔攻(50)|智(20)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20944(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '独立(50)|力(20)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20945(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '独立(50)|智(20)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20946(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣, 下装', '智(75)')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20947(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '腰带, 鞋', '智(50)')"
    if mode == 0:
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_20948(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '腰带, 鞋', '力(50)')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
    if mode == 1:
        pass


def enchanting_20949(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '物暴(10%)|魔暴(10%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.1 * rate)
        char.基础属性加成(魔法暴击率=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20950(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链', '所有属性强化(10)')"
    if mode == 0:
        char.所有属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20951(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链', '所有属性强化(15)')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20952(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链', '所有属性强化(23)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20953(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链', '四维(42)')"
    if mode == 0:
        char.基础属性加成(四维=42 * rate)
    if mode == 1:
        pass


def enchanting_20954(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链', '四维(25)')"
    if mode == 0:
        char.基础属性加成(四维=25 * rate)
    if mode == 1:
        pass


def enchanting_20955(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链', '四维(18)')"
    if mode == 0:
        char.基础属性加成(四维=18 * rate)
    if mode == 1:
        pass


def enchanting_20956(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '戒指', '所有属性强化(10)')"
    if mode == 0:
        char.所有属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20957(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '戒指', '所有属性强化(15)')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20958(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '戒指', '所有属性强化(23)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20959(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '戒指', '四维(42)')"
    if mode == 0:
        char.基础属性加成(四维=42 * rate)
    if mode == 1:
        pass


def enchanting_20960(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '戒指', '四维(25)')"
    if mode == 0:
        char.基础属性加成(四维=25 * rate)
    if mode == 1:
        pass


def enchanting_20961(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '戒指', '四维(18)')"
    if mode == 0:
        char.基础属性加成(四维=18 * rate)
    if mode == 1:
        pass


def enchanting_20962(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '所有属性强化(10)')"
    if mode == 0:
        char.所有属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20963(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '手镯', '所有属性强化(15)')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20964(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '手镯', '所有属性强化(23)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20965(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '手镯', '四维(42)')"
    if mode == 0:
        char.基础属性加成(四维=42 * rate)
    if mode == 1:
        pass


def enchanting_20966(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '手镯', '四维(25)')"
    if mode == 0:
        char.基础属性加成(四维=25 * rate)
    if mode == 1:
        pass


def enchanting_20967(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '手镯', '四维(18)')"
    if mode == 0:
        char.基础属性加成(四维=18 * rate)
    if mode == 1:
        pass


def enchanting_20968(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '四维(30)')"
    if mode == 0:
        char.基础属性加成(四维=30 * rate)
    if mode == 1:
        pass


def enchanting_20969(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '辅助装备', '四维(45)')"
    if mode == 0:
        char.基础属性加成(四维=45 * rate)
    if mode == 1:
        pass


def enchanting_20970(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '三攻(30)')"
    if mode == 0:
        char.基础属性加成(三攻=30 * rate)
    if mode == 1:
        pass


def enchanting_20971(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '辅助装备', '三攻(50)')"
    if mode == 0:
        char.基础属性加成(三攻=50 * rate)
    if mode == 1:
        pass


def enchanting_20972(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '辅助装备', '三攻(35)')"
    if mode == 0:
        char.基础属性加成(三攻=35 * rate)
    if mode == 1:
        pass


def enchanting_20973(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '智(75)')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20974(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '三攻(50)')"
    if mode == 0:
        char.基础属性加成(三攻=50 * rate)
    if mode == 1:
        pass


def enchanting_20975(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '智(75)')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20976(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(158, '魔法石', '所有属性强化(30)')"
    if mode == 0:
        char.所有属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20977(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(158, '魔法石', '四维(100)')"
    if mode == 0:
        char.基础属性加成(四维=100 * rate)
    if mode == 1:
        pass


def enchanting_20978(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '三攻(90)')"
    if mode == 0:
        char.基础属性加成(三攻=90 * rate)
    if mode == 1:
        pass


def enchanting_20979(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '辅助装备', '三攻(100)')"
    if mode == 0:
        char.基础属性加成(三攻=100 * rate)
    if mode == 1:
        pass


def enchanting_20980(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '四维(90)')"
    if mode == 0:
        char.基础属性加成(四维=90 * rate)
    if mode == 1:
        pass


def enchanting_20981(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '辅助装备', '四维(95)')"
    if mode == 0:
        char.基础属性加成(四维=95 * rate)
    if mode == 1:
        pass


def enchanting_20982(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '所有属性强化(21)')"
    if mode == 0:
        char.所有属性强化加成(21 * rate)
    if mode == 1:
        pass


def enchanting_20983(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '魔法石', '所有属性强化(23)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20984(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '四维(70)')"
    if mode == 0:
        char.基础属性加成(四维=70 * rate)
    if mode == 1:
        pass


def enchanting_20985(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '魔法石', '四维(75)')"
    if mode == 0:
        char.基础属性加成(四维=75 * rate)
    if mode == 1:
        pass


def enchanting_20986(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '头肩', '四维(30)|三攻(6)|物暴(5%)|魔暴(5%)|技攻(2%)')"
    if mode == 0:
        char.基础属性加成(四维=30 * rate)
        char.基础属性加成(三攻=6 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
        char.技能攻击力加成(0.02 * rate)
    if mode == 1:
        pass


def enchanting_20987(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '头肩', '四维(35)|三攻(8)|物暴(5%)|魔暴(5%)|技攻(2%)')"
    if mode == 0:
        char.基础属性加成(四维=35 * rate)
        char.基础属性加成(三攻=8 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
        char.技能攻击力加成(0.02 * rate)
    if mode == 1:
        pass


def enchanting_20988(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力智(75)')"
    if mode == 0:
        char.基础属性加成(力智=75 * rate)
    if mode == 1:
        pass


def enchanting_20989(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力(25)|物攻(55)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(物理攻击力=55 * rate)
    if mode == 1:
        pass


def enchanting_20990(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '智(25)|魔攻(55)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(魔法攻击力=55 * rate)
    if mode == 1:
        pass


def enchanting_20991(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力(25)|独立(55)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(独立攻击力=55 * rate)
    if mode == 1:
        pass


def enchanting_20992(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '智(25)|独立(55)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(独立攻击力=55 * rate)
    if mode == 1:
        pass


def enchanting_20993(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(8.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20994(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(10.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20995(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '施放速度(12.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.12 * rate)
    if mode == 1:
        pass


def enchanting_20996(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '施放速度(15.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.15 * rate)
    if mode == 1:
        pass


def enchanting_20997(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '耳环', '四维(110)')"
    if mode == 0:
        char.基础属性加成(四维=110 * rate)
    if mode == 1:
        pass


def enchanting_20998(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带, 鞋', '物暴(5%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20999(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带, 鞋', '物暴(6%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_21000(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '腰带, 鞋', '物暴(7%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_21001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带, 鞋', '魔暴(5%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_21002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带, 鞋', '魔暴(6%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_21003(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '腰带, 鞋', '魔暴(7%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_21004(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', '施放速度(9.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.09 * rate)
    if mode == 1:
        pass


def enchanting_21005(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '体(50)')"
    if mode == 0:
        char.基础属性加成(体力=50 * rate)
    if mode == 1:
        pass


def enchanting_21006(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '精(50)')"
    if mode == 0:
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_21007(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '上衣, 下装', '体(50)')"
    if mode == 0:
        char.基础属性加成(体力=50 * rate)
    if mode == 1:
        pass


def enchanting_21008(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '上衣, 下装', '精(50)')"
    if mode == 0:
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_21009(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣, 下装', '三攻(45)')"
    if mode == 0:
        char.基础属性加成(三攻=45 * rate)
    if mode == 1:
        pass


def enchanting_21010(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '冰强(21)|暗强(21)')"
    if mode == 0:
        char.冰属性强化加成(21 * rate)
        char.暗属性强化加成(21 * rate)
    if mode == 1:
        pass


def enchanting_21011(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '四维(35)')"
    if mode == 0:
        char.基础属性加成(四维=35 * rate)
    if mode == 1:
        pass


def enchanting_21012(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '所有属性强化(18)|物暴(2%)|魔暴(2%)')"
    if mode == 0:
        char.所有属性强化加成(18 * rate)
        char.基础属性加成(物理暴击率=0.02 * rate)
        char.基础属性加成(魔法暴击率=0.02 * rate)
    if mode == 1:
        pass


def enchanting_21013(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '鞋', '四维(45)|Lv1~30主动+1')"
    if mode == 0:
        char.基础属性加成(四维=45 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 30, 1)
    if mode == 1:
        pass


def enchanting_21014(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '辅助装备', '所有属性强化(12)|物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21015(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '四维(75)|物暴(5%)|魔暴(5%)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(四维=75 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21016(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(12)|光强(12)')"
    if mode == 0:
        char.火属性强化加成(12 * rate)
        char.光属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_21017(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(12)|暗强(12)')"
    if mode == 0:
        char.冰属性强化加成(12 * rate)
        char.暗属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_21018(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '力(50)')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
    if mode == 1:
        pass


def enchanting_21019(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力智(25)')"
    if mode == 0:
        char.基础属性加成(力智=25 * rate)
    if mode == 1:
        pass


def enchanting_21020(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(25)|体(25)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(体力=25 * rate)
    if mode == 1:
        pass


def enchanting_21021(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(25)|精(25)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(精神=25 * rate)
    if mode == 1:
        pass


def enchanting_21022(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(25)|物攻(20)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21023(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(25)|魔攻(20)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21024(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(25)|独立(30)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21025(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(25)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21026(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(25)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21027(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(25)|火强(8)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21028(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(25)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21029(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(25)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21030(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(25)|光强(8)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21031(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '智(50)')"
    if mode == 0:
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_21032(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(25)|体(25)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(体力=25 * rate)
    if mode == 1:
        pass


def enchanting_21033(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(25)|精(25)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(精神=25 * rate)
    if mode == 1:
        pass


def enchanting_21034(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(25)|物攻(20)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21035(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(25)|魔攻(20)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21036(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(25)|独立(30)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21037(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(25)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21038(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(25)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21039(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(25)|火强(8)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21040(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(25)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21041(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(25)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21042(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(25)|光强(8)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21043(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '体(50)')"
    if mode == 0:
        char.基础属性加成(体力=50 * rate)
    if mode == 1:
        pass


def enchanting_21044(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体精(25)')"
    if mode == 0:
        char.基础属性加成(体精=25 * rate)
    if mode == 1:
        pass


def enchanting_21045(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体(25)|物攻(20)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21046(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体(25)|魔攻(20)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21047(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(25)|独立(30)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21048(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体(25)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21049(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体(25)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21050(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(25)|火强(8)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21051(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(25)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21052(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(25)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21053(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(25)|光强(8)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21054(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '精(50)')"
    if mode == 0:
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_21055(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '精(25)|物攻(20)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21056(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '精(25)|魔攻(20)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21057(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(25)|独立(30)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21058(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '精(25)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21059(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '精(25)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21060(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(25)|火强(8)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21061(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(25)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21062(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(25)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21063(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(25)|光强(8)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21064(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '物攻(40)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_21065(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(20)|魔攻(20)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21066(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(20)|独立(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21067(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(20)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21068(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(20)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21069(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(20)|火强(8)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21070(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(20)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21071(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(20)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21072(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(20)|光强(8)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21073(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '魔攻(40)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_21074(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(20)|独立(30)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21075(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔攻(20)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21076(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔攻(20)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21077(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(20)|火强(8)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21078(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(20)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21079(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(20)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21080(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(20)|光强(8)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21081(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '独立(60)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_21082(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '独立(30)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21083(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '独立(30)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21084(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '独立(30)|火强(8)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21085(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '独立(30)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21086(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '独立(30)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21087(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '独立(30)|光强(8)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21088(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(8%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_21089(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(4%)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21090(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物暴(4%)|火强(8)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21091(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物暴(4%)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21092(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物暴(4%)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21093(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物暴(4%)|光强(8)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21094(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔暴(8%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_21095(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔暴(4%)|火强(8)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21096(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔暴(4%)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21097(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔暴(4%)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21098(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔暴(4%)|光强(8)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21099(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '火强(16)')"
    if mode == 0:
        char.火属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_21100(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '火强(8)|冰强(8)')"
    if mode == 0:
        char.火属性强化加成(8 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21101(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '火强(8)|暗强(8)')"
    if mode == 0:
        char.火属性强化加成(8 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21102(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '火强(8)|光强(8)')"
    if mode == 0:
        char.火属性强化加成(8 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21103(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '冰强(16)')"
    if mode == 0:
        char.冰属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_21104(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '冰强(8)|暗强(8)')"
    if mode == 0:
        char.冰属性强化加成(8 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21105(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '冰强(8)|光强(8)')"
    if mode == 0:
        char.冰属性强化加成(8 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21106(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '暗强(16)')"
    if mode == 0:
        char.暗属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_21107(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '暗强(8)|光强(8)')"
    if mode == 0:
        char.暗属性强化加成(8 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21108(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '光强(16)')"
    if mode == 0:
        char.光属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_21109(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '四维(24)')"
    if mode == 0:
        char.基础属性加成(四维=24 * rate)
    if mode == 1:
        pass


def enchanting_21110(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '三攻(25)')"
    if mode == 0:
        char.基础属性加成(三攻=25 * rate)
    if mode == 1:
        pass


def enchanting_21111(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣, 下装', '物攻(35)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=35 * rate)
    if mode == 1:
        pass


def enchanting_21112(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩, 腰带, 鞋', '物暴(5%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_21113(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣, 下装', '智(55)')"
    if mode == 0:
        char.基础属性加成(智力=55 * rate)
    if mode == 1:
        pass


def enchanting_21114(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩, 腰带, 鞋', '魔暴(5%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_21115(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '四维(32)')"
    if mode == 0:
        char.基础属性加成(四维=32 * rate)
    if mode == 1:
        pass


def enchanting_21116(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '力智(45)')"
    if mode == 0:
        char.基础属性加成(力智=45 * rate)
    if mode == 1:
        pass


def enchanting_21117(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', 'Lv15~25主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 15, 25, 1)
    if mode == 1:
        pass


def enchanting_21118(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', 'Lv25~35主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 25, 35, 1)
    if mode == 1:
        pass


def enchanting_21119(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '三攻(20)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(三攻=20 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21120(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', '三攻(40)|所有属性强化(15)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(三攻=40 * rate)
        char.所有属性强化加成(15 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21121(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '四维(75)|三攻(20)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(四维=75 * rate)
        char.基础属性加成(三攻=20 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21122(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带', '四维(45)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(四维=45 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21123(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '耳环', '四维(140)')"
    if mode == 0:
        char.基础属性加成(四维=140 * rate)
    if mode == 1:
        pass


def enchanting_21124(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '体(10)')"
    if mode == 0:
        char.基础属性加成(体力=10 * rate)
    if mode == 1:
        pass


def enchanting_21125(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣, 下装', '精(10)')"
    if mode == 0:
        char.基础属性加成(精神=10 * rate)
    if mode == 1:
        pass


def enchanting_21126(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(25)|物攻(30)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21127(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(25)|魔攻(30)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21128(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(25)|物攻(30)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21129(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(25)|魔攻(30)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21130(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(25)|物攻(30)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21131(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '体(25)|魔攻(30)')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21132(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(25)|物攻(30)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21133(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '精(25)|魔攻(30)')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21134(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '物攻(60)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_21135(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(30)|魔攻(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21136(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(30)|独立(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21137(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '物攻(30)|火强(8)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21138(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '物攻(30)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21139(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '物攻(30)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21140(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '物攻(30)|光强(8)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21141(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '魔攻(60)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_21142(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(30)|独立(30)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21143(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '魔攻(30)|火强(8)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21144(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '魔攻(30)|冰强(8)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21145(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '魔攻(30)|暗强(8)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21146(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '魔攻(30)|光强(8)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21147(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '武器', '力智(50)|三攻(50)|所有属性强化(16)')"
    if mode == 0:
        char.基础属性加成(力智=50 * rate)
        char.基础属性加成(三攻=50 * rate)
        char.所有属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_21148(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(30)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21149(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '物攻(30)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21150(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(30)|物暴(4%)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21151(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '魔攻(30)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21152(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '武器', '所有属性强化(15)|物攻(30)|独立(30)|攻击速度(5.0%)')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
        char.基础属性加成(攻击速度=0.05 * rate)
    if mode == 1:
        pass


def enchanting_21153(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '武器', '所有属性强化(15)|魔攻(30)|独立(30)|施放速度(5.0%)')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
        char.基础属性加成(施放速度=0.05 * rate)
    if mode == 1:
        pass


def enchanting_21154(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '力智(75)')"
    if mode == 0:
        char.基础属性加成(力智=75 * rate)
    if mode == 1:
        pass


def enchanting_21155(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '体精(75)')"
    if mode == 0:
        char.基础属性加成(体精=75 * rate)
    if mode == 1:
        pass


def enchanting_21156(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '腰带', '四维(45)')"
    if mode == 0:
        char.基础属性加成(四维=45 * rate)
    if mode == 1:
        pass


def enchanting_21157(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '腰带', '三攻(36)')"
    if mode == 0:
        char.基础属性加成(三攻=36 * rate)
    if mode == 1:
        pass


def enchanting_21158(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '鞋', '三攻(36)')"
    if mode == 0:
        char.基础属性加成(三攻=36 * rate)
    if mode == 1:
        pass


def enchanting_21159(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '耳环', '四维(135)')"
    if mode == 0:
        char.基础属性加成(四维=135 * rate)
    if mode == 1:
        pass


def enchanting_21160(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '称号', '三攻(30)|Lv1~35主动+1')"
    if mode == 0:
        char.基础属性加成(三攻=30 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 35, 1)
    if mode == 1:
        pass


def enchanting_21161(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '头肩', '四维(30)|三攻(10)|Lv1~35主动+1')"
    if mode == 0:
        char.基础属性加成(四维=30 * rate)
        char.基础属性加成(三攻=10 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 35, 1)
    if mode == 1:
        pass


def enchanting_21162(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '体精(70)')"
    if mode == 0:
        char.基础属性加成(体精=70 * rate)
    if mode == 1:
        pass


def enchanting_21163(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', 'Lv1~50主动+2')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 2)
    if mode == 1:
        pass


def enchanting_21164(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '称号', '三攻(30)|所有属性强化(10)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(三攻=30 * rate)
        char.所有属性强化加成(10 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21165(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '四维(75)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(四维=75 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21166(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '三攻(40)')"
    if mode == 0:
        char.基础属性加成(三攻=40 * rate)
    if mode == 1:
        pass


def enchanting_21167(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '鞋', '四维(45)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(四维=45 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21168(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', '三攻(40)|所有属性强化(15)|技攻(3%)')"
    if mode == 0:
        char.基础属性加成(三攻=40 * rate)
        char.所有属性强化加成(15 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_21169(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '四维(75)|三攻(20)|技攻(3%)')"
    if mode == 0:
        char.基础属性加成(四维=75 * rate)
        char.基础属性加成(三攻=20 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_21170(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '四维(60)|三攻(16)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(四维=60 * rate)
        char.基础属性加成(三攻=16 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21171(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带', '四维(36)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(四维=36 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21172(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '鞋', '四维(36)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(四维=36 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21173(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '辅助装备', '所有属性强化(9)|物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.所有属性强化加成(9 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21174(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '物攻(50)|独立(50)|力(20)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_21175(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '魔攻(50)|独立(50)|智(20)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_21176(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '鞋', '三攻(36)|技攻(3%)')"
    if mode == 0:
        char.基础属性加成(三攻=36 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_21177(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带', '三攻(36)|技攻(3%)')"
    if mode == 0:
        char.基础属性加成(三攻=36 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_21178(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', 'Lv1~50主动+1')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21179(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '攻击速度(0.5%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.005 * rate)
    if mode == 1:
        pass


def enchanting_21180(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '攻击速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_21181(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '攻击速度(4.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21182(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '施放速度(0.5%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.005 * rate)
    if mode == 1:
        pass


def enchanting_21183(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '施放速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_21184(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '施放速度(4.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21185(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '暗强(1)')"
    if mode == 0:
        char.暗属性强化加成(1 * rate)
    if mode == 1:
        pass


def enchanting_21186(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '暗强(3)')"
    if mode == 0:
        char.暗属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_21187(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '暗强(10)')"
    if mode == 0:
        char.暗属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_21188(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔攻(2)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=2 * rate)
    if mode == 1:
        pass


def enchanting_21189(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔攻(6)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=6 * rate)
    if mode == 1:
        pass


def enchanting_21190(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔攻(20)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21191(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(2)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=2 * rate)
    if mode == 1:
        pass


def enchanting_21192(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(6)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=6 * rate)
    if mode == 1:
        pass


def enchanting_21193(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物攻(20)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21194(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '火强(1)')"
    if mode == 0:
        char.火属性强化加成(1 * rate)
    if mode == 1:
        pass


def enchanting_21195(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '火强(3)')"
    if mode == 0:
        char.火属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_21196(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '火强(10)')"
    if mode == 0:
        char.火属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_21197(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '光强(1)')"
    if mode == 0:
        char.光属性强化加成(1 * rate)
    if mode == 1:
        pass


def enchanting_21198(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '光强(3)')"
    if mode == 0:
        char.光属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_21199(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '光强(10)')"
    if mode == 0:
        char.光属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_21200(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(3)')"
    if mode == 0:
        char.基础属性加成(智力=3 * rate)
    if mode == 1:
        pass


def enchanting_21201(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(12)')"
    if mode == 0:
        char.基础属性加成(智力=12 * rate)
    if mode == 1:
        pass


def enchanting_21202(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(30)')"
    if mode == 0:
        char.基础属性加成(智力=30 * rate)
    if mode == 1:
        pass


def enchanting_21203(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔暴(0.5%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.005 * rate)
    if mode == 1:
        pass


def enchanting_21204(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔暴(1%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.01 * rate)
    if mode == 1:
        pass


def enchanting_21205(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21206(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '精(3)')"
    if mode == 0:
        char.基础属性加成(精神=3 * rate)
    if mode == 1:
        pass


def enchanting_21207(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '精(12)')"
    if mode == 0:
        char.基础属性加成(精神=12 * rate)
    if mode == 1:
        pass


def enchanting_21208(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '精(30)')"
    if mode == 0:
        char.基础属性加成(精神=30 * rate)
    if mode == 1:
        pass


def enchanting_21209(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '移动速度(0.5%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.005 * rate)
    if mode == 1:
        pass


def enchanting_21210(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '移动速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_21211(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '移动速度(4.0%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21212(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(3)')"
    if mode == 0:
        char.基础属性加成(力量=3 * rate)
    if mode == 1:
        pass


def enchanting_21213(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(12)')"
    if mode == 0:
        char.基础属性加成(力量=12 * rate)
    if mode == 1:
        pass


def enchanting_21214(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(30)')"
    if mode == 0:
        char.基础属性加成(力量=30 * rate)
    if mode == 1:
        pass


def enchanting_21215(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(0.5%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.005 * rate)
    if mode == 1:
        pass


def enchanting_21216(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(1%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.01 * rate)
    if mode == 1:
        pass


def enchanting_21217(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '物暴(4%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21218(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体(3)')"
    if mode == 0:
        char.基础属性加成(体力=3 * rate)
    if mode == 1:
        pass


def enchanting_21219(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体(12)')"
    if mode == 0:
        char.基础属性加成(体力=12 * rate)
    if mode == 1:
        pass


def enchanting_21220(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '体(30)')"
    if mode == 0:
        char.基础属性加成(体力=30 * rate)
    if mode == 1:
        pass


def enchanting_21221(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '独立(4)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=4 * rate)
    if mode == 1:
        pass


def enchanting_21222(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '独立(10)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_21223(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '独立(35)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=35 * rate)
    if mode == 1:
        pass


def enchanting_21224(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '冰强(1)')"
    if mode == 0:
        char.冰属性强化加成(1 * rate)
    if mode == 1:
        pass


def enchanting_21225(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '冰强(3)')"
    if mode == 0:
        char.冰属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_21226(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '冰强(10)')"
    if mode == 0:
        char.冰属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_21227(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(14)')"
    if mode == 0:
        char.暗属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_21228(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '暗强(16)')"
    if mode == 0:
        char.暗属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_21229(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '暗强(17)')"
    if mode == 0:
        char.暗属性强化加成(17 * rate)
    if mode == 1:
        pass


def enchanting_21230(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '暗强(19)')"
    if mode == 0:
        char.暗属性强化加成(19 * rate)
    if mode == 1:
        pass


def enchanting_21231(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '暗强(20)|物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.暗属性强化加成(20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21232(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '火强(16)')"
    if mode == 0:
        char.火属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_21233(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '火强(17)')"
    if mode == 0:
        char.火属性强化加成(17 * rate)
    if mode == 1:
        pass


def enchanting_21234(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '火强(19)')"
    if mode == 0:
        char.火属性强化加成(19 * rate)
    if mode == 1:
        pass


def enchanting_21235(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '火强(20)|物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.火属性强化加成(20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21236(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '光强(16)')"
    if mode == 0:
        char.光属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_21237(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '光强(17)')"
    if mode == 0:
        char.光属性强化加成(17 * rate)
    if mode == 1:
        pass


def enchanting_21238(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '光强(20)|物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.光属性强化加成(20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21239(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '冰强(16)')"
    if mode == 0:
        char.冰属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_21240(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '冰强(17)')"
    if mode == 0:
        char.冰属性强化加成(17 * rate)
    if mode == 1:
        pass


def enchanting_21241(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '冰强(19)')"
    if mode == 0:
        char.冰属性强化加成(19 * rate)
    if mode == 1:
        pass


def enchanting_21242(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '冰强(20)|物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.冰属性强化加成(20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21243(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(7)')"
    if mode == 0:
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_21244(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 上衣, 下装', '魔攻(23)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=23 * rate)
    if mode == 1:
        pass


def enchanting_21245(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 鞋', '独立(44)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=44 * rate)
    if mode == 1:
        pass


def enchanting_21246(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 上衣, 下装', '物攻(23)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=23 * rate)
    if mode == 1:
        pass


def enchanting_21247(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '独立(30)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21248(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '独立(33)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=33 * rate)
    if mode == 1:
        pass


def enchanting_21249(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '独立(36)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=36 * rate)
    if mode == 1:
        pass


def enchanting_21250(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '独立(39)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=39 * rate)
    if mode == 1:
        pass


def enchanting_21251(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '独立(42)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=42 * rate)
    if mode == 1:
        pass


def enchanting_21252(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '独立(45)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=45 * rate)
    if mode == 1:
        pass


def enchanting_21253(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '物攻(4)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=4 * rate)
    if mode == 1:
        pass


def enchanting_21254(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '物攻(8)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=8 * rate)
    if mode == 1:
        pass


def enchanting_21255(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '物攻(12)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=12 * rate)
    if mode == 1:
        pass


def enchanting_21256(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '物攻(16)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=16 * rate)
    if mode == 1:
        pass


def enchanting_21257(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '物攻(22)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=22 * rate)
    if mode == 1:
        pass


def enchanting_21258(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '魔攻(4)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=4 * rate)
    if mode == 1:
        pass


def enchanting_21259(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '魔攻(8)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=8 * rate)
    if mode == 1:
        pass


def enchanting_21260(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '魔攻(12)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=12 * rate)
    if mode == 1:
        pass


def enchanting_21261(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '魔攻(16)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=16 * rate)
    if mode == 1:
        pass


def enchanting_21262(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '上衣', '魔攻(22)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=22 * rate)
    if mode == 1:
        pass


def enchanting_21263(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '魔攻(20)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21264(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '物攻(20)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21265(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '智(40)')"
    if mode == 0:
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_21266(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器', '力(40)')"
    if mode == 0:
        char.基础属性加成(力量=40 * rate)
    if mode == 1:
        pass


def enchanting_21267(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '魔攻(28)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=28 * rate)
    if mode == 1:
        pass


def enchanting_21268(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '魔攻(29)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=29 * rate)
    if mode == 1:
        pass


def enchanting_21269(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '魔攻(31)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=31 * rate)
    if mode == 1:
        pass


def enchanting_21270(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '魔攻(32)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=32 * rate)
    if mode == 1:
        pass


def enchanting_21271(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '魔攻(33)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=33 * rate)
    if mode == 1:
        pass


def enchanting_21272(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '独立(43)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=43 * rate)
    if mode == 1:
        pass


def enchanting_21273(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '独立(44)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=44 * rate)
    if mode == 1:
        pass


def enchanting_21274(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '独立(46)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=46 * rate)
    if mode == 1:
        pass


def enchanting_21275(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '物攻(28)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=28 * rate)
    if mode == 1:
        pass


def enchanting_21276(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '物攻(29)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=29 * rate)
    if mode == 1:
        pass


def enchanting_21277(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '物攻(31)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=31 * rate)
    if mode == 1:
        pass


def enchanting_21278(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '物攻(32)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=32 * rate)
    if mode == 1:
        pass


def enchanting_21279(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器, 上衣, 下装', '物攻(33)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=33 * rate)
    if mode == 1:
        pass


def enchanting_21280(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 下装, 腰带', '物攻(10)|独立(15)|力(25)|物暴(1%)|攻击速度(0.5%)|施放速度(0.5%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=10 * rate)
        char.基础属性加成(独立攻击力=15 * rate)
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(物理暴击率=0.01 * rate)
        char.基础属性加成(攻击速度=0.005 * rate)
        char.基础属性加成(施放速度=0.005 * rate)
    if mode == 1:
        pass


def enchanting_21281(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '力(25)')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
    if mode == 1:
        pass


def enchanting_21282(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '力(15)')"
    if mode == 0:
        char.基础属性加成(力量=15 * rate)
    if mode == 1:
        pass


def enchanting_21283(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '智(25)')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
    if mode == 1:
        pass


def enchanting_21284(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '智(15)')"
    if mode == 0:
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_21285(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '体(20)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
    if mode == 1:
        pass


def enchanting_21286(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '体(15)')"
    if mode == 0:
        char.基础属性加成(体力=15 * rate)
    if mode == 1:
        pass


def enchanting_21287(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '精(20)')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
    if mode == 1:
        pass


def enchanting_21288(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '精(15)')"
    if mode == 0:
        char.基础属性加成(精神=15 * rate)
    if mode == 1:
        pass


def enchanting_21289(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '物攻(16)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=16 * rate)
    if mode == 1:
        pass


def enchanting_21290(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '魔攻(16)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=16 * rate)
    if mode == 1:
        pass


def enchanting_21291(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '物暴(6%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_21292(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '物暴(4%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21293(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '魔暴(6%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_21294(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21295(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '物攻(15)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_21296(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '魔攻(15)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_21297(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备, 魔法石', '独立(15)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_21298(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备, 魔法石', '独立(20)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21299(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(11)|暗强(11)')"
    if mode == 0:
        char.光属性强化加成(11 * rate)
        char.暗属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_21300(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(11)|冰强(11)')"
    if mode == 0:
        char.火属性强化加成(11 * rate)
        char.冰属性强化加成(11 * rate)
    if mode == 1:
        pass


def enchanting_21301(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '力智(15)')"
    if mode == 0:
        char.基础属性加成(力智=15 * rate)
    if mode == 1:
        pass


def enchanting_21302(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '火强(20)')"
    if mode == 0:
        char.火属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_21303(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '属性攻击(火)|物攻(20)|魔攻(20)|攻击速度(3.0%)|施放速度(3.0%)')"
    if mode == 0:
        char.属性攻击('火')
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(攻击速度=0.03 * rate)
        char.基础属性加成(施放速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21304(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力智(50)|物攻(35)|魔攻(35)')"
    if mode == 0:
        char.基础属性加成(力智=50 * rate)
        char.基础属性加成(物理攻击力=35 * rate)
        char.基础属性加成(魔法攻击力=35 * rate)
    if mode == 1:
        pass


def enchanting_21305(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '物攻(40)|攻击速度(3.0%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=40 * rate)
        char.基础属性加成(攻击速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21306(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '暗强(20)')"
    if mode == 0:
        char.暗属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_21307(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '冰强(20)')"
    if mode == 0:
        char.冰属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_21308(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '属性攻击(冰)|物攻(20)|魔攻(20)|攻击速度(3.0%)|施放速度(3.0%)')"
    if mode == 0:
        char.属性攻击('冰')
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(攻击速度=0.03 * rate)
        char.基础属性加成(施放速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21309(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '属性攻击(光)|物攻(20)|魔攻(20)|攻击速度(3.0%)|施放速度(3.0%)')"
    if mode == 0:
        char.属性攻击('光')
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(攻击速度=0.03 * rate)
        char.基础属性加成(施放速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21310(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '光强(20)')"
    if mode == 0:
        char.光属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_21311(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '武器', '魔攻(40)|施放速度(5.0%)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=40 * rate)
        char.基础属性加成(施放速度=0.05 * rate)
    if mode == 1:
        pass


def enchanting_21312(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '属性攻击(暗)|物攻(20)|魔攻(20)|攻击速度(3.0%)|施放速度(3.0%)')"
    if mode == 0:
        char.属性攻击('暗')
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(攻击速度=0.03 * rate)
        char.基础属性加成(施放速度=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21313(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '魔攻(26)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=26 * rate)
    if mode == 1:
        pass


def enchanting_21314(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '魔攻(27)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=27 * rate)
    if mode == 1:
        pass


def enchanting_21315(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '物攻(16)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=16 * rate)
    if mode == 1:
        pass


def enchanting_21316(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '独立(23)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=23 * rate)
    if mode == 1:
        pass


def enchanting_21317(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '魔攻(12)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=12 * rate)
    if mode == 1:
        pass


def enchanting_21318(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(37)')"
    if mode == 0:
        char.基础属性加成(智力=37 * rate)
    if mode == 1:
        pass


def enchanting_21319(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '施放速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_21320(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '所有属性抗性(8)')"
    if mode == 0:
        char.所有属性抗性加成(8 * rate)
    if mode == 1:
        pass


def enchanting_21321(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '所有属性抗性(9)')"
    if mode == 0:
        char.所有属性抗性加成(9 * rate)
    if mode == 1:
        pass


def enchanting_21322(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '所有属性抗性(10)')"
    if mode == 0:
        char.所有属性抗性加成(10 * rate)
    if mode == 1:
        pass


def enchanting_21323(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(8)')"
    if mode == 0:
        char.基础属性加成(精神=8 * rate)
    if mode == 1:
        pass


def enchanting_21324(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(9)')"
    if mode == 0:
        char.基础属性加成(精神=9 * rate)
    if mode == 1:
        pass


def enchanting_21325(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(10)')"
    if mode == 0:
        char.基础属性加成(精神=10 * rate)
    if mode == 1:
        pass


def enchanting_21326(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(11)')"
    if mode == 0:
        char.基础属性加成(精神=11 * rate)
    if mode == 1:
        pass


def enchanting_21327(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(12)')"
    if mode == 0:
        char.基础属性加成(精神=12 * rate)
    if mode == 1:
        pass


def enchanting_21328(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(13)')"
    if mode == 0:
        char.基础属性加成(精神=13 * rate)
    if mode == 1:
        pass


def enchanting_21329(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(14)')"
    if mode == 0:
        char.基础属性加成(精神=14 * rate)
    if mode == 1:
        pass


def enchanting_21330(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '项链, 手镯, 戒指', '独立(30)|火强(5)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.火属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_21331(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火抗(11)')"
    if mode == 0:
        char.火属性抗性加成(11 * rate)
    if mode == 1:
        pass


def enchanting_21332(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '头肩', '物暴(3%)|魔暴(4%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_21333(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(3)')"
    if mode == 0:
        char.火属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_21334(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(4)')"
    if mode == 0:
        char.火属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_21335(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(5)')"
    if mode == 0:
        char.火属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_21336(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(20)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_21337(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(21)')"
    if mode == 0:
        char.基础属性加成(智力=21 * rate)
    if mode == 1:
        pass


def enchanting_21338(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(22)')"
    if mode == 0:
        char.基础属性加成(智力=22 * rate)
    if mode == 1:
        pass


def enchanting_21339(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(23)')"
    if mode == 0:
        char.基础属性加成(智力=23 * rate)
    if mode == 1:
        pass


def enchanting_21340(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(24)')"
    if mode == 0:
        char.基础属性加成(智力=24 * rate)
    if mode == 1:
        pass


def enchanting_21341(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(15)')"
    if mode == 0:
        char.基础属性加成(体力=15 * rate)
    if mode == 1:
        pass


def enchanting_21342(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(17)')"
    if mode == 0:
        char.基础属性加成(体力=17 * rate)
    if mode == 1:
        pass


def enchanting_21343(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(18)')"
    if mode == 0:
        char.基础属性加成(体力=18 * rate)
    if mode == 1:
        pass


def enchanting_21344(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(19)')"
    if mode == 0:
        char.基础属性加成(体力=19 * rate)
    if mode == 1:
        pass


def enchanting_21345(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(20)')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
    if mode == 1:
        pass


def enchanting_21346(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(21)')"
    if mode == 0:
        char.基础属性加成(体力=21 * rate)
    if mode == 1:
        pass


def enchanting_21347(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(22)')"
    if mode == 0:
        char.基础属性加成(体力=22 * rate)
    if mode == 1:
        pass


def enchanting_21348(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(2.1%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.021 * rate)
    if mode == 1:
        pass


def enchanting_21349(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(2.2%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.022 * rate)
    if mode == 1:
        pass


def enchanting_21350(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(2.3%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.023 * rate)
    if mode == 1:
        pass


def enchanting_21351(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(2.4%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.024 * rate)
    if mode == 1:
        pass


def enchanting_21352(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(2.5%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.025 * rate)
    if mode == 1:
        pass


def enchanting_21353(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(2.6%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.026 * rate)
    if mode == 1:
        pass


def enchanting_21354(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(2.7%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.027 * rate)
    if mode == 1:
        pass


def enchanting_21355(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链', '火抗(3)')"
    if mode == 0:
        char.火属性抗性加成(3 * rate)
    if mode == 1:
        pass


def enchanting_21356(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(10)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_21357(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(11)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=11 * rate)
    if mode == 1:
        pass


def enchanting_21358(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(12)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=12 * rate)
    if mode == 1:
        pass


def enchanting_21359(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(13)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=13 * rate)
    if mode == 1:
        pass


def enchanting_21360(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(1.2%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.012 * rate)
    if mode == 1:
        pass


def enchanting_21361(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(1.3%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.013 * rate)
    if mode == 1:
        pass


def enchanting_21362(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(1.4%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.014 * rate)
    if mode == 1:
        pass


def enchanting_21363(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '体精(8)')"
    if mode == 0:
        char.基础属性加成(体精=8 * rate)
    if mode == 1:
        pass


def enchanting_21364(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '力智(10)')"
    if mode == 0:
        char.基础属性加成(力智=10 * rate)
    if mode == 1:
        pass


def enchanting_21365(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '头肩, 腰带, 鞋', '力智(20)')"
    if mode == 0:
        char.基础属性加成(力智=20 * rate)
    if mode == 1:
        pass


def enchanting_21366(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '力智(15)')"
    if mode == 0:
        char.基础属性加成(力智=15 * rate)
    if mode == 1:
        pass


def enchanting_21367(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(15)')"
    if mode == 0:
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_21368(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(16)')"
    if mode == 0:
        char.基础属性加成(智力=16 * rate)
    if mode == 1:
        pass


def enchanting_21369(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(17)')"
    if mode == 0:
        char.基础属性加成(智力=17 * rate)
    if mode == 1:
        pass


def enchanting_21370(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(19)')"
    if mode == 0:
        char.基础属性加成(智力=19 * rate)
    if mode == 1:
        pass


def enchanting_21371(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '物攻(15)|魔攻(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21372(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣', '智(65)')"
    if mode == 0:
        char.基础属性加成(智力=65 * rate)
    if mode == 1:
        pass


def enchanting_21373(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '属性攻击(暗)|物攻(20)')"
    if mode == 0:
        char.属性攻击('暗')
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21374(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '魔攻(16)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=16 * rate)
    if mode == 1:
        pass


def enchanting_21375(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(31)')"
    if mode == 0:
        char.基础属性加成(体力=31 * rate)
    if mode == 1:
        pass


def enchanting_21376(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(33)')"
    if mode == 0:
        char.基础属性加成(体力=33 * rate)
    if mode == 1:
        pass


def enchanting_21377(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(3)')"
    if mode == 0:
        char.冰属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_21378(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(4)')"
    if mode == 0:
        char.冰属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_21379(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '冰强(5)')"
    if mode == 0:
        char.冰属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_21380(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(31)')"
    if mode == 0:
        char.基础属性加成(力量=31 * rate)
    if mode == 1:
        pass


def enchanting_21381(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '鞋', '力(2)|移动速度(0.2%)')"
    if mode == 0:
        char.基础属性加成(力量=2 * rate)
        char.基础属性加成(移动速度=0.002 * rate)
    if mode == 1:
        pass


def enchanting_21382(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '力智(30)')"
    if mode == 0:
        char.基础属性加成(力智=30 * rate)
    if mode == 1:
        pass


def enchanting_21383(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(31)')"
    if mode == 0:
        char.基础属性加成(智力=31 * rate)
    if mode == 1:
        pass


def enchanting_21384(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '智(33)')"
    if mode == 0:
        char.基础属性加成(智力=33 * rate)
    if mode == 1:
        pass


def enchanting_21385(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '物攻(26)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=26 * rate)
    if mode == 1:
        pass


def enchanting_21386(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '物攻(27)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=27 * rate)
    if mode == 1:
        pass


def enchanting_21387(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(23)')"
    if mode == 0:
        char.基础属性加成(体力=23 * rate)
    if mode == 1:
        pass


def enchanting_21388(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(24)')"
    if mode == 0:
        char.基础属性加成(体力=24 * rate)
    if mode == 1:
        pass


def enchanting_21389(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '下装', '移动速度(0.3%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.003 * rate)
    if mode == 1:
        pass


def enchanting_21390(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '项链, 手镯, 戒指', '独立(40)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_21391(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(14)')"
    if mode == 0:
        char.基础属性加成(体力=14 * rate)
    if mode == 1:
        pass


def enchanting_21392(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(46)')"
    if mode == 0:
        char.基础属性加成(智力=46 * rate)
    if mode == 1:
        pass


def enchanting_21393(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(47)')"
    if mode == 0:
        char.基础属性加成(智力=47 * rate)
    if mode == 1:
        pass


def enchanting_21394(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(48)')"
    if mode == 0:
        char.基础属性加成(智力=48 * rate)
    if mode == 1:
        pass


def enchanting_21395(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '武器, 上衣, 下装', '智(49)')"
    if mode == 0:
        char.基础属性加成(智力=49 * rate)
    if mode == 1:
        pass


def enchanting_21396(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(2.8%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.028 * rate)
    if mode == 1:
        pass


def enchanting_21397(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(1.5%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.015 * rate)
    if mode == 1:
        pass


def enchanting_21398(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(1.6%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.016 * rate)
    if mode == 1:
        pass


def enchanting_21399(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(1.7%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.017 * rate)
    if mode == 1:
        pass


def enchanting_21400(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(1.8%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.018 * rate)
    if mode == 1:
        pass


def enchanting_21401(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(1.9%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.019 * rate)
    if mode == 1:
        pass


def enchanting_21402(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '施放速度(1.5%)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.015 * rate)
    if mode == 1:
        pass


def enchanting_21403(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(8)')"
    if mode == 0:
        char.基础属性加成(体力=8 * rate)
    if mode == 1:
        pass


def enchanting_21404(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(9)')"
    if mode == 0:
        char.基础属性加成(体力=9 * rate)
    if mode == 1:
        pass


def enchanting_21405(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(11)')"
    if mode == 0:
        char.基础属性加成(体力=11 * rate)
    if mode == 1:
        pass


def enchanting_21406(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(12)')"
    if mode == 0:
        char.基础属性加成(体力=12 * rate)
    if mode == 1:
        pass


def enchanting_21407(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(13)')"
    if mode == 0:
        char.基础属性加成(体力=13 * rate)
    if mode == 1:
        pass


def enchanting_21408(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '四维(20)')"
    if mode == 0:
        char.基础属性加成(四维=20 * rate)
    if mode == 1:
        pass


def enchanting_21409(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(4)')"
    if mode == 0:
        char.所有属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_21410(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '所有属性强化(6)')"
    if mode == 0:
        char.所有属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_21411(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力智(20)')"
    if mode == 0:
        char.基础属性加成(力智=20 * rate)
    if mode == 1:
        pass


def enchanting_21412(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩', '物暴(1%)|魔暴(0.5%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.01 * rate)
        char.基础属性加成(魔法暴击率=0.005 * rate)
    if mode == 1:
        pass


def enchanting_21413(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '攻击速度(0.5%)|施放速度(0.5%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.005 * rate)
        char.基础属性加成(施放速度=0.005 * rate)
    if mode == 1:
        pass


def enchanting_21414(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '攻击速度(1.5%)|施放速度(1.5%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.015 * rate)
        char.基础属性加成(施放速度=0.015 * rate)
    if mode == 1:
        pass


def enchanting_21415(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '攻击速度(1.0%)|施放速度(1.0%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.01 * rate)
        char.基础属性加成(施放速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_21416(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '精(22)')"
    if mode == 0:
        char.基础属性加成(精神=22 * rate)
    if mode == 1:
        pass


def enchanting_21417(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '暗强(9)|独立(10)')"
    if mode == 0:
        char.暗属性强化加成(9 * rate)
        char.基础属性加成(独立攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_21418(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '鞋', '智(2)|移动速度(0.2%)')"
    if mode == 0:
        char.基础属性加成(智力=2 * rate)
        char.基础属性加成(移动速度=0.002 * rate)
    if mode == 1:
        pass


def enchanting_21419(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(23)')"
    if mode == 0:
        char.基础属性加成(力量=23 * rate)
    if mode == 1:
        pass


def enchanting_21420(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器, 上衣, 下装', '力(24)')"
    if mode == 0:
        char.基础属性加成(力量=24 * rate)
    if mode == 1:
        pass


def enchanting_21421(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '物攻(12)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=12 * rate)
    if mode == 1:
        pass


def enchanting_21422(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '武器', '攻击速度(0.6%)|施放速度(1.2%)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.006 * rate)
        char.基础属性加成(施放速度=0.012 * rate)
    if mode == 1:
        pass


def enchanting_21423(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(93, '称号', '物攻(7)|魔攻(7)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=7 * rate)
        char.基础属性加成(魔法攻击力=7 * rate)
    if mode == 1:
        pass


def enchanting_21424(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(26)')"
    if mode == 0:
        char.基础属性加成(体力=26 * rate)
    if mode == 1:
        pass


def enchanting_21425(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(27)')"
    if mode == 0:
        char.基础属性加成(体力=27 * rate)
    if mode == 1:
        pass


def enchanting_21426(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(28)')"
    if mode == 0:
        char.基础属性加成(体力=28 * rate)
    if mode == 1:
        pass


def enchanting_21427(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '头肩, 腰带, 鞋', '体(29)')"
    if mode == 0:
        char.基础属性加成(体力=29 * rate)
    if mode == 1:
        pass


def enchanting_21428(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣, 下装, 头肩, 腰带, 鞋', '物攻(20)|物暴(3%)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21429(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣, 下装, 头肩, 腰带, 鞋', '魔攻(20)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21430(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '上衣, 下装, 头肩, 腰带, 鞋', '独立(30)|物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21431(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '火强(10)|暗强(10)')"
    if mode == 0:
        char.火属性强化加成(10 * rate)
        char.暗属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_21432(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '项链, 手镯, 戒指', '光强(10)|冰强(10)')"
    if mode == 0:
        char.光属性强化加成(10 * rate)
        char.冰属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_21433(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备, 魔法石', '物攻(15)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_21434(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备, 魔法石', '魔攻(15)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_21435(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备, 魔法石', '独立(20)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_21436(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '头肩', '四维(75)|物暴(5%)|魔暴(5%)|Lv1~30主动+1')"
    if mode == 0:
        char.基础属性加成(四维=75 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 30, 1)
    if mode == 1:
        pass


def enchanting_21437(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '称号', '所有属性强化(15)|物攻(20)|魔攻(20)|独立(30)|Lv1~50主动+1')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_21438(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '辅助装备', '物攻(20)|魔攻(20)|独立(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21439(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '上衣, 下装', '物攻(28)|独立(30)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=28 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21440(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(69, '上衣, 下装', '魔攻(28)|独立(30)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=28 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_21441(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '物暴(7%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_21442(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '魔暴(7%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_21443(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '称号', '所有属性强化(5)')"
    if mode == 0:
        char.所有属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_21444(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(40)')"
    if mode == 0:
        char.基础属性加成(力量=40 * rate)
    if mode == 1:
        pass


def enchanting_21445(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力智(20)')"
    if mode == 0:
        char.基础属性加成(力智=20 * rate)
    if mode == 1:
        pass


def enchanting_21446(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(20)|体(20)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(体力=20 * rate)
    if mode == 1:
        pass


def enchanting_21447(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(20)|精(20)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(精神=20 * rate)
    if mode == 1:
        pass


def enchanting_21448(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(20)|物攻(15)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_21449(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(20)|魔攻(15)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_21450(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(20)|独立(25)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_21451(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(20)|物暴(3%)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21452(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '力(20)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21453(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(20)|火强(7)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_21454(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(20)|冰强(7)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_21455(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(20)|暗强(7)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_21456(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '力(20)|光强(7)')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_21457(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(40)')"
    if mode == 0:
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_21458(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(20)|体(20)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(体力=20 * rate)
    if mode == 1:
        pass


def enchanting_21459(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(20)|精(20)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(精神=20 * rate)
    if mode == 1:
        pass


def enchanting_21460(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(20)|物攻(15)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_21461(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(20)|魔攻(15)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_21462(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '智(20)|独立(25)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_21463(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '智(20)|物暴(3%)')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21464(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '所有属性强化(14)')"
    if mode == 0:
        char.所有属性强化加成(14*rate)
    if mode == 1:
        pass

def enchanting_21490(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '物暴(6%)|魔暴(6%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_21491(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(86, '腰带', '物暴(3%)|魔暴(3%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_21492(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带', '物暴(6%)|魔暴(6%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_21493(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(56, '鞋', '移动速度(2.5%)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.025 * rate)
    if mode == 1:
        pass




#  国服特色


def enchanting_23001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带，鞋', '三攻(36)|技攻(3%)')"
    if mode == 0:
        char.基础属性加成(三攻=36 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_23002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带，鞋', '三攻(36)|Lv1~50主动+1')"
    if mode == 0:
        char.基础属性加成(三攻=36 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_23003(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '所有属性强化(33)')"
    if mode == 0:
        char.所有属性强化加成(33 * rate)
    if mode == 1:
        pass


def enchanting_23004(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '冰强(35)|暗强(35)')"
    if mode == 0:
        char.冰属性强化加成(35 * rate)
        char.暗属性强化加成(35 * rate)
    if mode == 1:
        pass


def enchanting_23005(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '火强(35)|光强(35)')"
    if mode == 0:
        char.火属性强化加成(35 * rate)
        char.光属性强化加成(35 * rate)
    if mode == 1:
        pass


def enchanting_23006(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '辅助装备', '所有属性强化(12)|物暴(3%)|魔暴(3%)|最终伤害(3%)|攻击强化(3%)')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
        char.最终伤害加成(0.03 * rate)
        char.百分比攻击强化加成(0.03 * rate)
        char.暴击率增加(0.03)
    if mode == 1:
        pass


def enchanting_23007(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(158, '魔法石', '所有属性强化(30)')"
    if mode == 0:
        char.所有属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_23008(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '力智(75)|三攻(20)|技攻(3%)')"
    if mode == 0:
        char.三攻固定加成(20 * rate)
        char.力智固定加成(75 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_23009(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '力智(75)|三攻(20)|Lv1~50主动+1')"
    if mode == 0:
        char.三攻固定加成(20 * rate)
        char.力智固定加成(75 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


# endregion

# region 光环 24001~24099


def enchanting_24001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1|三攻(5%)')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.百分比三攻加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass


def enchanting_24002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1|黄字(5%)')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.伤害增加加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass


def enchanting_24003(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1|暴伤(5%)')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.暴击伤害加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass
# endregion

# region 武器装扮 24101~24199


def enchanting_24101(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '四维(55)|Lv40+1')"
    if mode == 0:
        char.武器装扮等级加成(40, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_24102(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '四维(55)|Lv45+1')"
    if mode == 0:
        char.武器装扮等级加成(45, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_24103(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '四维(55)|Lv60+1')"
    if mode == 0:
        char.武器装扮等级加成(60, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_24104(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '四维(55)|Lv70+1')"
    if mode == 0:
        char.武器装扮等级加成(70, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_24105(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '四维(55)|Lv75+1')"
    if mode == 0:
        char.武器装扮等级加成(75, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_24106(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '四维(55)|Lv80+1')"
    if mode == 0:
        char.武器装扮等级加成(80, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass

# endregion

# region 皮肤 24201~24299


def enchanting_24201(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '皮肤', '所有属性强化(5)')"
    if mode == 0:
        char.所有属性强化加成(5)
        pass
    if mode == 1:
        pass


def enchanting_24202(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '皮肤', '所有属性强化(6)')"
    if mode == 0:
        char.所有属性强化加成(6)
        pass
    if mode == 1:
        pass

# endregion

# region 宠物装备-红 24301~24399


def enchanting_24301(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '百分比三攻(8%)|攻击强化(8%)')"
    if mode == 0:
        char.百分比三攻加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass


def enchanting_24302(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '百分比力智(8%)|攻击强化(8%)')"
    if mode == 0:
        char.百分比力智加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass


def enchanting_24303(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '最终伤害(8%)|攻击强化(8%)')"
    if mode == 0:
        char.最终伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass


def enchanting_24304(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '附加伤害(8%)|攻击强化(8%)')"
    if mode == 0:
        char.附加伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass
# endregion

# region 宠物装备-绿 24401~24499


def enchanting_24401(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-绿', '三攻(40)|所有属性强化(20)')"
    if mode == 0:
        char.三攻固定加成(40)
        char.所有属性强化加成(20)
        pass
    if mode == 1:
        pass

# endregion

# region 宠物装备-蓝 24501~24599


def enchanting_24501(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-蓝', '三攻(30)')"
    if mode == 0:
        char.三攻固定加成(30)
        pass
    if mode == 1:
        pass

# endregion

# region 快捷装备 24601~24699


def enchanting_24601(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '快捷装备', '三攻(40)|附加伤害(8%)|攻击强化(8%)')"
    if mode == 0:
        pass
    if mode == 1:
        char.三攻固定加成(30)
        char.附加伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass


def enchanting_24602(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '快捷装备', '四维(8)|附加伤害(8%)|攻击强化(8%)')"
    if mode == 0:
        char.力智固定加成(8)
        char.体精固定加成(8)
        pass
    if mode == 1:
        char.附加伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass


# endregion


# 附魔效果id范围 20001~24999
for i in range(20000, 24999):
    try:
        if i not in enchanting_func_list.keys():
            enchanting_func_list[i] = eval('enchanting_{}'.format(i))
    except:
        pass


def get_encfunc_by_id(id):
    return enchanting_func_list.get(id, enchanting_20000)


def get_enchanting_setinfo():
    infolist = []
    for i in enchanting_func_list.keys():
        data = {}
        data['id'] = i
        info = eval(enchanting_func_list[i](text=True))
        num = 0
        for k in index:
            data[k] = info[num]
            num += 1
        infolist.append(data)
    return infolist
