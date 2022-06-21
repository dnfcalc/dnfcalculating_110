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
        return "(107, '称号', '火属性强化 +4')"
    if mode == 0:
        char.火属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '火属性强化 +5')"
    if mode == 0:
        char.火属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20003(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '火属性强化 +6')"
    if mode == 0:
        char.火属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20004(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '冰属性强化 +4')"
    if mode == 0:
        char.冰属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20005(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '冰属性强化 +5')"
    if mode == 0:
        char.冰属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20006(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '冰属性强化 +6')"
    if mode == 0:
        char.冰属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20007(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '暗属性强化 +4')"
    if mode == 0:
        char.暗属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20008(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '暗属性强化 +5')"
    if mode == 0:
        char.暗属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20009(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '暗属性强化 +6')"
    if mode == 0:
        char.暗属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20010(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '光属性强化 +4')"
    if mode == 0:
        char.光属性强化加成(4 * rate)
    if mode == 1:
        pass


def enchanting_20011(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '光属性强化 +5')"
    if mode == 0:
        char.光属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20012(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '光属性强化 +6')"
    if mode == 0:
        char.光属性强化加成(6 * rate)
    if mode == 1:
        pass


def enchanting_20013(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '炽炎之艾格尼丝')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20014(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '征集令支援宝珠 (物理暴击率5%)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20015(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '征集令支援宝珠 (魔法暴击率5%)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20016(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '库尔图洛·玛努斯[暴击 + 7%]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.07 * rate)
        char.基础属性加成(魔法暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20017(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '库尔图洛·玛努斯 Mark-II[暴击 + 8%]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.08 * rate)
        char.基础属性加成(魔法暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20018(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '[活动]小女儿斯库尔[魔法暴击 + 6%]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20019(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '穿靴子的玛尔切拉[物理暴击 + 6%]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20020(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '耳环', '新手冒险家宝珠[四维 + 125]')"
    if mode == 0:
        char.基础属性加成(力量=125 * rate)
        char.基础属性加成(智力=125 * rate)
        char.基础属性加成(体力=125 * rate)
        char.基础属性加成(精神=125 * rate)
    if mode == 1:
        pass


def enchanting_20021(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '万圣节黑色宝珠[体力 + 45]')"
    if mode == 0:
        char.基础属性加成(体力=45 * rate)
    if mode == 1:
        pass


def enchanting_20022(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '万圣节白色宝珠[精神 + 45]')"
    if mode == 0:
        char.基础属性加成(精神=45 * rate)
    if mode == 1:
        pass


def enchanting_20023(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '[活动]乌恩·莱奥尼尔的宝珠 (黄色)[物理暴击 + 5%]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20024(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '[活动]乌恩·莱奥尼尔的宝珠 (绿色)[魔法暴击 + 5%]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20025(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '[积分商城]魔剑士瑟尔莫[独立 + 50 力量 + 20]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20026(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '狂热者迪欧尔贝[魔法暴击 + 10%]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20027(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '灵魂饲养员蒙德格林[力量 + 75]')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
    if mode == 1:
        pass


def enchanting_20028(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '银光妲可儿[物理暴击 + 10%]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20029(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '圣光之思维宝珠[精神 + 75]')"
    if mode == 0:
        char.基础属性加成(精神=75 * rate)
    if mode == 1:
        pass


def enchanting_20030(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '[积分商城]碎心者里查德[独立 + 50 智力 + 20]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20031(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '[积分商城]皎玉之哈尔巴特[物攻 + 50 力量 + 20]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20032(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '无尽的知识宝珠[智力 + 75]')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20033(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '[积分商城]被囚禁的开普洛斯[魔攻 + 50 智力 + 20]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20034(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '囚徒之麦克罗里[魔法暴击 + 7%]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20035(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '圣光之坚守宝珠[体力 + 75]')"
    if mode == 0:
        char.基础属性加成(体力=75 * rate)
    if mode == 1:
        pass


def enchanting_20036(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '血剑比拉多[物理暴击 + 7%]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20037(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '超越之行星 - 罗什[全属 + 23]')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20038(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '寒冰之行星 - 罗什[冰/光 + 25]')"
    if mode == 0:
        char.冰属性强化加成(25 * rate)
        char.光属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20039(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '火焰之行星 - 罗什[火/暗 + 25]')"
    if mode == 0:
        char.火属性强化加成(25 * rate)
        char.暗属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20040(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '阿拉德智慧之海宝珠[智力 + 75]')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20042(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '魂·异界比特·伯斯提')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20045(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '夜市火珠')"
    if mode == 0:
        char.火属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20046(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '夜市冰珠')"
    if mode == 0:
        char.冰属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20047(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '夜市光珠')"
    if mode == 0:
        char.光属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20048(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '夜市暗珠')"
    if mode == 0:
        char.暗属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20049(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '所有属性强化 +23')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20050(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '[体/精 + 35 力/智 + 40]')"
    if mode == 0:
        char.基础属性加成(智力=40 * rate)
        char.基础属性加成(力量=40 * rate)
        char.基础属性加成(精神=35 * rate)
        char.基础属性加成(体力=35 * rate)
    if mode == 1:
        pass


def enchanting_20051(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '耳环', '魂·异界真龙利特雷诺')"
    if mode == 0:
        char.基础属性加成(力量=150 * rate)
        char.基础属性加成(智力=150 * rate)
        char.基础属性加成(体力=150 * rate)
        char.基础属性加成(精神=150 * rate)
    if mode == 1:
        pass


def enchanting_20052(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '被蚕食的碎心者里查德 ')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20053(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '触犯禁忌的白锈之希斯林 ')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20054(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '铎黑德 ')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20055(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '银白妲可儿 ')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20056(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '残暴之沃兹沃斯 ')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20057(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '魔剑巴吉罗·改 ')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
    if mode == 1:
        pass


def enchanting_20058(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '耳环', '回归冒险家耳环宝珠')"
    if mode == 0:
        char.基础属性加成(力量=125 * rate)
        char.基础属性加成(智力=125 * rate)
        char.基础属性加成(体力=125 * rate)
        char.基础属性加成(精神=125 * rate)
    if mode == 1:
        pass


def enchanting_20059(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '回归冒险家魔法石宝珠 (强攻)')"
    if mode == 0:
        char.所有属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20060(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '回归冒险家魔法石宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20061(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '回归冒险家辅助装备宝珠 (强攻)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=70 * rate)
        char.基础属性加成(魔法攻击力=70 * rate)
        char.基础属性加成(独立攻击力=70 * rate)
    if mode == 1:
        pass


def enchanting_20062(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '回归冒险家辅助装备宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=80 * rate)
        char.基础属性加成(智力=80 * rate)
        char.基础属性加成(体力=80 * rate)
        char.基础属性加成(精神=80 * rate)
    if mode == 1:
        pass


def enchanting_20067(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '回归冒险家首饰宝珠 (强攻)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20068(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '回归冒险家首饰宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=42 * rate)
        char.基础属性加成(智力=42 * rate)
        char.基础属性加成(体力=38 * rate)
        char.基础属性加成(精神=38 * rate)
    if mode == 1:
        pass


def enchanting_20072(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '强攻型冒险宝珠 (头肩/腰带/鞋子)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass

def enchanting_20078(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '魂·异界首饰宝珠 (冰/暗属性强化)')"
    if mode == 0:
        char.冰属性强化加成(30 * rate)
        char.暗属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20079(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '魂·异界首饰宝珠 (火/光属性强化)')"
    if mode == 0:
        char.火属性强化加成(30 * rate)
        char.光属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20080(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '仲夏夜梦宝珠 [所有四维]')"
    if mode == 0:
        char.基础属性加成(力量=70 * rate)
        char.基础属性加成(智力=70 * rate)
        char.基础属性加成(体力=70 * rate)
        char.基础属性加成(精神=70 * rate)
    if mode == 1:
        pass


def enchanting_20081(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '祭司长阿拉克 ')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(独立攻击力=50 * rate)
    if mode == 1:
        pass


def enchanting_20082(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '力量、 智力 +65')"
    if mode == 0:
        char.基础属性加成(力量=70 * rate)
        char.基础属性加成(智力=70 * rate)
    if mode == 1:
        pass


def enchanting_20083(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '次元术士拉齐亚 ')"
    if mode == 0:
        char.所有属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20084(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '体力、 精神 +65')"
    if mode == 0:
        char.基础属性加成(体力=70 * rate)
        char.基础属性加成(精神=70 * rate)
    if mode == 1:
        pass


def enchanting_20085(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '雪之华曼达林 ')"
    if mode == 0:
        char.光属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20086(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '愚者锡德尔 ')"
    if mode == 0:
        char.火属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20087(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '领悟者乌佐 ')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20088(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '被卡赞附身的罗森伯格 ')"
    if mode == 0:
        char.暗属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20089(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '灵媒埃里克 ')"
    if mode == 0:
        char.冰属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20090(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '灰血之手罗森伯格 ')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20091(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '毒王路易斯 ')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20092(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '青面修罗洛兹贝伦 ')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20093(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '伪装者血腥里娅 ')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
    if mode == 1:
        pass


def enchanting_20094(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '伪装者尼罗罗特 ')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20095(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '特里亚·赛鲁姆 ')"
    if mode == 0:
        char.基础属性加成(体力=75 * rate)
    if mode == 1:
        pass


def enchanting_20096(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '烈焰蜘蛛 ')"
    if mode == 0:
        char.基础属性加成(精神=75 * rate)
    if mode == 1:
        pass


def enchanting_20097(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '记忆印痕刀疤鼠 ')"
    if mode == 0:
        char.基础属性加成(物理攻击力=60 * rate)
        char.基础属性加成(魔法攻击力=60 * rate)
        char.基础属性加成(独立攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_20098(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '灾厄的堕星公爵')"
    if mode == 0:
        char.基础属性加成(力量=70 * rate)
        char.基础属性加成(智力=70 * rate)
        char.基础属性加成(体力=70 * rate)
        char.基础属性加成(精神=70 * rate)
    if mode == 1:
        pass


def enchanting_20099(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '强攻型首饰宝珠 ')"
    if mode == 0:
        char.所有属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20100(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '红色禽兽施布拉斯')"
    if mode == 0:
        char.火属性强化加成(15 * rate)
        char.光属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20101(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '适应者扎戈斯')"
    if mode == 0:
        char.冰属性强化加成(15 * rate)
        char.暗属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20102(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '遗忘姓名的守门人 ')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
    if mode == 1:
        pass


def enchanting_20103(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '崔拉&昙娜 ')"
    if mode == 0:
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_20106(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '破坏之洛多斯')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
        char.基础属性加成(力量=25 * rate)
    if mode == 1:
        pass


def enchanting_20107(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '魅惑之哈妮尔 ')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.06 * rate)
        char.基础属性加成(智力=25 * rate)
    if mode == 1:
        pass


def enchanting_20108(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带, 鞋', '希洛克的噩梦 ')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(力量=25 * rate)
    if mode == 1:
        pass


def enchanting_20109(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带, 鞋', '惊悸梦魇')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.基础属性加成(智力=25 * rate)
    if mode == 1:
        pass


def enchanting_20112(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '迷雾中的暗杀者 ')"
    if mode == 0:
        char.基础属性加成(体力=100 * rate)
    if mode == 1:
        pass


def enchanting_20113(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '卢克西 ')"
    if mode == 0:
        char.基础属性加成(精神=100 * rate)
    if mode == 1:
        pass


def enchanting_20114(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '无念之希洛克 - 莱斯特 ')"
    if mode == 0:
        char.基础属性加成(力量=100 * rate)
    if mode == 1:
        pass


def enchanting_20118(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '耳环', '魂·异界耳环宝珠')"
    if mode == 0:
        char.基础属性加成(力量=150 * rate)
        char.基础属性加成(智力=150 * rate)
        char.基础属性加成(体力=150 * rate)
        char.基础属性加成(精神=150 * rate)
    if mode == 1:
        pass


def enchanting_20119(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '德鲁伊·弥雅 ')"
    if mode == 0:
        char.基础属性加成(力量=55 * rate)
        char.基础属性加成(智力=55 * rate)
        char.基础属性加成(体力=55 * rate)
        char.基础属性加成(精神=55 * rate)
    if mode == 1:
        pass


def enchanting_20120(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '清夜 ')"
    if mode == 0:
        char.所有属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20121(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '黑夜的启示者 ')"
    if mode == 0:
        char.基础属性加成(力量=35 * rate)
        char.基础属性加成(智力=35 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20122(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '夜之伪装者 ')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20123(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '先知者埃思拉 ')"
    if mode == 0:
        char.冰属性强化加成(30 * rate)
        char.暗属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20124(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '赤鬼索伦 ')"
    if mode == 0:
        char.火属性强化加成(30 * rate)
        char.光属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20125(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '魂·异界守护者沃利')"
    if mode == 0:
        char.基础属性加成(力量=70 * rate)
        char.基础属性加成(智力=70 * rate)
        char.基础属性加成(体力=70 * rate)
        char.基础属性加成(精神=70 * rate)
    if mode == 1:
        pass


def enchanting_20126(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '毒王路易斯 ')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20127(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '青面修罗洛兹贝伦 ')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20128(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '伪装者血腥里娅 ')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
    if mode == 1:
        pass


def enchanting_20129(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '伪装者尼罗罗特 ')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20130(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '特里亚·赛鲁姆 ')"
    if mode == 0:
        char.基础属性加成(体力=75 * rate)
    if mode == 1:
        pass


def enchanting_20131(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '烈焰蜘蛛 ')"
    if mode == 0:
        char.基础属性加成(精神=75 * rate)
    if mode == 1:
        pass


def enchanting_20132(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '魂·异界首饰宝珠 (所有属性强化)')"
    if mode == 0:
        char.所有属性强化加成(28 * rate)
    if mode == 1:
        pass


def enchanting_20133(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '饮血者清夜 ')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
        char.基础属性加成(智力=45 * rate)
        char.基础属性加成(体力=45 * rate)
        char.基础属性加成(精神=45 * rate)
    if mode == 1:
        pass


def enchanting_20134(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '新手冒险家宝珠(强攻)')"
    if mode == 0:
        char.所有属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20135(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '新手冒险家宝珠(强攻)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=55 * rate)
        char.基础属性加成(魔法攻击力=55 * rate)
        char.基础属性加成(独立攻击力=55 * rate)
    if mode == 1:
        pass


def enchanting_20136(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '绝望之泰玛特 ')"
    if mode == 0:
        char.基础属性加成(力量=65 * rate)
        char.基础属性加成(智力=65 * rate)
        char.基础属性加成(体力=65 * rate)
        char.基础属性加成(精神=65 * rate)
    if mode == 1:
        pass


def enchanting_20137(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '黑暗笼罩桀特 ')"
    if mode == 0:
        char.火属性强化加成(26 * rate)
        char.光属性强化加成(26 * rate)
    if mode == 1:
        pass


def enchanting_20138(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '纯血者狄摩尔 ')"
    if mode == 0:
        char.冰属性强化加成(26 * rate)
        char.暗属性强化加成(26 * rate)
    if mode == 1:
        pass


def enchanting_20139(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '鞋', '囚途者梵塔 ')"
    if mode == 0:
        char.基础属性加成(移动速度=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20140(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '堕落阿拉贡的孤独 ')"
    if mode == 0:
        char.冰属性强化加成(30 * rate)
        char.暗属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20141(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '堕落阿拉贡的愤怒 ')"
    if mode == 0:
        char.火属性强化加成(30 * rate)
        char.光属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20142(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '堕落阿拉贡的疯狂 ')"
    if mode == 0:
        char.所有属性强化加成(28 * rate)
    if mode == 1:
        pass


def enchanting_20143(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '先知者埃思拉 ')"
    if mode == 0:
        char.冰属性强化加成(30 * rate)
        char.暗属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20144(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '赤鬼索伦 ')"
    if mode == 0:
        char.火属性强化加成(30 * rate)
        char.光属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20145(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '疯魔索伦 ')"
    if mode == 0:
        char.基础属性加成(力量=70 * rate)
        char.基础属性加成(智力=70 * rate)
        char.基础属性加成(体力=70 * rate)
        char.基础属性加成(精神=70 * rate)
    if mode == 1:
        pass


def enchanting_20146(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '黑色魔物的逆鳞 ')"
    if mode == 0:
        char.所有属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20147(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '公义之奈克斯 ')"
    if mode == 0:
        char.基础属性加成(独立攻击力=70 * rate)
        char.基础属性加成(力量=40 * rate)
    if mode == 1:
        pass


def enchanting_20148(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '慈悲之维塔 ')"
    if mode == 0:
        char.基础属性加成(独立攻击力=70 * rate)
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_20149(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '迷雾中的暗杀者 ')"
    if mode == 0:
        char.基础属性加成(体力=100 * rate)
    if mode == 1:
        pass


def enchanting_20150(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '无我之希洛克 - 拉维茜 ')"
    if mode == 0:
        char.基础属性加成(智力=100 * rate)
    if mode == 1:
        pass


def enchanting_20151(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '无言之希洛克 - 吉里 ')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=70 * rate)
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_20152(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器, 上衣, 下装', '无形之希洛克 ')"
    if mode == 0:
        char.基础属性加成(物理攻击力=70 * rate)
        char.基础属性加成(力量=40 * rate)
    if mode == 1:
        pass


def enchanting_20153(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '深沉的恐怖之阿斯特罗斯 ')"
    if mode == 0:
        char.所有属性强化加成(28 * rate)
    if mode == 1:
        pass


def enchanting_20154(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '辅助装备', '混沌之神奥兹玛 ')"
    if mode == 0:
        char.基础属性加成(物理攻击力=110 * rate)
        char.基础属性加成(魔法攻击力=110 * rate)
        char.基础属性加成(独立攻击力=110 * rate)
    if mode == 1:
        pass


def enchanting_20155(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '辅助装备', '毁灭之神卡赞 ')"
    if mode == 0:
        char.基础属性加成(力量=100 * rate)
        char.基础属性加成(智力=100 * rate)
        char.基础属性加成(体力=100 * rate)
        char.基础属性加成(精神=100 * rate)
    if mode == 1:
        pass


def enchanting_20156(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '魔法石', '毁灭征兆之贝利亚斯 ')"
    if mode == 0:
        char.所有属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20157(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '魔法石', '迫近的绝望之泰玛特 ')"
    if mode == 0:
        char.基础属性加成(力量=80 * rate)
        char.基础属性加成(智力=80 * rate)
        char.基础属性加成(体力=80 * rate)
        char.基础属性加成(精神=80 * rate)
    if mode == 1:
        pass


def enchanting_20158(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(158, '头肩', '黑色恐怖之阿斯特罗斯 ')"
    if mode == 0:
        char.基础属性加成(力量=40 * rate)
        char.基础属性加成(智力=40 * rate)
        char.基础属性加成(体力=40 * rate)
        char.基础属性加成(精神=40 * rate)
        char.基础属性加成(物理攻击力=10 * rate)
        char.基础属性加成(魔法攻击力=10 * rate)
        char.基础属性加成(独立攻击力=10 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
        char.技能攻击力加成(0.02 * rate)
    if mode == 1:
        pass


def enchanting_20159(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '卢克西 ')"
    if mode == 0:
        char.基础属性加成(精神=100 * rate)
    if mode == 1:
        pass


def enchanting_20160(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '刮刮乐宝珠 (物理暴击率)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20161(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '刮刮乐宝珠 (物理暴击率)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20162(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '刮刮乐宝珠 (魔法暴击率)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20163(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '刮刮乐宝珠 (魔法暴击率)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20164(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '腰带', '卡兰蒂斯宝珠')"
    if mode == 0:
        char.基础属性加成(力量=30 * rate)
        char.基础属性加成(智力=30 * rate)
        char.基础属性加成(体力=30 * rate)
        char.基础属性加成(精神=30 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 30, 1)
    if mode == 1:
        pass


def enchanting_20165(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', '光之英雄凯特拉宝珠')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(独立攻击力=40 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20166(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '鞋', '雷欧帕多将军宝珠')"
    if mode == 0:
        char.基础属性加成(力量=30 * rate)
        char.基础属性加成(智力=30 * rate)
        char.基础属性加成(体力=30 * rate)
        char.基础属性加成(精神=30 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 30, 1)
    if mode == 1:
        pass


def enchanting_20167(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '巫女迪美利亚宝珠')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20168(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '乱斗王的宝珠 [智慧]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20169(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '乱斗王的宝珠 [魔法攻击]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20170(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '乱斗王的宝珠 [冥想]')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
    if mode == 1:
        pass


def enchanting_20171(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '乱斗王的宝珠 [光属性增幅]')"
    if mode == 0:
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20172(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '乱斗王的宝珠 [活力]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
    if mode == 1:
        pass


def enchanting_20173(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '乱斗王的宝珠 [冰属性增幅]')"
    if mode == 0:
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20174(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '乱斗王的宝珠 [灵心]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20175(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '乱斗王的宝珠 [物理攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20176(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '乱斗王的宝珠 [武力]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20177(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '乱斗王的宝珠 [火属性增幅]')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20178(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '乱斗王的宝珠 [鹰眼]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20179(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '乱斗王的宝珠 [暗属性增幅]')"
    if mode == 0:
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20180(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '乱斗王的宝珠 [独立攻击]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20181(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '物理、 魔法暴击率 +8%')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.08 * rate)
        char.基础属性加成(魔法暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20182(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '宇宙恶魔 : 罗什(黑暗) ')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20183(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '[活动]酷夏迷你宠物专属宝珠')"
    if mode == 0:
        char.基础属性加成(力量=10 * rate)
        char.基础属性加成(智力=10 * rate)
        char.基础属性加成(体力=10 * rate)
        char.基础属性加成(精神=10 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20184(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '[活动]物理暴击率+6百分比')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20185(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '[活动]物理暴击率+8百分比')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20186(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '[活动]魔法暴击率+8百分比')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20187(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '哈林装备专属宝珠 (物理暴击率)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20188(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '哈林装备专属宝珠 (魔法暴击率)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20189(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '哈林史诗专用物理暴击率')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20190(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '哈林史诗专用魔法暴击率')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20191(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '大乱弹宠物强身神秘宝珠')"
    if mode == 0:
        char.基础属性加成(力量=30 * rate)
        char.基础属性加成(智力=30 * rate)
        char.基础属性加成(体力=30 * rate)
        char.基础属性加成(精神=30 * rate)
    if mode == 1:
        pass


def enchanting_20192(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '大乱弹宠物强身神秘宝珠')"
    if mode == 0:
        char.基础属性加成(力量=35 * rate)
        char.基础属性加成(智力=35 * rate)
        char.基础属性加成(体力=35 * rate)
        char.基础属性加成(精神=35 * rate)
    if mode == 1:
        pass


def enchanting_20193(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '大乱弹宠物强身神秘宝珠')"
    if mode == 0:
        char.基础属性加成(力量=40 * rate)
        char.基础属性加成(智力=40 * rate)
        char.基础属性加成(体力=40 * rate)
        char.基础属性加成(精神=40 * rate)
    if mode == 1:
        pass


def enchanting_20194(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '大乱弹宠物强身神秘宝珠')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
        char.基础属性加成(智力=45 * rate)
        char.基础属性加成(体力=45 * rate)
        char.基础属性加成(精神=45 * rate)
    if mode == 1:
        pass


def enchanting_20195(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '大乱弹宠物强身神秘宝珠')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
        char.基础属性加成(智力=50 * rate)
        char.基础属性加成(体力=50 * rate)
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20196(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩, 腰带, 鞋', '天界支援兵 ')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_20197(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '誓卫者宝珠')"
    if mode == 0:
        char.基础属性加成(物理攻击力=45 * rate)
        char.基础属性加成(力量=15 * rate)
    if mode == 1:
        pass


def enchanting_20198(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '古代图书馆宝珠')"
    if mode == 0:
        char.基础属性加成(独立攻击力=45 * rate)
        char.基础属性加成(力量=15 * rate)
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_20199(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '塔拉库沓宝珠')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=45 * rate)
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_20200(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '旋魔会宝珠')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
        char.基础属性加成(智力=45 * rate)
        char.基础属性加成(体力=45 * rate)
        char.基础属性加成(精神=45 * rate)
    if mode == 1:
        pass


def enchanting_20201(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装, 武器', '胜者宝珠 (物攻/力量)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=45 * rate)
        char.基础属性加成(力量=15 * rate)
    if mode == 1:
        pass


def enchanting_20202(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装, 武器', '胜者宝珠 (魔攻/智力)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=45 * rate)
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_20203(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装, 武器', '胜者宝珠 (独攻/力量)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=45 * rate)
        char.基础属性加成(力量=15 * rate)
    if mode == 1:
        pass


def enchanting_20204(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装, 武器', '胜者宝珠 (独攻/智力)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=45 * rate)
        char.基础属性加成(智力=15 * rate)
    if mode == 1:
        pass


def enchanting_20205(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '燃烧的维京宝珠')"
    if mode == 0:
        char.火属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20206(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '冰冷的维京宝珠')"
    if mode == 0:
        char.冰属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20207(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '耀眼的维京宝珠')"
    if mode == 0:
        char.光属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20208(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '漆黑的维京宝珠')"
    if mode == 0:
        char.暗属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20209(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '耳环', '制造者卢克 (光) ')"
    if mode == 0:
        char.基础属性加成(力量=125 * rate)
        char.基础属性加成(智力=125 * rate)
        char.基础属性加成(体力=125 * rate)
        char.基础属性加成(精神=125 * rate)
    if mode == 1:
        pass


def enchanting_20210(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '花之女王波塞姆 ')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20211(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '普雷·伊希斯 ')"
    if mode == 0:
        char.所有属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20212(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '野兽斯瑞姆 ')"
    if mode == 0:
        char.基础属性加成(力量=80 * rate)
        char.基础属性加成(智力=80 * rate)
        char.基础属性加成(体力=80 * rate)
        char.基础属性加成(精神=80 * rate)
    if mode == 1:
        pass


def enchanting_20213(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '红腿爱克托 ')"
    if mode == 0:
        char.基础属性加成(物理攻击力=70 * rate)
        char.基础属性加成(魔法攻击力=70 * rate)
        char.基础属性加成(独立攻击力=70 * rate)
    if mode == 1:
        pass


def enchanting_20214(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '四维 +60')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20215(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '三攻 +50')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(独立攻击力=50 * rate)
    if mode == 1:
        pass


def enchanting_20216(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '谋略家诺兰的火之宝珠 (首饰)')"
    if mode == 0:
        char.火属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20217(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '谋略家诺兰的冰之宝珠 (首饰)')"
    if mode == 0:
        char.冰属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20218(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '谋略家诺兰的光之宝珠 (首饰)')"
    if mode == 0:
        char.光属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20219(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '谋略家诺兰的暗之宝珠 (首饰)')"
    if mode == 0:
        char.暗属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20220(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '谋略家诺兰的强攻宝珠 (辅助装备)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=70 * rate)
        char.基础属性加成(魔法攻击力=70 * rate)
        char.基础属性加成(独立攻击力=70 * rate)
    if mode == 1:
        pass


def enchanting_20221(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '谋略家诺兰的四维宝珠 (辅助装备)')"
    if mode == 0:
        char.基础属性加成(力量=80 * rate)
        char.基础属性加成(智力=80 * rate)
        char.基础属性加成(体力=80 * rate)
        char.基础属性加成(精神=80 * rate)
    if mode == 1:
        pass


def enchanting_20222(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '谋略家诺兰的四维宝珠 (魔法石)')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20223(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '耳环', '谋略家诺兰的四维宝珠 (耳环)')"
    if mode == 0:
        char.基础属性加成(力量=125 * rate)
        char.基础属性加成(智力=125 * rate)
        char.基础属性加成(体力=125 * rate)
        char.基础属性加成(精神=125 * rate)
    if mode == 1:
        pass


def enchanting_20224(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '萌噬噬专属宝珠')"
    if mode == 0:
        char.所有属性抗性加成(10 * rate)
        char.火属性强化加成(10 * rate)
        char.冰属性强化加成(10 * rate)
        char.光属性强化加成(10 * rate)
        char.暗属性强化加成(10 * rate)
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(精神=20 * rate)
    if mode == 1:
        pass


def enchanting_20225(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '寻宝王的魔法石宝珠')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
        char.基础属性加成(智力=50 * rate)
        char.基础属性加成(体力=50 * rate)
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20226(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '寻宝王的辅助装备宝珠')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20227(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '鞋', '维京劫掠宝珠(头肩)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 35, 1)
    if mode == 1:
        pass


def enchanting_20228(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '天弓亚历山德拉 ')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20229(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '红腿爱克托 ')"
    if mode == 0:
        char.基础属性加成(物理攻击力=70 * rate)
        char.基础属性加成(魔法攻击力=70 * rate)
        char.基础属性加成(独立攻击力=70 * rate)
    if mode == 1:
        pass


def enchanting_20230(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '普雷·伊希斯 ')"
    if mode == 0:
        char.所有属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20231(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '耳环', '制造者卢克 (光) ')"
    if mode == 0:
        char.基础属性加成(力量=125 * rate)
        char.基础属性加成(智力=125 * rate)
        char.基础属性加成(体力=125 * rate)
        char.基础属性加成(精神=125 * rate)
    if mode == 1:
        pass


def enchanting_20232(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '吉赛尔 ')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20233(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '深海头肩宝珠 (Lv1~50)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20234(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '遗忘海域称号宝珠(Lv1~10)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 10, 1)
    if mode == 1:
        pass


def enchanting_20235(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '遗忘海域称号宝珠(Lv10~20)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 10, 20, 1)
    if mode == 1:
        pass


def enchanting_20236(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '遗忘海域称号宝珠(Lv20~30)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 20, 30, 1)
    if mode == 1:
        pass


def enchanting_20237(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '遗忘海域称号宝珠(Lv30~40)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 30, 40, 1)
    if mode == 1:
        pass


def enchanting_20238(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '遗忘海域称号宝珠(Lv40~50)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 40, 50, 1)
    if mode == 1:
        pass


def enchanting_20239(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '深海称号宝珠 (Lv1~20)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 20, 1)
    if mode == 1:
        pass


def enchanting_20240(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '深海称号宝珠 (Lv10~30)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 10, 30, 1)
    if mode == 1:
        pass


def enchanting_20241(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '深海称号宝珠 (Lv20~40)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 20, 40, 1)
    if mode == 1:
        pass


def enchanting_20242(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '深海称号宝珠 (Lv30~50)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 30, 50, 1)
    if mode == 1:
        pass


def enchanting_20243(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '称号', '深海称号宝珠 (Lv1~50)')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20244(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '天弓亚历山德拉 ')"
    if mode == 0:
        char.所有属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20245(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '耳环', '黑眼之夏勒·弗兹 ')"
    if mode == 0:
        char.基础属性加成(力量=150 * rate)
        char.基础属性加成(智力=150 * rate)
        char.基础属性加成(体力=150 * rate)
        char.基础属性加成(精神=150 * rate)
    if mode == 1:
        pass


def enchanting_20246(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '回归冒险家耳环宝珠')"
    if mode == 0:
        char.基础属性加成(力量=55 * rate)
        char.基础属性加成(智力=55 * rate)
        char.基础属性加成(体力=55 * rate)
        char.基础属性加成(精神=55 * rate)
    if mode == 1:
        pass


def enchanting_20247(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '协力型冒险宝珠 (头肩/腰带/鞋子)')"
    if mode == 0:
        char.基础属性加成(体力=75 * rate)
        char.基础属性加成(精神=75 * rate)
    if mode == 1:
        pass


def enchanting_20248(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '强攻型冒险宝珠 (力攻)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20249(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '强攻型冒险宝珠 (智攻)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20250(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '强攻型冒险宝珠 (力独)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20251(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '强攻型冒险宝珠 (智独)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20252(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '腰带, 鞋', '爆裂之崔拉 ')"
    if mode == 0:
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_20253(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '腰带, 鞋', '包容之昙娜 ')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
    if mode == 1:
        pass


def enchanting_20254(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '花郎道 ')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.1 * rate)
        char.基础属性加成(魔法暴击率=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20255(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '四维跃迁宝珠')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
        char.基础属性加成(智力=50 * rate)
        char.基础属性加成(体力=50 * rate)
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20256(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '狂浪突袭宝珠')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20257(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '奔浪突袭宝珠')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(独立攻击力=50 * rate)
    if mode == 1:
        pass


def enchanting_20258(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '谋略家的勇气宝珠')"
    if mode == 0:
        char.所有属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20259(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '极跃魔力宝珠')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
        char.基础属性加成(智力=50 * rate)
        char.基础属性加成(体力=50 * rate)
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20260(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '极跃能量宝珠')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20261(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链', '天运之轮强攻宝珠 (项链)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20262(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '戒指', '天运之轮强攻宝珠 (戒指)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20263(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '手镯', '天运之轮强攻宝珠 (手镯)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20264(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '天运之轮协力宝珠 (魔法石)')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20265(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '天运之轮协力宝珠 (辅助装备)')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20266(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '最强大作战武器宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20267(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '最强大作战防具宝珠 (强攻)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(独立攻击力=50 * rate)
    if mode == 1:
        pass


def enchanting_20268(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '最强大作战防具宝珠 (强攻)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20269(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '最强大作战防具宝珠 (强攻)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20270(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '最强大作战防具宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(体力=75 * rate)
    if mode == 1:
        pass


def enchanting_20271(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '最强大作战防具宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(精神=75 * rate)
    if mode == 1:
        pass


def enchanting_20272(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '最强大作战首饰宝珠 (强攻)')"
    if mode == 0:
        char.火属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20273(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '最强大作战首饰宝珠 (强攻)')"
    if mode == 0:
        char.冰属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20274(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '最强大作战首饰宝珠 (强攻)')"
    if mode == 0:
        char.光属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20275(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '最强大作战首饰宝珠 (强攻)')"
    if mode == 0:
        char.暗属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20276(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '最强大作战首饰宝珠 (强攻)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20277(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '最强大作战辅助装备宝珠 (强攻)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(独立攻击力=50 * rate)
    if mode == 1:
        pass


def enchanting_20278(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '最强大作战辅助装备宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20279(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '最强大作战魔法石宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
        char.基础属性加成(智力=50 * rate)
        char.基础属性加成(体力=50 * rate)
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20280(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '最强大作战防具宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20281(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '冥灵的安息 ')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
    if mode == 1:
        pass


def enchanting_20282(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(158, '魔法石', '复仇之混沌恶神奥兹玛 ')"
    if mode == 0:
        char.所有属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20283(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(158, '魔法石', '脱离冥界的毁灭之神卡赞 ')"
    if mode == 0:
        char.基础属性加成(力量=100 * rate)
        char.基础属性加成(智力=100 * rate)
        char.基础属性加成(体力=100 * rate)
        char.基础属性加成(精神=100 * rate)
    if mode == 1:
        pass


def enchanting_20284(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '辅助装备', '魂·异界辅助装备宝珠 (强攻)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=110 * rate)
        char.基础属性加成(魔法攻击力=110 * rate)
        char.基础属性加成(独立攻击力=110 * rate)
    if mode == 1:
        pass


def enchanting_20285(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '辅助装备', '魂·异界辅助装备宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=100 * rate)
        char.基础属性加成(智力=100 * rate)
        char.基础属性加成(体力=100 * rate)
        char.基础属性加成(精神=100 * rate)
    if mode == 1:
        pass


def enchanting_20286(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '魔法石', '魂·异界魔法石宝珠 (强攻)')"
    if mode == 0:
        char.所有属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20287(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(138, '魔法石', '魂·异界魔法石宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=80 * rate)
        char.基础属性加成(智力=80 * rate)
        char.基础属性加成(体力=80 * rate)
        char.基础属性加成(精神=80 * rate)
    if mode == 1:
        pass


def enchanting_20288(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(158, '头肩', '黑色恐怖之阿斯特罗斯 ')"
    if mode == 0:
        char.基础属性加成(力量=40 * rate)
        char.基础属性加成(智力=40 * rate)
        char.基础属性加成(体力=40 * rate)
        char.基础属性加成(精神=40 * rate)
        char.基础属性加成(物理攻击力=10 * rate)
        char.基础属性加成(魔法攻击力=10 * rate)
        char.基础属性加成(独立攻击力=10 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
        char.技能攻击力加成(0.02 * rate)
    if mode == 1:
        pass


def enchanting_20289(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '混沌居士清夜 ')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20290(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '将军卡列林 ')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(物理攻击力=55 * rate)
    if mode == 1:
        pass


def enchanting_20291(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '副官雷奥尼特 ')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(魔法攻击力=55 * rate)
    if mode == 1:
        pass


def enchanting_20292(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '追迹者德劳克 ')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(独立攻击力=55 * rate)
    if mode == 1:
        pass


def enchanting_20293(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '侵蚀者特萝卡 ')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(独立攻击力=55 * rate)
    if mode == 1:
        pass


def enchanting_20294(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '腰带, 鞋', '被混沌蚕食的K ')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20295(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '腰带, 鞋', '追随混沌的德斯佩罗 ')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20296(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '畅玩辅助装备宝珠 (强攻)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=70 * rate)
        char.基础属性加成(魔法攻击力=70 * rate)
        char.基础属性加成(独立攻击力=70 * rate)
    if mode == 1:
        pass


def enchanting_20297(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '辅助装备', '畅玩辅助装备宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=80 * rate)
        char.基础属性加成(智力=80 * rate)
        char.基础属性加成(体力=80 * rate)
        char.基础属性加成(精神=80 * rate)
    if mode == 1:
        pass


def enchanting_20298(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '畅玩魔法石宝珠 (强攻)')"
    if mode == 0:
        char.所有属性强化加成(20 * rate)
    if mode == 1:
        pass


def enchanting_20299(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '畅玩魔法石宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20300(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '耳环', '畅玩耳环宝珠')"
    if mode == 0:
        char.基础属性加成(力量=150 * rate)
        char.基础属性加成(智力=150 * rate)
        char.基础属性加成(体力=150 * rate)
        char.基础属性加成(精神=150 * rate)
    if mode == 1:
        pass


def enchanting_20301(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '回归专属辅助装备宝珠 (强攻)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=55 * rate)
        char.基础属性加成(魔法攻击力=55 * rate)
        char.基础属性加成(独立攻击力=55 * rate)
    if mode == 1:
        pass


def enchanting_20302(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '回归专属辅助装备宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=70 * rate)
        char.基础属性加成(智力=70 * rate)
        char.基础属性加成(体力=70 * rate)
        char.基础属性加成(精神=70 * rate)
    if mode == 1:
        pass


def enchanting_20303(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '回归专属魔法石宝珠 (协力)')"
    if mode == 0:
        char.基础属性加成(力量=55 * rate)
        char.基础属性加成(智力=55 * rate)
        char.基础属性加成(体力=55 * rate)
        char.基础属性加成(精神=55 * rate)
    if mode == 1:
        pass


def enchanting_20304(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '回归专属首饰宝珠 (强攻)')"
    if mode == 0:
        char.所有属性强化加成(23 * rate)
    if mode == 1:
        pass


def enchanting_20305(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '寻宝王的武器宝珠 (体力)')"
    if mode == 0:
        char.基础属性加成(体力=50 * rate)
    if mode == 1:
        pass


def enchanting_20306(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '寻宝王的武器宝珠 (精神)')"
    if mode == 0:
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20307(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器', '寻宝王的武器宝珠 (智力)')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20308(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '寻宝王的衣裳宝珠 (物攻/力量)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20309(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '寻宝王的衣裳宝珠 (魔攻/智力)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20310(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '寻宝王的衣裳宝珠 (独攻/力量)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20311(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '寻宝王的衣裳宝珠 (独攻/智力)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20312(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '上衣, 下装', '寻宝王的衣裳宝珠 (体力)')"
    if mode == 0:
        char.基础属性加成(体力=50 * rate)
    if mode == 1:
        pass


def enchanting_20313(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '上衣, 下装', '寻宝王的衣裳宝珠 (精神)')"
    if mode == 0:
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20314(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '寻宝王的衣裳宝珠 (智力)')"
    if mode == 0:
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20315(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '寻宝王的武器宝珠 (属强)')"
    if mode == 0:
        char.所有属性强化加成(13 * rate)
    if mode == 1:
        pass


def enchanting_20316(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '魂灭结晶 : 暴击率宝珠')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20317(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '鞋', '混沌之英雄凯特拉宝珠')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
        char.基础属性加成(智力=45 * rate)
        char.基础属性加成(体力=45 * rate)
        char.基础属性加成(精神=45 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 30, 1)
    if mode == 1:
        pass


def enchanting_20318(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '辅助装备', '骑士莱恩宝珠')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20319(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '吟游诗人薇泽达宝珠')"
    if mode == 0:
        char.基础属性加成(力量=55 * rate)
        char.基础属性加成(智力=55 * rate)
        char.基础属性加成(体力=55 * rate)
        char.基础属性加成(精神=55 * rate)
    if mode == 1:
        pass


def enchanting_20320(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '暗之英雄凯特拉宝珠')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
        char.基础属性加成(智力=75 * rate)
        char.基础属性加成(体力=75 * rate)
        char.基础属性加成(精神=75 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20321(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '仙灵之赐宝珠 [武力][武力]')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
    if mode == 1:
        pass


def enchanting_20322(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [武力][智慧]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(智力=25 * rate)
    if mode == 1:
        pass


def enchanting_20323(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [武力][活力]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(体力=25 * rate)
    if mode == 1:
        pass


def enchanting_20324(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [武力][冥想]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(精神=25 * rate)
    if mode == 1:
        pass


def enchanting_20325(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [武力][物理攻击]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20326(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [武力][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20327(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [武力][独立攻击]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20328(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [武力][鹰眼]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20329(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [武力][灵心]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20330(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [武力][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20331(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [武力][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20332(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [武力][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20333(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [武力][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20334(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '仙灵之赐宝珠 [智慧][智慧]')"
    if mode == 0:
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_20335(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [智慧][活力]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(体力=25 * rate)
    if mode == 1:
        pass


def enchanting_20336(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [智慧][冥想]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(精神=25 * rate)
    if mode == 1:
        pass


def enchanting_20337(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [智慧][物理攻击]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20338(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [智慧][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20339(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [智慧][独立攻击]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20340(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [智慧][鹰眼]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20341(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [智慧][灵心]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20342(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [智慧][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20343(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [智慧][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20344(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [智慧][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20345(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [智慧][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20346(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [活力][活力]')"
    if mode == 0:
        char.基础属性加成(体力=50 * rate)
    if mode == 1:
        pass


def enchanting_20347(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [活力][冥想]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(精神=25 * rate)
    if mode == 1:
        pass


def enchanting_20348(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [活力][物理攻击]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20349(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [活力][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20350(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [活力][独立攻击]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20351(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [活力][鹰眼]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20352(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [活力][灵心]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20353(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [活力][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20354(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [活力][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20355(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [活力][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20356(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [活力][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20357(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [冥想][冥想]')"
    if mode == 0:
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20358(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [冥想][物理攻击]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20359(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [冥想][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20360(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [冥想][独立攻击]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20361(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [冥想][鹰眼]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20362(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [冥想][灵心]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20363(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [冥想][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20364(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [冥想][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20365(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [冥想][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20366(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [冥想][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20367(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '仙灵之赐宝珠 [物理攻击][物理攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_20368(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [物理攻击][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20369(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '仙灵之赐宝珠 [物理攻击][独立攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20370(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [物理攻击][鹰眼]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20371(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [物理攻击][灵心]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20372(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '仙灵之赐宝珠 [物理攻击][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20373(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '仙灵之赐宝珠 [物理攻击][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20374(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '仙灵之赐宝珠 [物理攻击][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20375(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '仙灵之赐宝珠 [物理攻击][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20376(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '仙灵之赐宝珠 [魔法攻击][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=40 * rate)
    if mode == 1:
        pass


def enchanting_20377(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '仙灵之赐宝珠 [魔法攻击][独立攻击]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20378(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [魔法攻击][鹰眼]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20379(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '仙灵之赐宝珠 [魔法攻击][灵心]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20380(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '仙灵之赐宝珠 [魔法攻击][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20381(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '仙灵之赐宝珠 [魔法攻击][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20382(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '仙灵之赐宝珠 [魔法攻击][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20383(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '仙灵之赐宝珠 [魔法攻击][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20384(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '仙灵之赐宝珠 [独立攻击][独立攻击]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_20385(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [独立攻击][鹰眼]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20386(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [独立攻击][灵心]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20387(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [独立攻击][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20388(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [独立攻击][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20389(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [独立攻击][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20390(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [独立攻击][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=30 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20391(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [鹰眼][鹰眼]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20392(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [鹰眼][灵心]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20393(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [鹰眼][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20394(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [鹰眼][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20395(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [鹰眼][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20396(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [鹰眼][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20397(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '恒久之刚毅宝珠 [灵心][灵心]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.08 * rate)
    if mode == 1:
        pass


def enchanting_20398(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [灵心][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20399(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [灵心][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20400(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [灵心][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20401(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [灵心][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20402(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '仙灵之赐宝珠 [火属性增幅][火属性增幅]')"
    if mode == 0:
        char.火属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_20403(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [火属性增幅][冰属性增幅]')"
    if mode == 0:
        char.火属性强化加成(8 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20404(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [火属性增幅][暗属性增幅]')"
    if mode == 0:
        char.火属性强化加成(8 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20405(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [火属性增幅][光属性增幅]')"
    if mode == 0:
        char.火属性强化加成(8 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20406(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '仙灵之赐宝珠 [冰属性增幅][冰属性增幅]')"
    if mode == 0:
        char.冰属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_20407(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [冰属性增幅][暗属性增幅]')"
    if mode == 0:
        char.冰属性强化加成(8 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20408(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [冰属性增幅][光属性增幅]')"
    if mode == 0:
        char.冰属性强化加成(8 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20409(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '仙灵之赐宝珠 [暗属性增幅][暗属性增幅]')"
    if mode == 0:
        char.暗属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_20410(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [暗属性增幅][光属性增幅]')"
    if mode == 0:
        char.暗属性强化加成(8 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20411(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '仙灵之赐宝珠 [光属性增幅][光属性增幅]')"
    if mode == 0:
        char.光属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_20412(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '耀银技能宝珠')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 15, 25, 1)
    if mode == 1:
        pass


def enchanting_20413(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿金技能宝珠')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 25, 35, 1)
    if mode == 1:
        pass


def enchanting_20414(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '超越极限宝珠 (头肩)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=20 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20415(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', '魂·异界空间支配者伽乌尼斯 (技能)')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(物理攻击力=40 * rate)
        char.基础属性加成(魔法攻击力=40 * rate)
        char.基础属性加成(独立攻击力=40 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20416(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '伊希斯之翼')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
        char.基础属性加成(智力=75 * rate)
        char.基础属性加成(体力=75 * rate)
        char.基础属性加成(精神=75 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=20 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20417(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带', '安徒恩之肤')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
        char.基础属性加成(智力=45 * rate)
        char.基础属性加成(体力=45 * rate)
        char.基础属性加成(精神=45 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20418(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '魔法石', '狄瑞吉之疫')"
    if mode == 0:
        char.基础属性加成(力量=70 * rate)
        char.基础属性加成(智力=70 * rate)
        char.基础属性加成(体力=70 * rate)
        char.基础属性加成(精神=70 * rate)
    if mode == 1:
        pass


def enchanting_20419(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '耳环', '卢克之械')"
    if mode == 0:
        char.基础属性加成(力量=140 * rate)
        char.基础属性加成(智力=140 * rate)
        char.基础属性加成(体力=140 * rate)
        char.基础属性加成(精神=140 * rate)
    if mode == 1:
        pass


def enchanting_20420(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '辅助装备', '罗特斯之触')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20421(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [武力][物理攻击]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20422(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [武力][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(力量=25 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20423(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [智慧][物理攻击]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20424(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [智慧][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(智力=25 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20425(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [活力][物理攻击]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20426(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [活力][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(体力=25 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20427(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [冥想][物理攻击]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20428(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [冥想][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(精神=25 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20429(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '恒久之刚毅宝珠 [物理攻击][物理攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_20430(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [物理攻击][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20431(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [物理攻击][独立攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20432(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [物理攻击][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20433(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [物理攻击][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20434(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [物理攻击][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20435(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [物理攻击][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20436(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '恒久之刚毅宝珠 [魔法攻击][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_20437(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [魔法攻击][独立攻击]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20438(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [魔法攻击][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.火属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20439(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [魔法攻击][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.冰属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20440(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [魔法攻击][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.暗属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20441(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '恒久之刚毅宝珠 [魔法攻击][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.光属性强化加成(8 * rate)
    if mode == 1:
        pass


def enchanting_20442(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '武器', '格陵布拉德')"
    if mode == 0:
        char.所有属性强化加成(16 * rate)
        char.基础属性加成(力量=50 * rate)
        char.基础属性加成(智力=50 * rate)
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(独立攻击力=50 * rate)
    if mode == 1:
        pass


def enchanting_20443(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [物理攻击][鹰眼]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20444(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [物理攻击][灵心]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20445(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [魔法攻击][鹰眼]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20446(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '恒久之刚毅宝珠 [魔法攻击][灵心]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20447(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '武器', '艾肯')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
        char.基础属性加成(攻击速度=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20448(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '武器', '阿古朗达')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
        char.基础属性加成(施放速度=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20449(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '辅助装备', '征服者克努特')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
    if mode == 1:
        pass


def enchanting_20450(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '战争之神奥丁')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
        char.基础属性加成(智力=75 * rate)
    if mode == 1:
        pass


def enchanting_20451(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '雷霆之神托尔')"
    if mode == 0:
        char.基础属性加成(体力=75 * rate)
        char.基础属性加成(精神=75 * rate)
    if mode == 1:
        pass


def enchanting_20452(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '腰带', '光明之神海姆达尔')"
    if mode == 0:
        char.基础属性加成(物理攻击力=36 * rate)
        char.基础属性加成(魔法攻击力=36 * rate)
        char.基础属性加成(独立攻击力=36 * rate)
    if mode == 1:
        pass


def enchanting_20453(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '鞋', '诡计之神洛基')"
    if mode == 0:
        char.基础属性加成(物理攻击力=36 * rate)
        char.基础属性加成(魔法攻击力=36 * rate)
        char.基础属性加成(独立攻击力=36 * rate)
    if mode == 1:
        pass


def enchanting_20454(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '耳环', '阿斯加德的祝福')"
    if mode == 0:
        char.基础属性加成(力量=135 * rate)
        char.基础属性加成(智力=135 * rate)
        char.基础属性加成(体力=135 * rate)
        char.基础属性加成(精神=135 * rate)
    if mode == 1:
        pass


def enchanting_20455(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '称号', '灿烂之光称号宝珠')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 35, 1)
    if mode == 1:
        pass


def enchanting_20456(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '头肩', '灿烂之光头肩宝珠')"
    if mode == 0:
        char.基础属性加成(力量=30 * rate)
        char.基础属性加成(智力=30 * rate)
        char.基础属性加成(体力=30 * rate)
        char.基础属性加成(精神=30 * rate)
        char.基础属性加成(物理攻击力=10 * rate)
        char.基础属性加成(魔法攻击力=10 * rate)
        char.基础属性加成(独立攻击力=10 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 35, 1)
    if mode == 1:
        pass


def enchanting_20457(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '阿拉德静谧之海宝珠')"
    if mode == 0:
        char.基础属性加成(体力=70 * rate)
        char.基础属性加成(精神=70 * rate)
    if mode == 1:
        pass


def enchanting_20458(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', '谋略家诺兰')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 2)
    if mode == 1:
        pass


def enchanting_20459(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '舞动青春宝珠 : 火属性强化 +25')"
    if mode == 0:
        char.火属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20460(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '舞动青春宝珠 : 冰属性强化 +25')"
    if mode == 0:
        char.冰属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20461(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '舞动青春宝珠 : 光属性强化 +25')"
    if mode == 0:
        char.光属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20462(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '舞动青春宝珠 : 暗属性强化 +25')"
    if mode == 0:
        char.暗属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20463(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '燃动青春宝珠 : 物理攻击力 +50、 力量 +20')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20464(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '燃动青春宝珠 : 魔法攻击力 +50、 智力 +20')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20465(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '燃动青春宝珠 : 独立攻击力 +50、 力量 +20')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20466(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '上衣, 下装', '燃动青春宝珠 : 独立攻击力 +50、 智力 +20')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20467(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '称号', '眷属之信念宝珠')"
    if mode == 0:
        char.所有属性强化加成(10 * rate)
        char.基础属性加成(物理攻击力=30 * rate)
        char.基础属性加成(魔法攻击力=30 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20468(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '无我之使徒宝珠')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
        char.基础属性加成(智力=75 * rate)
        char.基础属性加成(体力=75 * rate)
        char.基础属性加成(精神=75 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20469(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '崇高智慧宝珠')"
    if mode == 0:
        char.基础属性加成(智力=70 * rate)
    if mode == 1:
        pass


def enchanting_20470(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '鞋', '魂·异界贝诺马拉 (技能)')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
        char.基础属性加成(智力=45 * rate)
        char.基础属性加成(体力=45 * rate)
        char.基础属性加成(精神=45 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20471(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '称号', '魂·异界空间支配者伽乌尼斯 (攻击)')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(物理攻击力=40 * rate)
        char.基础属性加成(魔法攻击力=40 * rate)
        char.基础属性加成(独立攻击力=40 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_20472(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '魂·异界卡勒梅亚 (攻击)')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
        char.基础属性加成(智力=75 * rate)
        char.基础属性加成(体力=75 * rate)
        char.基础属性加成(精神=75 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=20 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_20473(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带', '安徒恩之肤')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
        char.基础属性加成(智力=45 * rate)
        char.基础属性加成(体力=45 * rate)
        char.基础属性加成(精神=45 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20474(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '鞋', '狄瑞吉之疫')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
        char.基础属性加成(智力=45 * rate)
        char.基础属性加成(体力=45 * rate)
        char.基础属性加成(精神=45 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20475(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '项链, 手镯, 戒指', '魂·异界恐怖之阿斯特罗斯')"
    if mode == 0:
        char.所有属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20476(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '魔法石', '魂·异界莫格尼斯')"
    if mode == 0:
        char.所有属性强化加成(18 * rate)
    if mode == 1:
        pass


def enchanting_20477(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '次元扭曲宝珠 [武力]')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
    if mode == 1:
        pass


def enchanting_20478(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '次元扭曲宝珠 [智慧]')"
    if mode == 0:
        char.基础属性加成(智力=50 * rate)
    if mode == 1:
        pass


def enchanting_20479(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '次元扭曲宝珠 [活力]')"
    if mode == 0:
        char.基础属性加成(体力=50 * rate)
    if mode == 1:
        pass


def enchanting_20480(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '次元扭曲宝珠 [冥想]')"
    if mode == 0:
        char.基础属性加成(精神=50 * rate)
    if mode == 1:
        pass


def enchanting_20481(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '次元扭曲宝珠 [物理攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_20482(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '次元扭曲宝珠 [魔法攻击]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_20483(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '次元扭曲宝珠 [独立攻击]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=60 * rate)
    if mode == 1:
        pass


def enchanting_20484(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '次元扭曲宝珠 [火属性增幅]')"
    if mode == 0:
        char.火属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_20485(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '次元扭曲宝珠 [冰属性增幅]')"
    if mode == 0:
        char.冰属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_20486(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '次元扭曲宝珠 [暗属性增幅]')"
    if mode == 0:
        char.暗属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_20487(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '次元扭曲宝珠 [光属性增幅]')"
    if mode == 0:
        char.光属性强化加成(16 * rate)
    if mode == 1:
        pass


def enchanting_20488(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '魂·异界卡勒梅亚 (技能)')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
        char.基础属性加成(智力=75 * rate)
        char.基础属性加成(体力=75 * rate)
        char.基础属性加成(精神=75 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=20 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20489(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带', '魂·异界海勒尼温 (技能)')"
    if mode == 0:
        char.基础属性加成(力量=45 * rate)
        char.基础属性加成(智力=45 * rate)
        char.基础属性加成(体力=45 * rate)
        char.基础属性加成(精神=45 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20490(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '辅助装备', '魂·异界可可卓拉 (攻击)')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20491(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '仲夏晴空宝珠 [火属性强化]')"
    if mode == 0:
        char.火属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20492(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '仲夏夜梦宝珠 [冰属性强化]')"
    if mode == 0:
        char.冰属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20493(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '仲夏晴空宝珠 [光属性强化]')"
    if mode == 0:
        char.光属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20494(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '项链, 手镯, 戒指', '仲夏夜梦宝珠 [暗属性强化]')"
    if mode == 0:
        char.暗属性强化加成(25 * rate)
    if mode == 1:
        pass


def enchanting_20495(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '仲夏晴空宝珠 [武器]')"
    if mode == 0:
        char.火属性强化加成(15 * rate)
        char.光属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20496(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '武器', '仲夏夜梦宝珠 [武器]')"
    if mode == 0:
        char.冰属性强化加成(15 * rate)
        char.暗属性强化加成(15 * rate)
    if mode == 1:
        pass


def enchanting_20497(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '亚贝罗的头肩宝珠 (技能)')"
    if mode == 0:
        char.基础属性加成(力量=60 * rate)
        char.基础属性加成(智力=60 * rate)
        char.基础属性加成(体力=60 * rate)
        char.基础属性加成(精神=60 * rate)
        char.基础属性加成(物理攻击力=16 * rate)
        char.基础属性加成(魔法攻击力=16 * rate)
        char.基础属性加成(独立攻击力=16 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20498(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带', '亚贝罗的腰带宝珠 (技能)')"
    if mode == 0:
        char.基础属性加成(力量=36 * rate)
        char.基础属性加成(智力=36 * rate)
        char.基础属性加成(体力=36 * rate)
        char.基础属性加成(精神=36 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20499(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '鞋', '亚贝罗的鞋子宝珠 (技能)')"
    if mode == 0:
        char.基础属性加成(力量=36 * rate)
        char.基础属性加成(智力=36 * rate)
        char.基础属性加成(体力=36 * rate)
        char.基础属性加成(精神=36 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20500(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '辅助装备', '亚贝罗的辅助装备宝珠 (攻击)')"
    if mode == 0:
        char.所有属性强化加成(9 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20501(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '仲夏晴空宝珠 [物理攻击力]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=50 * rate)
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(力量=20 * rate)
    if mode == 1:
        pass


def enchanting_20502(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '仲夏夜梦宝珠 [魔法攻击力]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=50 * rate)
        char.基础属性加成(独立攻击力=50 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20503(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '泰达·贝欧纳')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=20 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20504(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '鞋', '欧贝斯·罗什巴赫')"
    if mode == 0:
        char.基础属性加成(物理攻击力=36 * rate)
        char.基础属性加成(魔法攻击力=36 * rate)
        char.基础属性加成(独立攻击力=36 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_20505(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带', '歌兰蒂斯·格拉西亚')"
    if mode == 0:
        char.基础属性加成(物理攻击力=36 * rate)
        char.基础属性加成(魔法攻击力=36 * rate)
        char.基础属性加成(独立攻击力=36 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_20506(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '信奘')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
        char.基础属性加成(智力=75 * rate)
        char.基础属性加成(体力=75 * rate)
        char.基础属性加成(精神=75 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20507(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(185, '宠物', '魔界雪人萌宠宝珠')"
    if mode == 0:
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20508(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (攻击速度)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.005 * rate)
    if mode == 1:
        pass


def enchanting_20509(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (攻击速度)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20510(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (攻击速度)')"
    if mode == 0:
        char.基础属性加成(攻击速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20511(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (施放速度)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.005 * rate)
    if mode == 1:
        pass


def enchanting_20512(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (施放速度)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20513(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (施放速度)')"
    if mode == 0:
        char.基础属性加成(施放速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20514(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (暗属性强化)')"
    if mode == 0:
        char.暗属性强化加成(1 * rate)
    if mode == 1:
        pass


def enchanting_20515(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (暗属性强化)')"
    if mode == 0:
        char.暗属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20516(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '灿烂的宠物宝珠 (暗属性强化)')"
    if mode == 0:
        char.暗属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20517(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (魔法攻击)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=2 * rate)
    if mode == 1:
        pass


def enchanting_20518(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (魔法攻击)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=6 * rate)
    if mode == 1:
        pass


def enchanting_20519(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (魔法攻击)')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20520(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (物理攻击)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=2 * rate)
    if mode == 1:
        pass


def enchanting_20521(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (物理攻击)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=6 * rate)
    if mode == 1:
        pass


def enchanting_20522(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (物理攻击)')"
    if mode == 0:
        char.基础属性加成(物理攻击力=20 * rate)
    if mode == 1:
        pass


def enchanting_20523(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (火属性强化)')"
    if mode == 0:
        char.火属性强化加成(1 * rate)
    if mode == 1:
        pass


def enchanting_20524(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (火属性强化)')"
    if mode == 0:
        char.火属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20525(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '灿烂的宠物宝珠 (火属性强化)')"
    if mode == 0:
        char.火属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20526(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (光属性强化)')"
    if mode == 0:
        char.光属性强化加成(1 * rate)
    if mode == 1:
        pass


def enchanting_20527(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (光属性强化)')"
    if mode == 0:
        char.光属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20528(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '灿烂的宠物宝珠 (光属性强化)')"
    if mode == 0:
        char.光属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20529(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (智力)')"
    if mode == 0:
        char.基础属性加成(智力=3 * rate)
    if mode == 1:
        pass


def enchanting_20530(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (智力)')"
    if mode == 0:
        char.基础属性加成(智力=12 * rate)
    if mode == 1:
        pass


def enchanting_20531(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (智力)')"
    if mode == 0:
        char.基础属性加成(智力=30 * rate)
    if mode == 1:
        pass


def enchanting_20532(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (魔法暴击)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.005 * rate)
    if mode == 1:
        pass


def enchanting_20533(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (魔法暴击)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20534(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (魔法暴击)')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20535(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (精神)')"
    if mode == 0:
        char.基础属性加成(精神=3 * rate)
    if mode == 1:
        pass


def enchanting_20536(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (精神)')"
    if mode == 0:
        char.基础属性加成(精神=12 * rate)
    if mode == 1:
        pass


def enchanting_20537(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (精神)')"
    if mode == 0:
        char.基础属性加成(精神=30 * rate)
    if mode == 1:
        pass


def enchanting_20538(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (移动速度)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.005 * rate)
    if mode == 1:
        pass


def enchanting_20539(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (移动速度)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20540(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (移动速度)')"
    if mode == 0:
        char.基础属性加成(移动速度=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20541(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (力量)')"
    if mode == 0:
        char.基础属性加成(力量=3 * rate)
    if mode == 1:
        pass


def enchanting_20542(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (力量)')"
    if mode == 0:
        char.基础属性加成(力量=12 * rate)
    if mode == 1:
        pass


def enchanting_20543(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (力量)')"
    if mode == 0:
        char.基础属性加成(力量=30 * rate)
    if mode == 1:
        pass


def enchanting_20544(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (物理暴击)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.005 * rate)
    if mode == 1:
        pass


def enchanting_20545(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (物理暴击)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.01 * rate)
    if mode == 1:
        pass


def enchanting_20546(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (物理暴击)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.04 * rate)
    if mode == 1:
        pass


def enchanting_20547(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (体力)')"
    if mode == 0:
        char.基础属性加成(体力=3 * rate)
    if mode == 1:
        pass


def enchanting_20548(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (体力)')"
    if mode == 0:
        char.基础属性加成(体力=12 * rate)
    if mode == 1:
        pass


def enchanting_20549(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '灿烂的宠物宝珠 (体力)')"
    if mode == 0:
        char.基础属性加成(体力=30 * rate)
    if mode == 1:
        pass


def enchanting_20550(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (独立攻击)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=4 * rate)
    if mode == 1:
        pass


def enchanting_20551(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (独立攻击)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=10 * rate)
    if mode == 1:
        pass


def enchanting_20552(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '灿烂的宠物宝珠 (独立攻击)')"
    if mode == 0:
        char.基础属性加成(独立攻击力=35 * rate)
    if mode == 1:
        pass


def enchanting_20553(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '黯淡的宠物宝珠 (冰属性强化)')"
    if mode == 0:
        char.冰属性强化加成(1 * rate)
    if mode == 1:
        pass


def enchanting_20554(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '闪耀的宠物宝珠 (冰属性强化)')"
    if mode == 0:
        char.冰属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20555(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '灿烂的宠物宝珠 (冰属性强化)')"
    if mode == 0:
        char.冰属性强化加成(10 * rate)
    if mode == 1:
        pass


def enchanting_20556(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '哥特风披肩 ')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20557(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '哥特风洋装帽 ')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20558(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '武器, 上衣, 下装', '使徒卡恩')"
    if mode == 0:
        char.基础属性加成(力量=50 * rate)
        char.基础属性加成(物理攻击力=35 * rate)
        char.基础属性加成(智力=50 * rate)
        char.基础属性加成(魔法攻击力=35 * rate)
    if mode == 1:
        pass


def enchanting_20559(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(107, '称号', '黄龙之白玉')"
    if mode == 0:
        char.所有属性强化加成(3 * rate)
    if mode == 1:
        pass


def enchanting_20560(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '公爵尤里斯')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.05 * rate)
    if mode == 1:
        pass


def enchanting_20561(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '吟游诗人艾丽丝')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.09 * rate)
    if mode == 1:
        pass


def enchanting_20562(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '头肩', '魂 : 长枪麦斯')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.1 * rate)
    if mode == 1:
        pass


def enchanting_20563(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '凯恩')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.09 * rate)
    if mode == 1:
        pass


def enchanting_20564(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '头肩', '春联仙娥宝珠 - 雪莲')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
        char.基础属性加成(智力=75 * rate)
        char.基础属性加成(体力=75 * rate)
        char.基础属性加成(精神=75 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 30, 1)
    if mode == 1:
        pass


def enchanting_20565(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '称号', '春联仙娥宝珠 - 尔怜')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20566(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '无畏的女枪手宝珠')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20567(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩, 腰带, 鞋', '无畏的暗夜使者宝珠')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.07 * rate)
    if mode == 1:
        pass


def enchanting_20568(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '称号', '晴空夏影宝珠')"
    if mode == 0:
        char.所有属性强化加成(5 * rate)
    if mode == 1:
        pass


def enchanting_20569(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '晴空夏影宝珠')"
    if mode == 0:
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20570(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '晴空夏影宝珠')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20571(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '晴空夏影宝珠')"
    if mode == 0:
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20572(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(130, '称号', '晴空夏影宝珠')"
    if mode == 0:
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20573(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [武力][武力]')"
    if mode == 0:
        char.基础属性加成(力量=40 * rate)
    if mode == 1:
        pass


def enchanting_20574(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [武力][智慧]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(智力=20 * rate)
    if mode == 1:
        pass


def enchanting_20575(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [武力][活力]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(体力=20 * rate)
    if mode == 1:
        pass


def enchanting_20576(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [武力][冥想]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(精神=20 * rate)
    if mode == 1:
        pass


def enchanting_20577(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [武力][物理攻击]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20578(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [武力][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20579(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [武力][独立攻击]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20580(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [武力][鹰眼]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20581(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [武力][灵心]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20582(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [武力][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20583(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [武力][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20584(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [武力][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20585(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [武力][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(力量=20 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20586(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [智慧][智慧]')"
    if mode == 0:
        char.基础属性加成(智力=40 * rate)
    if mode == 1:
        pass


def enchanting_20587(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [智慧][活力]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(体力=20 * rate)
    if mode == 1:
        pass


def enchanting_20588(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [智慧][冥想]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(精神=20 * rate)
    if mode == 1:
        pass


def enchanting_20589(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [智慧][物理攻击]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20590(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [智慧][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20591(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [智慧][独立攻击]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20592(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [智慧][鹰眼]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20593(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [智慧][灵心]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20594(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [智慧][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20595(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [智慧][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20596(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [智慧][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20597(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [智慧][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(智力=20 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20598(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [活力][活力]')"
    if mode == 0:
        char.基础属性加成(体力=40 * rate)
    if mode == 1:
        pass


def enchanting_20599(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [活力][冥想]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(精神=20 * rate)
    if mode == 1:
        pass


def enchanting_20600(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [活力][物理攻击]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20601(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [活力][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20602(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [活力][独立攻击]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20603(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [活力][鹰眼]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20604(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [活力][灵心]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20605(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [活力][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20606(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [活力][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20607(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [活力][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20608(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [活力][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(体力=20 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20609(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [冥想][冥想]')"
    if mode == 0:
        char.基础属性加成(精神=40 * rate)
    if mode == 1:
        pass


def enchanting_20610(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [冥想][物理攻击]')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.基础属性加成(物理攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20611(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [冥想][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20612(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [冥想][独立攻击]')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20613(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [冥想][鹰眼]')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20614(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [冥想][灵心]')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20615(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [冥想][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20616(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [冥想][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20617(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [冥想][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20618(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [冥想][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(精神=20 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20619(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [物理攻击][物理攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20620(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [物理攻击][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.基础属性加成(魔法攻击力=15 * rate)
    if mode == 1:
        pass


def enchanting_20621(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [物理攻击][独立攻击]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20622(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [物理攻击][鹰眼]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20623(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [物理攻击][灵心]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20624(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [物理攻击][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20625(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [物理攻击][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20626(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [物理攻击][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20627(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [物理攻击][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理攻击力=15 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20628(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [魔法攻击][魔法攻击]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=30 * rate)
    if mode == 1:
        pass


def enchanting_20629(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [魔法攻击][独立攻击]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.基础属性加成(独立攻击力=25 * rate)
    if mode == 1:
        pass


def enchanting_20630(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [魔法攻击][鹰眼]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20631(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [魔法攻击][灵心]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20632(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [魔法攻击][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20633(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [魔法攻击][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20634(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [魔法攻击][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20635(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [魔法攻击][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法攻击力=15 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20636(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(159, '宠物', '和氏之璧宝珠 [独立攻击][独立攻击]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=50 * rate)
    if mode == 1:
        pass


def enchanting_20637(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [独立攻击][鹰眼]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.基础属性加成(物理暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20638(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [独立攻击][灵心]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20639(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [独立攻击][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20640(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [独立攻击][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20641(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [独立攻击][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20642(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [独立攻击][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(独立攻击力=25 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20643(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [鹰眼][鹰眼]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20644(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [鹰眼][灵心]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.基础属性加成(魔法暴击率=0.03 * rate)
    if mode == 1:
        pass


def enchanting_20645(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [鹰眼][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20646(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [鹰眼][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20647(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [鹰眼][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20648(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [鹰眼][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.03 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20649(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(139, '宠物', '和氏之璧宝珠 [灵心][灵心]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20650(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [灵心][火属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.火属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20651(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [灵心][冰属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20652(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [灵心][暗属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20653(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [灵心][光属性增幅]')"
    if mode == 0:
        char.基础属性加成(魔法暴击率=0.03 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20654(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '和氏之璧宝珠 [火属性增幅][火属性增幅]')"
    if mode == 0:
        char.火属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20655(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [火属性增幅][冰属性增幅]')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
        char.冰属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20656(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [火属性增幅][暗属性增幅]')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20657(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [火属性增幅][光属性增幅]')"
    if mode == 0:
        char.火属性强化加成(7 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20658(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '和氏之璧宝珠 [冰属性增幅][冰属性增幅]')"
    if mode == 0:
        char.冰属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20659(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [冰属性增幅][暗属性增幅]')"
    if mode == 0:
        char.冰属性强化加成(7 * rate)
        char.暗属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20660(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [冰属性增幅][光属性增幅]')"
    if mode == 0:
        char.冰属性强化加成(7 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20661(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '和氏之璧宝珠 [暗属性增幅][暗属性增幅]')"
    if mode == 0:
        char.暗属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20662(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(148, '宠物', '和氏之璧宝珠 [暗属性增幅][光属性增幅]')"
    if mode == 0:
        char.暗属性强化加成(7 * rate)
        char.光属性强化加成(7 * rate)
    if mode == 1:
        pass


def enchanting_20663(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(170, '宠物', '和氏之璧宝珠 [光属性增幅][光属性增幅]')"
    if mode == 0:
        char.光属性强化加成(14 * rate)
    if mode == 1:
        pass


def enchanting_20664(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '称号', '卧龙诸葛宝珠')"
    if mode == 0:
        char.所有属性强化加成(15 * rate)
        char.基础属性加成(物理攻击力=20 * rate)
        char.基础属性加成(魔法攻击力=20 * rate)
        char.基础属性加成(独立攻击力=30 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20665(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(153, '头肩', '凤雏庞统宝珠')"
    if mode == 0:
        char.基础属性加成(力量=75 * rate)
        char.基础属性加成(智力=75 * rate)
        char.基础属性加成(体力=75 * rate)
        char.基础属性加成(精神=75 * rate)
        char.基础属性加成(物理暴击率=0.05 * rate)
        char.基础属性加成(魔法暴击率=0.05 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 30, 1)
    if mode == 1:
        pass


def enchanting_20666(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '莉兹贝特 (SAO)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20667(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '头肩', '莉兹贝特 (ALO)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20668(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带', '莉法 (SAO)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


def enchanting_20669(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(106, '腰带', '莉法 (ALO)')"
    if mode == 0:
        char.基础属性加成(物理暴击率=0.06 * rate)
        char.基础属性加成(魔法暴击率=0.06 * rate)
    if mode == 1:
        pass


#  国服特色
def enchanting_20670(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带，鞋', '三攻 +36 技攻 +3%')"
    if mode == 0:
        char.基础属性加成(三攻=36 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_20671(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '腰带，鞋', '三攻 +36 Lv1~50 主动+1')"
    if mode == 0:
        char.基础属性加成(三攻=36 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


def enchanting_20672(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '不稳定的裂缝[全 +33]')"
    if mode == 0:
        char.所有属性强化加成(33 * rate)
    if mode == 1:
        pass


def enchanting_20673(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '魔渊漫步者[冰/暗 +35]')"
    if mode == 0:
        char.冰属性强化加成(35 * rate)
        char.暗属性强化加成(35 * rate)
    if mode == 1:
        pass


def enchanting_20674(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(147, '项链，手镯，戒指', '破坏之王后[火/光 +35]')"
    if mode == 0:
        char.火属性强化加成(35 * rate)
        char.光属性强化加成(35 * rate)
    if mode == 1:
        pass


def enchanting_20675(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '辅助装备', '全属强 +12 暴击 +3% 最终 +3% 攻击强化 +3%')"
    if mode == 0:
        char.所有属性强化加成(12 * rate)
        char.最终伤害加成(0.03 * rate)
        char.百分比攻击强化加成(0.03 * rate)
        char.暴击率增加(0.03)
    if mode == 1:
        pass


def enchanting_20676(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(158, '魔法石', '复仇之混沌恶神奥兹玛[全 +30]')"
    if mode == 0:
        char.所有属性强化加成(30 * rate)
    if mode == 1:
        pass


def enchanting_20677(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '力智 +75 三攻 +20 技攻 +3%')"
    if mode == 0:
        char.三攻固定加成(20 * rate)
        char.力智固定加成(75 * rate)
        char.技能攻击力加成(0.03 * rate)
    if mode == 1:
        pass


def enchanting_20678(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(168, '头肩', '力智 +75 三攻 +20  Lv1~50 主动+1')"
    if mode == 0:
        char.三攻固定加成(20 * rate)
        char.力智固定加成(75 * rate)
        if rate == 1:
            char.技能等级加成('主动', 1, 50, 1)
    if mode == 1:
        pass


# endregion

# region 光环 21001~21500


def enchanting_21001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1 5%三攻')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.百分比三攻加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass


def enchanting_21002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1 5%黄字')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.伤害增加加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass


def enchanting_21003(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '光环', 'Lv1~80+1 5%暴伤')"
    if mode == 0:
        char.技能等级加成('所有', 1, 80, 1)
        char.暴击伤害加成(0.05)
        char.百分比攻击强化加成(0.05)
        pass
    if mode == 1:
        pass
# endregion

# region 武器装扮 21501~22000


def enchanting_21501(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '40级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(40, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21502(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '45级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(45, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21503(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '60级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(60, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21504(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '70级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(70, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21505(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '75级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(75, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21506(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '80级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(80, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass


def enchanting_21506(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '武器装扮', '80级技能 Lv+1')"
    if mode == 0:
        char.武器装扮等级加成(80, 1)
        char.力智固定加成(55)
        char.体精固定加成(55)
    if mode == 1:
        pass

# endregion

# region 皮肤 22001~22500


def enchanting_22001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '皮肤', '全属强 +5')"
    if mode == 0:
        char.所有属性强化加成(5)
        pass
    if mode == 1:
        pass


def enchanting_22002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '皮肤', '全属强 +6')"
    if mode == 0:
        char.所有属性强化加成(6)
        pass
    if mode == 1:
        pass

# endregion

# region 宠物装备-红 22501~23000


def enchanting_22501(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '三攻 +8% 攻击强化 +8%')"
    if mode == 0:
        char.百分比三攻加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass


def enchanting_22502(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '力智 +8% 攻击强化 +8%')"
    if mode == 0:
        char.百分比力智加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass


def enchanting_22503(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '最终 +8% 攻击强化 +8%')"
    if mode == 0:
        char.最终伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass


def enchanting_22504(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-红', '附加伤害 +8% 攻击强化 +8%')"
    if mode == 0:
        char.附加伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass
    if mode == 1:
        pass
# endregion

# region 宠物装备-绿 23001~23500


def enchanting_23001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-绿', '三攻 +40 属强 +20')"
    if mode == 0:
        char.三攻固定加成(40)
        char.所有属性强化加成(20)
        pass
    if mode == 1:
        pass

# endregion

# region 宠物装备-蓝 23501~24000


def enchanting_23501(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '宠物装备-蓝', '三攻 +30')"
    if mode == 0:
        char.三攻固定加成(30)
        pass
    if mode == 1:
        pass

# endregion

# region 快捷装备 24001~24999


def enchanting_24001(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '快捷装备', '三攻 +30 附加伤害 +8% 攻击强化 +8%')"
    if mode == 0:
        pass
    if mode == 1:
        char.三攻固定加成(30)
        char.附加伤害加成(0.08)
        char.百分比攻击强化加成(0.08)
        pass


def enchanting_24002(char: Character = {}, mode=0, text=False, rate=1.0):
    if text:
        return "(0, '快捷装备', '四维 +8 附加伤害 +8% 攻击强化 +8%')"
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
