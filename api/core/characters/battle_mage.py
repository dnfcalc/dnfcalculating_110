from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能

# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型, 输出类型):
#         if 武器类型 == '矛':
#             return round(self.CDR / self.恢复 * 1.05, 1)
#         if 武器类型 == '棍棒':
#             return round(self.CDR / self.恢复 * 0.95, 1)


class 技能0(主动技能):
    名称 = '基本攻击'
    备注 = '(一轮,TP为基础精通)'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    data0 = [0, 152+182+274]
    # 基础 = 225.2*2.662/1.115*1.1
    # 基础2 = 1.16 * 225.2*2.662/1.115*1.1
    # 基础3 = 1.8 * 225.2*2.662/1.115*1.1
    形态 = ['普通', '变身']
    CD = 1
    TP成长 = 0.10
    TP上限 = 3

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "普通":
            self.data0 = [0, 152+182+274]
        if 形态 == "变身":
            self.data0 = [0, 149+177+267]


class 技能1(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    学习间隔 = 1
    等级精通 = 110
    关联技能 = ['基本攻击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class 技能2(被动技能):
    名称 = '尼巫的战斗术'
    所在等级 = 15
    等级上限 = 11
    等级精通 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级, 3)


class 技能3(被动技能):
    名称 = '炫纹'
    所在等级 = 15
    等级上限 = 60
    等级间隔 = 2
    等级精通 = 50

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.20+0.00*self.等级, 3)


class 技能4(被动技能):
    名称 = '矛精通'
    所在等级 = 20
    等级上限 = 30
    等级间隔 = 3
    等级精通 = 20
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['星纹陨爆', '一骑当千碎霸', '太古星河·殒灭']

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.05

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '矛':
            return 1.0
        if self.等级 <= 20:
            return round(1.00+0.01*self.等级, 3)
        if self.等级 > 20:
            return round(0.80+0.02*self.等级, 3)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '矛':
            return 1.0
        if self.等级 <= 20:
            return round(1.00+0.01*self.等级, 3)
        if self.等级 > 20:
            return round(0.80+0.02*self.等级, 3)


class 技能5(被动技能):
    名称 = '棍棒精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    学习间隔 = 3
    等级精通 = 20
    冷却关联技能 = ['所有']
    非冷却关联技能 = ['星纹陨爆', '一骑当千碎霸', '太古星河·殒灭']

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '棍棒':
            return 1.0
        if self.等级 <= 20:
            return round(1.00+0.01*self.等级, 3)
        if self.等级 > 20:
            return round(0.80+0.02*self.等级, 3)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '棍棒':
            return 1.0
        if self.等级 <= 20:
            return round(1.00+0.01*self.等级, 3)
        if self.等级 > 20:
            return round(0.80+0.02*self.等级, 3)


class 技能6(主动技能):
    名称 = '炫纹发射'
    备注 = '(个数,TP为强化炫纹)'
    是否主动 = 0
    所在等级 = 15
    等级上限 = 70
    等级间隔 = 2
    等级精通 = 60

    data0 = [0, 281, 309, 340, 367, 397, 424, 452, 480, 508, 539, 568, 595, 624, 652, 681, 710, 740, 768, 795, 825, 852, 881, 909, 937, 969, 996, 1023, 1053, 1080, 1109, 1137, 1167, 1197, 1224, 1254, 1282,
             1311, 1338, 1370, 1397, 1425, 1453, 1482, 1509, 1537, 1567, 1596, 1625, 1654, 1682, 1711, 1739, 1765, 1798, 1825, 1853, 1882, 1910, 1937, 1968, 1995, 2026, 2054, 2082, 2109, 2139, 2168, 2194, 2227, 2253]
    MP = [12, 140]
    # 95被动,默认超大炫纹,倍率*1.5
    倍率 = 1.5

    CD = 0.25
    TP成长 = 0.10
    TP上限 = 1


class 技能7(主动技能):
    名称 = '双重锤击'
    所在等级 = 20
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    # 第一击物理攻击力：<data0>%10.6
    data0 = [0, 538, 593, 652, 708, 761, 816, 872, 928, 984, 1039, 1092, 1147, 1207, 1262, 1317, 1378, 1434, 1488, 1543, 1600, 1654, 1710, 1766, 1820, 1874, 1933, 1989, 2043, 2099, 2156, 2210, 2264, 2319, 2375, 2433,
             2489, 2545, 2598, 2653, 2711, 2765, 2821, 2878, 2928, 2992, 3046, 3101, 3159, 3215, 3271, 3325, 3382, 3437, 3491, 3547, 3605, 3658, 3716, 3770, 3826, 3880, 3937, 3993, 4047, 4100, 4160, 4214, 4270, 4326, 4380]
    hit0 = 1.0
    # 最后一击物理攻击力：<data1>%
    data1 = [0, 1976, 2183, 2383, 2588, 2793, 2998, 3202, 3408, 3608, 3814, 4020, 4224, 4426, 4632, 4835, 5042, 5247, 5445, 5653, 5858, 6061, 6269, 6470, 6672, 6879, 7084, 7289, 7491, 7697, 7898, 8106, 8309, 8513, 8718, 8921, 9129, 9335,
             9533, 9738, 9944, 10150, 10356, 10555, 10759, 10968, 11172, 11371, 11577, 11781, 11989, 12194, 12393, 12598, 12805, 13012, 13215, 13414, 13621, 13826, 14031, 14239, 14435, 14642, 14851, 15052, 15258, 15460, 15665, 15868, 16077]
    hit1 = 1.0
    # 冲击波独立物理攻击力：<data2>%
    data2 = [0, 1510, 1663, 1820, 1976, 2132, 2289, 2442, 2598, 2755, 2916, 3069, 3227, 3382, 3535, 3693, 3847, 4004, 4160, 4315, 4470, 4626, 4788, 4941, 5101, 5254, 5408, 5564, 5718, 5880, 6033, 6184, 6345, 6497, 6660, 6815,
             6966, 7125, 7279, 7435, 7591, 7751, 7903, 8059, 8216, 8366, 8532, 8686, 8836, 8998, 9152, 9309, 9464, 9623, 9771, 9930, 10089, 10242, 10405, 10558, 10708, 10871, 11024, 11178, 11335, 11488, 11648, 11801, 11960, 12114, 12276]
    hit2 = 1.0
    CD = 8
    TP成长 = 0.10
    TP上限 = 7

    MP = [60, 546]


class 技能8(主动技能):
    名称 = '炫纹爆弹'
    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    # 直刺5.97
    data0 = [0, 1379, 1526, 1663, 1811, 1964, 2095, 2250, 2389, 2532, 2673, 2815, 2956, 3104, 3239, 3387, 3528, 3670, 3810, 3951, 4095, 4246, 4379, 4531, 4683, 4814, 4969, 5110, 5251, 5392, 5534, 5677, 5823, 5958, 6105, 6247,
             6390, 6531, 6674, 6814, 6968, 7098, 7252, 7400, 7534, 7680, 7817, 7965, 8107, 8248, 8388, 8530, 8672, 8825, 8965, 9109, 9251, 9393, 9534, 9689, 9829, 9971, 10112, 10256, 10395, 10536, 10683, 10826, 10967, 11110, 11249]
    hit0 = 1.0
    # 多段
    data1 = [0, 172, 187, 205, 224, 248, 265, 282, 296, 319, 331, 348, 378, 390, 405, 412, 442, 461, 472, 502, 506, 532, 549, 567, 584, 604, 627, 631, 661, 672, 691, 718, 727, 743, 754, 783, 802,
             814, 838, 847, 866, 884, 909, 926, 944, 963, 974, 1002, 1009, 1028, 1056, 1069, 1084, 1103, 1121, 1144, 1163, 1169, 1192, 1211, 1226, 1245, 1264, 1286, 1304, 1321, 1340, 1351, 1369, 1386, 1405]
    hit1 = 13.0
    # 爆炸
    data2 = [0, 4153, 4579, 5003, 5440, 5868, 6296, 6721, 7157, 7586, 8006, 8438, 8873, 9298, 9734, 10158, 10589, 11027, 11441, 11876, 12299, 12730, 13158, 13593, 14031, 14454, 14878, 15309, 15745, 16161, 16596, 17027, 17450, 17886, 18313, 18750,
             19180, 19598, 20028, 20455, 20892, 21316, 21746, 22182, 22608, 23032, 23458, 23900, 24317, 24748, 25183, 25612, 26043, 26466, 26890, 27328, 27752, 28187, 28614, 29045, 29468, 29903, 30332, 30763, 31185, 31621, 32045, 32484, 32908, 33334, 33762]
    hit2 = 1.0
    # 演出时间 = 12.0
    CD = 12
    TP成长 = 0.10
    TP上限 = 7

    MP = [60, 546]


class 技能9(主动技能):
    名称 = '碎霸'
    所在等级 = 30
    学习间隔 = 2
    等级精通 = 60
    等级上限 = 70
    data0 = [0, 4686, 5169, 5657, 6140, 6623, 7104, 7589, 8077, 8562, 9045, 9531, 10016, 10502, 10986, 11472, 11952, 12438, 12921, 13406, 13894, 14377, 14862, 15347, 15833, 16320, 16799, 17281, 17769, 18252, 18738, 19223, 19708, 20194, 20679, 21160,
             21643, 22128, 22615, 23101, 23584, 24069, 24557, 25039, 25525, 26006, 26489, 26977, 27459, 27945, 28432, 28916, 29401, 29884, 30373, 30851, 31338, 31820, 32306, 32792, 33277, 33764, 34247, 34733, 35213, 35697, 36183, 36667, 37154, 37637, 38123]

    CD = 8
    基础释放次数 = 0
    TP成长 = 0.10
    TP上限 = 7

    MP = [60, 546]


class 技能10(主动技能):
    名称 = '炫纹融合'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 327, 358, 392, 424, 458, 491, 522, 558, 589, 624, 656, 691, 722, 754, 789, 820, 855, 887, 922, 953, 989, 1020, 1051, 1087, 1118, 1153, 1185, 1220, 1251, 1285, 1318, 1350, 1384, 1416, 1451, 1482,
             1516, 1549, 1583, 1616, 1648, 1682, 1713, 1747, 1780, 1814, 1847, 1881, 1913, 1946, 1979, 2011, 2045, 2078, 2112, 2144, 2178, 2211, 2244, 2276, 2310, 2343, 2376, 2410, 2442, 2476, 2508, 2541, 2574, 2608]
    hit0 = 15
    data1 = [0, 4891, 5386, 5883, 6378, 6875, 7370, 7867, 8362, 8857, 9357, 9852, 10348, 10843, 11340, 11837, 12332, 12829, 13324, 13819, 14316, 14813, 15308, 15804, 16300, 16798, 17294, 17789, 18286, 18783, 19278, 19775, 20270, 20765, 21262, 21759,
             22254, 22750, 23246, 23745, 24240, 24735, 25232, 25727, 26224, 26719, 27216, 27711, 28207, 28705, 29200, 29696, 30192, 30691, 31186, 31681, 32178, 32673, 33170, 33665, 34162, 34658, 35153, 35651, 36146, 36643, 37138, 37635, 38132, 38627, 39124]
    hit1 = 0

    形态 = ['旋转', '爆炸']

    CD = 8
    TP成长 = 0.10
    TP上限 = 7

    MP = [25, 210]

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == '旋转':
            self.hit0 = 15
            self.hit1 = 0
        if 形态 == '爆炸':
            self.hit0 = 0
            self.hit1 = 1


class 技能11(主动技能):
    名称 = '流星闪影击'
    所在等级 = 35
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2
    data0 = [0, 10796, 11892, 12988, 14083, 15178, 16277, 17367, 18468, 19565, 20653, 21749, 22847, 23943, 25035, 26134, 27223, 28321, 29414, 30513, 31611, 32706, 33799, 34895, 35992, 37089, 38185, 39272, 40371, 41469, 42563, 43660, 44756, 45848, 46944,
             48035, 49134, 50231, 51326, 52415, 53516, 54612, 55707, 56806, 57899, 58992, 60089, 61185, 62280, 63373, 64469, 65564, 66659, 67757, 68853, 69949, 71038, 72134, 73233, 74327, 75426, 76518, 77613, 78709, 79806, 80901, 81996, 83092, 84184, 85280, 86375]
    data1 = [0, 80, 88, 94, 99, 106, 115, 127, 133, 145, 148, 155, 164, 173, 179, 192, 193, 201, 214, 221, 231, 238, 242, 252, 260, 264, 280, 281, 289, 301, 305, 319, 323, 326, 340,
             347, 352, 364, 371, 373, 385, 392, 403, 411, 418, 425, 432, 439, 450, 459, 461, 471, 480, 489, 496, 505, 512, 520, 526, 536, 544, 554, 556, 565, 573, 583, 593, 601, 604, 612, 622]
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

    形态 = ['打满', '秒C']

    def TP加成(self):
        return 1

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "打满":
            self.hit0 = 1
            self.hit1 = 15
            self.hit1 += self.TP等级
            self.power0 = 1 + self.TP成长 * self.TP等级
        if 形态 == "秒C":
            self.hit0 = 1
            self.hit1 = 0
            self.power0 = 1 + self.TP成长 * self.TP等级

    MP = [180, 1512]
    无色消耗 = 1


class 技能12(主动技能):
    名称 = '炫纹强压'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 10296, 11341, 12385, 13430, 14475, 15520, 16563, 17608, 18653, 19698, 20742, 21786, 22831, 23875, 24920, 25965, 27010, 28053, 29098, 30143, 31188, 32231, 33276, 34321, 35365, 36410, 37455, 38499, 39543, 40588, 41633, 42678, 43721, 44766,
             45811, 46855, 47901, 48946, 49991, 51034, 52079, 53124, 54169, 55212, 56257, 57302, 58346, 59391, 60436, 61482, 62525, 63570, 64615, 65660, 66704, 67748, 68793, 69837, 70882, 71927, 72972, 74015, 75060, 76105, 77150, 78193, 79238, 80284, 81328, 82373]
    CD = 17
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [300, 1260]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.31
        self.CDR *= 0.92


class 技能13(主动技能):
    名称 = '强袭流星打'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [0, 12387, 13671, 14954, 16227, 17508, 18794, 20076, 21359, 22638, 23926, 25203, 26474, 27765, 29044, 30331, 31605, 32881, 34169, 35450, 36727, 38015, 39290, 40579, 41853, 43134, 44424, 45702, 46976, 48262, 49539, 50828, 52109, 53382, 54671,
             55948, 57237, 58511, 59792, 61081, 62356, 63628, 64917, 66196, 67486, 68758, 70040, 71330, 72605, 73885, 75168, 76445, 77733, 79011, 80291, 81577, 82858, 84133, 85417, 86699, 87987, 89265, 90536, 91822, 93108, 94389, 95664, 96948, 98232, 99514, 100792]
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [160, 1344]
    无色消耗 = 1

    def 装备护石(self):
        self.倍率 *= 1.05*1.22


class 技能14(主动技能):
    名称 = '煌龙偃月'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    # 普通龙刀
    data0 = [0, 4939, 5447, 5964, 6471, 6983, 7492, 8004, 8511, 9029, 9537, 10047, 10559, 11067, 11579, 12094, 12603, 13116, 13623, 14133, 14645, 15157, 15666, 16180, 16689, 17198, 17713, 18222, 18732, 19246, 19756, 20260, 20779, 21286, 21796, 22309,
             22817, 23326, 23845, 24353, 24862, 25372, 25883, 26391, 26905, 27417, 27931, 28438, 28947, 29462, 29970, 30482, 30995, 31504, 32012, 32528, 33037, 33545, 34059, 34565, 35075, 35593, 36101, 36610, 37122, 37634, 38140, 38660, 39168, 39673, 40187]
    hit0 = 1
    data1 = [0, 1648, 1816, 1990, 2161, 2330, 2497, 2667, 2837, 3010, 3181, 3349, 3519, 3689, 3861, 4030, 4202, 4373, 4542, 4712, 4886, 5055, 5224, 5394, 5563, 5731, 5906, 6076, 6244, 6413, 6587, 6756, 6927, 7097, 7265, 7437, 7606,
             7776, 7948, 8120, 8288, 8457, 8628, 8797, 8969, 9140, 9309, 9479, 9647, 9822, 9996, 10162, 10331, 10502, 10671, 10843, 11014, 11183, 11352, 11522, 11692, 11864, 12035, 12204, 12375, 12546, 12713, 12888, 13057, 13228, 13396]
    hit1 = 7
    power1 = 1
    data2 = [0, 7064, 7790, 8524, 9256, 9982, 10716, 11447, 12172, 12908, 13638, 14364, 15102, 15830, 16553, 17289, 18020, 18750, 19479, 20211, 20941, 21671, 22400, 23136, 23866, 24590, 25327, 26055, 26781, 27519, 28248, 28973, 29710, 30439, 31163, 31899,
             32628, 33355, 34096, 34821, 35550, 36288, 37011, 37740, 38476, 39203, 39939, 40666, 41394, 42131, 42858, 43586, 44325, 45050, 45780, 46515, 47242, 47972, 48706, 49434, 50163, 50893, 51623, 52354, 53083, 53815, 54543, 55275, 56002, 56734, 57470]
    hit2 = 1
    power2 = 1

    # 被动形态
    data3 = [0, 1678, 1849, 2019, 2190, 2359, 2531, 2701, 2871, 3042, 3211, 3382, 3552, 3723, 3892, 4064, 4233, 4404, 4575, 4745, 4916, 5085, 5256, 5426, 5597, 5766, 5938, 6107, 6278, 6449, 6619, 6788, 6960, 7130, 7299, 7471, 7640,
             7811, 7981, 8152, 8323, 8493, 8662, 8835, 9004, 9173, 9345, 9514, 9685, 9855, 10026, 10195, 10367, 10537, 10707, 10878, 11048, 11218, 11388, 11559, 11729, 11900, 12069, 12241, 12411, 12581, 12752, 12922, 13092, 13262, 13433]
    hit3 = 0
    power3 = 1
    data4 = [0, 12594, 13871, 15147, 16426, 17704, 18982, 20259, 21537, 22814, 24091, 25369, 26646, 27926, 29203, 30481, 31758, 33035, 34313, 35590, 36868, 38146, 39425, 40701, 41980, 43257, 44533, 45812, 47088, 48367, 49645, 50923, 52200, 53477, 54755,
             56032, 57310, 58587, 59867, 61144, 62422, 63699, 64976, 66254, 67531, 68809, 70087, 71366, 72642, 73919, 75198, 76474, 77753, 79030, 80308, 81586, 82864, 84141, 85418, 86696, 87973, 89251, 90528, 91808, 93085, 94362, 95640, 96917, 98195, 99472, 100750]
    hit4 = 0
    power4 = 1

    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [360, 3024]
    无色消耗 = 2

    def 形态变更(self, 形态, char: Character):
        if char.get_skill_by_name("煌龙乱舞").等级 > 0:
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 0
            self.hit3 = 5
            self.hit4 = 1
            if '煌龙偃月' in char.护石栏:
                self.hit3 += 1
                self.power3 = 1.14
                self.power4 = 1.18
        else:
            self.hit0 = 1
            self.hit1 = 7
            self.hit2 = 1
            self.hit3 = 0
            self.hit4 = 0
            if '煌龙偃月' in char.护石栏:
                self.hit1 += 3
                self.power2 = 1.36

    def 装备护石(self):
        pass


class 技能15(被动技能):
    名称 = '煌龙乱舞'
    所在等级 = 45
    等级上限 = 1
    学习间隔 = 2
    等级精通 = 1


class 技能16(被动技能):
    名称 = '斗神意志'
    所在等级 = 48
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05+0.02*self.等级, 3)


class 技能17(主动技能):
    名称 = '星纹陨爆'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [0, 65335, 80484, 95633, 110783, 125934, 141084, 156234, 171385, 186534, 201684, 216835, 231985, 247135, 262284, 277434, 292584, 307734, 322885, 338035, 353185, 368336, 383485, 398634, 413784, 428936, 444085, 459235, 474386, 489535, 504685, 519836, 534986, 550136, 565286, 580435,
             595585, 610735, 625886, 641036, 656186, 671337, 686486, 701636, 716785, 731937, 747086, 762236, 777388, 792536, 807686, 822837, 837987, 853137, 868287, 883436, 898586, 913736, 928887, 944037, 959187, 974337, 989487, 1004637, 1019786, 1034938, 1050088, 1065237, 1080389, 1095537, 1110687]
    CD = 145.0

    无色消耗 = 7
    MP = [1500, 3500]


class 技能18(主动技能):
    名称 = '闪击碎霸'
    所在等级 = 60
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [0, 19548, 21530, 23512, 25496, 27481, 29468, 31446, 33431, 35413, 37397, 39378, 41363, 43346, 45330, 47311, 49296, 51282, 53263, 55246, 57229, 59213, 61197, 63175, 65161, 67148, 69124, 71108, 73096, 75078, 77058, 79041, 81026, 83009, 84990, 86973, 88961,
             90942, 92923, 94908, 96894, 98875, 100858, 102840, 104824, 106810, 108788, 110773, 112758, 114736, 116721, 118708, 120692, 122672, 124652, 126636, 128625, 130600, 132587, 134570, 136557, 138535, 140521, 142502, 144489, 146471, 148452, 150437, 152422, 154402, 156382]
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [400, 1120]
    无色消耗 = 2

    def 装备护石(self):
        self.倍率 *= 1.24
        self.CDR *= 0.90


class 技能19(主动技能):
    名称 = '流星雷连击'
    所在等级 = 70
    等级上限 = 50
    等级间隔 = 2
    等级精通 = 40
    data0 = [0, 32250, 35517, 38788, 42056, 45330, 48596, 51867, 55136, 58405, 61675, 64947, 68215, 71485, 74753, 78024, 81293, 84564, 87833, 91104, 94372, 97644, 100909, 104181, 107452, 110718, 113989, 117257, 120527, 123798, 127067, 130338, 133609, 136875, 140146, 143414, 146684,
             149956, 153226, 156495, 159766, 163032, 166306, 169569, 172841, 176112, 179381, 182651, 185919, 189189, 192460, 195729, 198999, 202269, 205537, 208808, 212074, 215348, 218617, 221885, 225154, 228426, 231694, 234966, 238231, 241503, 244773, 248042, 251311, 254583, 257853]
    data1 = [0, 235, 253, 270, 287, 301, 316, 333, 350, 364, 383, 397, 413, 426, 445, 460, 475, 494, 508, 526, 541, 558, 571, 587, 607, 619, 636, 653, 670, 684, 699, 719, 731, 748, 763, 782, 796,
             812, 829, 846, 861, 874, 892, 906, 924, 940, 956, 972, 990, 1004, 1018, 1035, 1053, 1067, 1084, 1100, 1117, 1128, 1149, 1166, 1180, 1194, 1212, 1228, 1245, 1260, 1278, 1291, 1307, 1323, 1340]
    power1 = 1
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    MP = [800, 1680]
    无色消耗 = 3

    形态 = ['打满', '秒C']

    def 形态变更(self, 形态, char: Character):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "打满":
            self.hit0 = 1
            self.hit1 = 15
            if '流星雷连击' in char.护石栏:
                self.hit1 += 7
                self.power1 = 1.22
                self.power0 = 1.19
        if 形态 == "秒C":
            self.hit0 = 1
            self.hit1 = 0
            if '流星雷连击' in char.护石栏:
                self.power0 = 1.19

    def 装备护石(self):
        pass


class 技能20(被动技能):
    名称 = '战灵潜能'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22+0.02*self.等级, 3)


class 技能22(主动技能):
    名称 = '炫纹簇'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [0, 6863, 7559, 8256, 8953, 9649, 10346, 11042, 11738, 12434, 13132, 13827, 14523, 15218, 15914, 16610, 17308, 18004, 18701, 19397, 20093, 20789, 21487, 22183, 22879, 23576, 24272, 24968, 25666, 26361, 27057, 27753, 28449, 29146, 29843, 30539,
             31236, 31932, 32628, 33324, 34021, 34718, 35414, 36109, 36806, 37502, 38198, 38894, 39590, 40287, 40983, 41679, 42375, 43073, 43769, 44466, 45162, 45858, 46554, 47252, 47948, 48644, 49341, 50037, 50733, 51431, 52126, 52822, 53518, 54214, 54911]
    hit0 = 7.0
    CD = 45
    是否有护石 = 1

    无色消耗 = 5
    MP = [360, 3024]

    def 装备护石(self):
        self.hit0 = 1
        self.倍率 *= 1+6.95+1.25


class 技能21(主动技能):
    名称 = '使徒之舞'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [0, 2016, 2219, 2425, 2630, 2836, 3040, 3246, 3448, 3653, 3857, 4064, 4265, 4471, 4675, 4882, 5086, 5290, 5494, 5698, 5904, 6108, 6315, 6518, 6719, 6925, 7130, 7339, 7540, 7744, 7950, 8154, 8360, 8565, 8768, 8972, 9176, 9383,
             9587, 9789, 9993, 10199, 10404, 10610, 10815, 11019, 11222, 11428, 11633, 11839, 12042, 12244, 12451, 12656, 12858, 13062, 13268, 13472, 13676, 13885, 14087, 14292, 14496, 14701, 14907, 15111, 15312, 15521, 15722, 15928, 16132]
    hit0 = 3
    data1 = [0, 4034, 4443, 4852, 5261, 5669, 6079, 6487, 6897, 7307, 7718, 8125, 8534, 8941, 9351, 9759, 10171, 10579, 10990, 11400, 11808, 12215, 12625, 13034, 13444, 13854, 14262, 14672, 15079, 15489, 15900, 16307, 16716, 17128, 17537, 17944,
             18355, 18761, 19172, 19582, 19991, 20401, 20810, 21216, 21626, 22037, 22446, 22855, 23264, 23675, 24083, 24492, 24900, 25310, 25718, 26129, 26536, 26949, 27357, 27764, 28175, 28583, 28994, 29401, 29811, 30219, 30629, 31036, 31447, 31857, 32267]
    hit1 = 1
    power1 = 1
    data2 = [0, 40344, 44431, 48517, 52602, 56688, 60794, 64880, 68965, 73070, 77175, 81244, 85348, 89415, 93521, 97605, 101711, 105799, 109901, 113988, 118075, 122161, 126246, 130352, 134438, 138542, 142630, 146714, 150802, 154887, 158992, 163077, 167164, 171269, 175374, 179441,
             183545, 187613, 191719, 195823, 199908, 203995, 208100, 212168, 216273, 220376, 224446, 228568, 232636, 236739, 240826, 244913, 249000, 253104, 257170, 261295, 265363, 269467, 273573, 277639, 281744, 285830, 289937, 294020, 298106, 302194, 306298, 310366, 314470, 318576, 322661]
    hit2 = 1
    power2 = 1
    CD = 40
    是否有护石 = 1

    MP = [384, 3255]
    无色消耗 = 5

    def 装备护石(self):
        # self.倍率 *= 1.36801
        self.hit1 = 0
        self.power2 *= 0.13*10*1.2


class 技能22(主动技能):
    名称 = '一骑当千碎霸'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [0, 64860, 79898, 94938, 109979, 125017, 140055, 155098, 170137, 185178, 200218, 215260, 230298, 245339, 260373, 275413, 290453, 305495, 320535, 335578, 350618, 365655, 380695, 395735, 410777, 425815, 440854, 455893, 470933, 485971, 501014, 516053, 531094, 546133, 561172, 576213,
             591253, 606293, 621333, 636369, 651408, 666449, 681492, 696531, 711571, 726611, 741651, 756693, 771730, 786769, 801809, 816847, 831886, 846929, 861969, 877010, 892050, 907086, 922126, 937168, 952206, 967247, 982285, 997327, 1012365, 1027408, 1042446, 1057486, 1072527, 1087567, 1102606]
    hit0 = 1.0
    data1 = [0, 43240, 53267, 63293, 73320, 83348, 93373, 103396, 113424, 123451, 133477, 143504, 153528, 163558, 173584, 183610, 193638, 203664, 213694, 223718, 233743, 243770, 253797, 263823, 273851, 283874, 293904, 303930, 313957, 323982, 334008, 344036, 354061, 364091, 374113, 384140,
             394169, 404193, 414221, 424249, 434275, 444303, 454327, 464355, 474382, 484408, 494434, 504459, 514484, 524512, 534538, 544567, 554592, 564619, 574647, 584673, 594702, 604726, 614754, 624782, 634803, 644830, 654857, 664885, 674912, 684937, 694962, 704990, 715017, 725044, 735072]
    hit1 = 1.0
    CD = 180

    MP = [2500, 8000]
    无色消耗 = 10


class 技能23(主动技能):
    名称 = '炫纹之源：太古神光'
    所在等级 = 95
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    data0 = [0, 119002, 131075, 143147, 155221, 167293, 179365, 191439, 203511, 215583, 227657, 239729, 251802, 263875, 275947, 288021, 300093, 312165, 324239, 336311, 348383, 360457, 372529, 384601, 396675, 408747, 420821, 432893, 444965, 457039, 469111, 481183, 493257, 505329, 517401,
             529475, 541547, 553619, 565693, 577765, 589839, 601911, 613983, 626057, 638129, 650201, 662275, 674347, 686419, 698493, 710565, 722638, 734711, 746783, 758857, 770929, 783001, 795075, 807147, 819219, 831293, 843365, 855438, 867511, 879583, 891656, 903729, 915801, 927875, 939947, 952019]

    CD = 60
    MP = [960, 7200]
    无色消耗 = 7

    def 等效百分比(self, **argv):
        # 额外计算10次炫纹
        char = argv.get('char', {})
        炫纹 = char.get_skill_by_name('炫纹发射').等效百分比()
        return super().等效百分比(**argv) + 炫纹 * 10


class 技能24(被动技能):
    名称 = '太古之力'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级, 3)


class 技能25(主动技能):
    名称 = '太古星河·殒灭'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    data0 = [0, 14839, 18279, 21721, 25161, 28602, 32043, 35483, 38925, 42365, 45807, 49247, 52689, 56129, 59571, 63011, 66451, 69893, 73333, 76775, 80215, 83657, 87097, 90539, 93979, 97420, 100861, 104302, 107743, 111184, 114625, 118066, 121507, 124947, 128388, 131829, 135270,
             138711, 142152, 145593, 149034, 152475, 155916, 159356, 162798, 166238, 169680, 173120, 176562, 180002, 183443, 186884, 190324, 193766, 197206, 200648, 204088, 207530, 210970, 214412, 217852, 221292, 224734, 228174, 231616, 235056, 238498, 241938, 245380, 248820, 252261]
    data1 = [0, 11871, 14623, 17376, 20128, 22881, 25635, 28387, 31140, 33892, 36645, 39397, 42150, 44904, 47656, 50409, 53161, 55914, 58666, 61420, 64173, 66925, 69678, 72430, 75183, 77935, 80689, 83442, 86194, 88947, 91699, 94452, 97206, 99958, 102711, 105463, 108216,
             110968, 113721, 116475, 119227, 121980, 124732, 127485, 130237, 132991, 135744, 138496, 141249, 144001, 146754, 149506, 152260, 155013, 157765, 160518, 163270, 166023, 168777, 171529, 174282, 177034, 179787, 182539, 185292, 188046, 190798, 193551, 196303, 199056, 201808]
    data2 = [0, 59356, 73118, 86882, 100646, 114410, 128174, 141937, 155700, 169464, 183228, 196991, 210755, 224519, 238283, 252045, 265809, 279573, 293337, 307101, 320864, 334628, 348392, 362156, 375918, 389682, 403446, 417210, 430974, 444737, 458501, 472264, 486028, 499791, 513555, 527319,
             541083, 554847, 568609, 582373, 596137, 609901, 623664, 637428, 651192, 664956, 678720, 692482, 706246, 720010, 733774, 747537, 761301, 775065, 788828, 802591, 816355, 830119, 843883, 857647, 871410, 885173, 898937, 912701, 926464, 940228, 953992, 967756, 981520, 995282, 1009046]
    data3 = [0, 39570, 48745, 57922, 67097, 76273, 85448, 94625, 103800, 112976, 122151, 131328, 140503, 149679, 158854, 168031, 177206, 186382, 195557, 204734, 213909, 223085, 232260, 241437, 250612, 259788, 268964, 278140, 287316, 296491, 305667, 314843, 324019, 333194, 342370, 351546,
             360722, 369897, 379073, 388249, 397425, 406600, 415776, 424951, 434128, 443303, 452479, 461654, 470831, 480006, 489182, 498357, 507534, 516709, 525885, 535060, 544237, 553413, 562588, 571765, 580940, 590116, 599291, 608467, 617643, 626819, 635994, 645170, 654346, 663522, 672697]
    data4 = [0, 11871, 14623, 17376, 20128, 22881, 25635, 28387, 31140, 33892, 36645, 39397, 42150, 44904, 47656, 50409, 53161, 55914, 58666, 61420, 64173, 66925, 69678, 72430, 75183, 77935, 80689, 83442, 86194, 88947, 91699, 94452, 97206, 99958, 102711, 105463, 108216,
             110968, 113721, 116475, 119227, 121980, 124732, 127485, 130237, 132991, 135744, 138496, 141249, 144001, 146754, 149506, 152260, 155013, 157765, 160518, 163270, 166023, 168777, 171529, 174282, 177034, 179787, 182539, 185292, 188046, 190798, 193551, 196303, 199056, 201808]

    hit0 = 4
    hit1 = 5
    hit2 = 1
    hit3 = 1
    hit4 = 15
    # 基础 = 9665*4 + 7733*5 + 38660 + 25772 + 7733*15
    # 成长 = 2917*4 + 2333*5 + 11669 + 7780 + 2333*15
    CD = 290

    MP = [4025, 8055]
    无色消耗 = 15


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'battle_mage'
        self.名称 = '知源·战斗法师'
        self.角色 = '魔法师(女)'

        self.职业 = '战斗法师'
        self.武器选项 = ['矛', '棍棒']
        self.输出类型选项 = ['物理百分比', '魔法百分比']
        self.防具精通属性 = ['力量', '智力']
        self.类型 = '物理百分比'
        self.武器类型 = '矛'
        self.防具类型 = '皮甲'

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
        self.buff = 1.85

        super().__init__()

    def 职业特殊计算(self):
        pass

    def set_skill_info(self, info, rune_except=[], clothes_pants=[]):
        super().set_skill_info(info, clothes_pants=['魔法秀'])
