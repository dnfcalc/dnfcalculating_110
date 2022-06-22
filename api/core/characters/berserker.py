
from core.baseClass.skill import 技能
from core.baseClass.character import Character
from core.baseClass.skill import 主动技能, 被动技能


class 技能0(主动技能):
    名称 = '崩山击'
    所在等级 = 10
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [17, 150]
    data0 = [int(x*1.202) for x in [0, 131, 144, 157, 170, 184, 197, 210, 224, 237, 250, 264, 277, 290, 303, 317, 330, 343, 357, 370, 383, 397,
                                    410, 423, 436, 450, 463, 476, 490, 503, 516, 529, 543, 556, 569, 583, 596, 609, 623, 636, 649, 662, 676, 689,
                                    702, 716, 729, 742, 756, 769, 782, 795, 809, 822, 835, 849, 862, 875, 888, 902, 915, 928, 942, 955, 968, 982,
                                    995, 1008, 1021, 1035, 1048]]
    hit0 = 1
    power0 = 3.4
    data1 = [int(x*1.202) for x in [0, 736, 811, 886, 960, 1035, 1110, 1184, 1259, 1334, 1409, 1483, 1558, 1633, 1707, 1782, 1857, 1932, 2006,
                                    2081, 2156, 2231, 2305, 2380, 2455, 2529, 2604, 2679, 2754, 2828, 2903, 2978, 3052, 3127, 3202, 3277, 3351,
                                    3426, 3501, 3576, 3650, 3725, 3800, 3874, 3949, 4024, 4099, 4173, 4248, 4323, 4397, 4472, 4547, 4622, 4696,
                                    4771, 4846, 4921, 4995, 5070, 5145, 5219, 5294, 5369, 5444, 5518, 5593, 5668, 5742, 5817, 5892]]
    hit1 = 1
    CD = 4.0
    TP成长 = 0.1
    TP上限 = 7


class 技能1(主动技能):
    名称 = '十字斩'
    所在等级 = 15
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [17, 170]
    data0 = [int(x*1.166) for x in [0, 142, 157, 171, 186, 200, 215, 229, 244, 258, 273, 287, 302, 316, 330, 345, 359, 374, 388, 403, 417, 432,
                                    446, 461, 475, 490, 504, 519, 533, 548, 562, 577, 591, 606, 620, 635, 649, 664, 678, 692, 707, 721, 736, 750,
                                    765, 779, 794, 808, 823, 837, 852, 866, 881, 895, 910, 924, 939, 953, 968, 982, 997, 1011, 1026, 1040, 1055,
                                    1069, 1083, 1098, 1112, 1127]]
    hit0 = 1
    CD = 2.4
    TP成长 = 0.1
    TP上限 = 7


class 技能2(主动技能):
    名称 = '血之狂暴'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    是否有伤害 = 0
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 <= 20:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.9 + 0.015 * self.等级, 5)


class 技能3(被动技能):
    名称 = '血气唤醒'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.267 + 0.02 * self.等级, 5)


class 技能4(主动技能):
    名称 = '嗜魂之手'

    所在等级 = 25
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [37, 200]
    data0 = [int(x*1.178) for x in [0, 1893, 2085, 2277, 2469, 2662, 2854, 3046, 3238, 3430, 3622, 3814, 4006, 4198, 4391, 4583, 4775, 4967, 5159, 5351, 5543, 5735, 5927, 6120, 6312, 6504, 6696, 6888, 7080, 7272, 7464, 7656, 7848, 8041, 8233, 8425, 8617, 8809,
                                    9001, 9193, 9385, 9577, 9770, 9962, 10154, 10346, 10538, 10730, 10922, 11114, 11306, 11499, 11691, 11883, 12075, 12267, 12459, 12651, 12843, 13035, 13228, 13420, 13612, 13804, 13996, 14188, 14380, 14572, 14764, 14956, 15149]]
    hit0 = 1
    CD = 4.8
    TP成长 = 0.10
    TP上限 = 7


class 技能5(主动技能):
    名称 = '怒气爆发'
    所在等级 = 30
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [110, 924]
    data0 = [int(x*1.206) for x in [0, 318, 351, 383, 415, 448, 480, 512, 545, 577, 609, 642, 674, 706, 739, 771, 803, 836, 868, 901, 933, 965,
                                    998, 1030, 1062, 1095, 1127, 1159, 1192, 1224, 1256, 1289, 1321, 1353, 1386, 1418, 1450, 1483, 1515, 1547,
                                    1580, 1612, 1644, 1677, 1709, 1741, 1774, 1806, 1838, 1871, 1903, 1936, 1968, 2000, 2033, 2065, 2097, 2130,
                                    2162, 2194, 2227, 2259, 2291, 2324, 2356, 2388, 2421, 2453, 2485, 2518, 2550]]
    hit0 = 10
    data1 = [int(x*1.206) for x in [0, 835, 920, 1005, 1089, 1174, 1259, 1344, 1428, 1513, 1598, 1683, 1767, 1852, 1937, 2022, 2107, 2191, 2276,
                                    2361, 2446, 2530, 2615, 2700, 2785, 2869, 2954, 3039, 3124, 3209, 3293, 3378, 3463, 3548, 3632, 3717, 3802,
                                    3887, 3971, 4056, 4141, 4226, 4310, 4395, 4480, 4565, 4650, 4734, 4819, 4904, 4989, 5073, 5158, 5243, 5328,
                                    5412, 5497, 5582, 5667, 5752, 5836, 5921, 6006, 6091, 6175, 6260, 6345, 6430, 6514, 6599, 6684]]
    hit1 = 1
    CD = 12.8
    TP成长 = 0.10
    TP上限 = 7


class 技能6(主动技能):
    名称 = '嗜魂封魔斩'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [int(x*1.188) for x in [0, 8275, 9115, 9955, 10794, 11634, 12473, 13313, 14152, 14992, 15832, 16671, 17511, 18350, 19190, 20030,
                                    20869, 21709, 22548, 23388, 24227, 25067, 25907, 26746, 27586, 28425, 29265, 30105, 30944, 31784, 32623,
                                    33463, 34302, 35142, 35982, 36821, 37661, 38500, 39340, 40180, 41019, 41859, 42698, 43538, 44377, 45217,
                                    46057, 46896, 47736, 48575, 49415, 50255, 51094, 51934, 52773, 53613, 54452, 55292, 56132, 56971, 57811,
                                    58650, 59490, 60330, 61169, 62009, 62848, 63688, 64527, 65367, 66207]]
    hit0 = 1
    MP = [180, 1512]
    无色消耗 = 1
    CD = 24.0
    TP成长 = 0.10
    TP上限 = 5


class 技能7(主动技能):
    名称 = '暴怒狂斩'
    所在等级 = 35
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [113, 1117]
    无色消耗 = 1
    data0 = [int(x*1.184) for x in [0, 1054, 1161, 1268, 1375, 1482, 1589, 1696, 1803, 1910, 2017, 2124, 2231, 2338, 2445, 2552, 2659, 2766, 2873,
                                    2980, 3087, 3194, 3301, 3408, 3515, 3622, 3729, 3836, 3943, 4050, 4156, 4263, 4370, 4477, 4584, 4691, 4798,
                                    4905, 5012, 5119, 5226, 5333, 5440, 5547, 5654, 5761, 5868, 5975, 6082, 6189, 6296, 6403, 6510, 6617, 6724,
                                    6831, 6938, 7045, 7152, 7259, 7366, 7473, 7580, 7687, 7794, 7901, 8008, 8115, 8222, 8329, 8436]]
    hit0 = 1
    data1 = [int(x*1.184) for x in [0, 307, 338, 369, 401, 432, 463, 494, 525, 557, 588, 619, 650, 682, 713, 744, 775, 806, 838, 869, 900, 931,
                                    962, 994, 1025, 1056, 1087, 1118, 1150, 1181, 1212, 1243, 1274, 1306, 1337, 1368, 1399, 1430, 1462, 1493,
                                    1524, 1555, 1586, 1618, 1649, 1680, 1711, 1742, 1774, 1805, 1836, 1867, 1898, 1930, 1961, 1992, 2023, 2054,
                                    2086, 2117, 2148, 2179, 2210, 2242, 2273, 2304, 2335, 2366, 2398, 2429, 2460]]
    hit1 = 8
    data2 = [int(x*1.184) for x in [0, 1757, 1935, 2114, 2292, 2470, 2649, 2827, 3005, 3183, 3362, 3540, 3718, 3897, 4075, 4253, 4432, 4610,
                                    4788, 4966, 5145, 5323, 5501, 5680, 5858, 6036, 6215, 6393, 6571, 6750, 6928, 7106, 7284, 7463, 7641, 7819,
                                    7998, 8176, 8354, 8533, 8711, 8889, 9067, 9246, 9424, 9602, 9781, 9959, 10137, 10316, 10494, 10672, 10850,
                                    11029, 11207, 11385, 11564, 11742, 11920, 12099, 12277, 12455, 12633, 12812, 12990, 13168, 13347, 13525,
                                    13703, 13882, 14060]]
    hit2 = 2
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    power1 = 1
    power2 = 1

    def 装备护石(self):
        self.power0 = 0
        self.power1 *= 1.56
        self.power2 *= 1.56
        self.CDR *= 0.9


class 技能8(主动技能):
    名称 = '嗜血'
    所在等级 = 35
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.01 * self.等级, 5)


class 技能9(主动技能):
    名称 = '血气之刃'
    所在等级 = 40
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    MP = [0, 0]
    无色消耗 = 1
    data0 = [int(x*1.198) for x in [0, 6379, 7026, 7674, 8321, 8968, 9615, 10262, 10910, 11557, 12204, 12851, 13499, 14146, 14793, 15440, 16087,
                                    16735, 17382, 18029, 18676, 19323, 19971, 20618, 21265, 21912, 22559, 23207, 23854, 24501, 25148, 25796,
                                    26443, 27090, 27737, 28384, 29032, 29679, 30326, 30973, 31620, 32268, 32915, 33562, 34209, 34857, 35504,
                                    36151, 36798, 37445, 38093, 38740, 39387, 40034, 40681, 41329, 41976, 42623, 43270, 43918, 44565, 45212,
                                    45859, 46506, 47154, 47801, 48448, 49095, 49742, 50390, 51037]]
    hit0 = 1
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.37


class 技能10(主动技能):
    名称 = '崩山裂地斩'
    所在等级 = 45
    等级上限 = 70
    学习间隔 = 2
    等级精通 = 60
    data0 = [int(x*1.202) for x in [0, 321, 354, 386, 419, 452, 484, 517, 550, 582, 615, 648, 680, 713, 745, 778, 811, 843, 876, 909, 941, 974,
                                    1007, 1039, 1072, 1104, 1137, 1170, 1202, 1235, 1268, 1300, 1333, 1366, 1398, 1431, 1463, 1496, 1529, 1561,
                                    1594, 1627, 1659, 1692, 1724, 1757, 1790, 1822, 1855, 1888, 1920, 1953, 1986, 2018, 2051, 2083, 2116, 2149,
                                    2181, 2214, 2247, 2279, 2312, 2345, 2377, 2410, 2442, 2475, 2508, 2540, 2573]]
    hit0 = 1
    data1 = [int(x*1.202) for x in [0, 2144, 2362, 2579, 2797, 3014, 3232, 3449, 3667, 3885, 4102, 4320, 4537, 4755, 4972, 5190, 5408, 5625,
                                    5843, 6060, 6278, 6495, 6713, 6931, 7148, 7366, 7583, 7801, 8018, 8236, 8454, 8671, 8889, 9106, 9324, 9541,
                                    9759, 9976, 10194, 10412, 10629, 10847, 11064, 11282, 11499, 11717, 11935, 12152, 12370, 12587, 12805, 13022,
                                    13240, 13458, 13675, 13893, 14110, 14328, 14545, 14763, 14980, 15198, 15416, 15633, 15851, 16068, 16286,
                                    16503, 16721, 16939, 17156]]
    hit1 = 1
    data2 = [int(x*1.202) for x in [0, 1376, 1515, 1655, 1794, 1934, 2074, 2213, 2353, 2492, 2632, 2772, 2911, 3051, 3190, 3330, 3470, 3609,
                                    3749, 3888, 4028, 4168, 4307, 4447, 4587, 4726, 4866, 5005, 5145, 5285, 5424, 5564, 5703, 5843, 5983, 6122,
                                    6262, 6401, 6541, 6681, 6820, 6960, 7099, 7239, 7379, 7518, 7658, 7797, 7937, 8077, 8216, 8356, 8495, 8635,
                                    8775, 8914, 9054, 9193, 9333, 9473, 9612, 9752, 9892, 10031, 10171, 10310, 10450, 10590, 10729, 10869, 11008]]
    hit2 = 6
    MP = [0, 0]
    无色消耗 = 2
    CD = 32.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.26
        self.CDR *= 0.95


class 技能11(被动技能):
    名称 = '鲜血之忆'
    所在等级 = 48
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 3

    def 独立攻击力倍率进图(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.114 + 0.015 * self.等级, 5)


class 技能12(主动技能):
    名称 = '魔狱血刹'
    所在等级 = 50
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [int(x*1.238) for x in [0, 6404, 7889, 9374, 10859, 12344, 13829, 15314, 16799, 18284, 19769, 21254, 22739, 24224, 25709, 27194,
                                    28679, 30164, 31649, 33134, 34619, 36104, 37589, 39074, 40559, 42044, 43529, 45014, 46499, 47984, 49469,
                                    50954, 52439, 53924, 55409, 56894, 58379, 59864, 61349, 62834, 64319, 65804, 67289, 68774, 70259, 71744,
                                    73229, 74714, 76199, 77684, 79169, 80654, 82139, 83624, 85109, 86594, 88079, 89564, 91049, 92534, 94019,
                                    95504, 96989, 98474, 99959, 101444, 102929, 104414, 105899, 107384, 108869]]
    hit0 = 1
    data1 = [int(x*1.238) for x in [0, 908, 1118, 1329, 1540, 1750, 1961, 2171, 2382, 2593, 2803, 3014, 3224, 3435, 3646, 3856, 4067, 4277, 4488,
                                    4699, 4909, 5120, 5330, 5541, 5752, 5962, 6173, 6383, 6594, 6805, 7015, 7226, 7436, 7647, 7858, 8068, 8279,
                                    8489, 8700, 8911, 9121, 9332, 9542, 9753, 9964, 10174, 10385, 10595, 10806, 11017, 11227, 11438, 11648,
                                    11859, 12070, 12280, 12491, 12701, 12912, 13123, 13333, 13544, 13754, 13965, 14176, 14386, 14597, 14807,
                                    15018, 15229, 15439]]
    hit1 = 27
    CD = 145
    MP = [900, 7560]
    无色消耗 = 10


class 技能13(主动技能):
    名称 = '鲜血暴掠'
    所在等级 = 60
    等级上限 = 50
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [int(x*1.204) for x in [0, 1808, 1991, 2175, 2358, 2542, 2725, 2908, 3092, 3275, 3459, 3642, 3826, 4009, 4193, 4376, 4559, 4743, 4926,
                                    5110, 5293, 5477, 5660, 5843, 6027, 6210, 6394, 6577, 6761, 6944, 7128, 7311, 7494, 7678, 7861, 8045, 8228,
                                    8412, 8595, 8779, 8962, 9145, 9329, 9512, 9696, 9879, 10063, 10246, 10430, 10613, 10796, 10980, 11163, 11347,
                                    11530, 11714, 11897, 12081, 12264, 12447, 12631, 12814, 12998, 13181, 13365, 13548, 13732, 13915, 14098,
                                    14282, 14465]]
    hit0 = 1
    data1 = [int(x*1.204) for x in [0, 10246, 11286, 12325, 13365, 14404, 15444, 16483, 17523, 18562, 19602, 20641, 21681, 22720, 23760, 24799,
                                    25839, 26878, 27918, 28957, 29997, 31036, 32076, 33115, 34155, 35195, 36234, 37274, 38313, 39353, 40392,
                                    41432, 42471, 43511, 44550, 45590, 46629, 47669, 48708, 49748, 50787, 51827, 52866, 53906, 54945, 55985,
                                    57024, 58064, 59103, 60143, 61182, 62222, 63261, 64301, 65340, 66380, 67419, 68459, 69498, 70538, 71578,
                                    72617, 73657, 74696, 75736, 76775, 77815, 78854, 79894, 80933, 81973]]
    hit1 = 1
    MP = [344, 963]
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    # 血之连接
    # 施放过程中连接[崩山裂地斩]时， 血气爆炸的瞬间施放[崩山裂地斩]
    # 攻击力 +14%
    # 不抓取敌人也可以引发血气爆炸
    # 血气爆炸范围 +20%
    # 攻击力 +6%

    def 装备护石(self):
        self.倍率 *= 1.29


class 技能14(主动技能):
    名称 = '血气爆发'
    所在等级 = 70
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    MP = [1000, 2800]
    无色 = 2
    data0 = [int(x*1.207) for x in [0, 980, 1079, 1178, 1278, 1377, 1477, 1576, 1676, 1775, 1874, 1974, 2073, 2173, 2272, 2371, 2471, 2570, 2670,
                                    2769, 2869, 2968, 3067, 3167, 3266, 3366, 3465, 3565, 3664, 3763, 3863, 3962, 4062, 4161, 4261, 4360, 4459,
                                    4559, 4658, 4758, 4857, 4956, 5056, 5155, 5255, 5354, 5454, 5553, 5652, 5752, 5851, 5951, 6050, 6150, 6249,
                                    6348, 6448, 6547, 6647, 6746, 6846, 6945, 7044, 7144, 7243, 7343, 7442, 7542, 7641, 7740, 7840]]
    hit0 = 20
    data1 = [int(x*1.207) for x in [0, 3631, 4000, 4368, 4737, 5105, 5474, 5842, 6211, 6579, 6947, 7316, 7684, 8053, 8421, 8790, 9158, 9527,
                                    9895, 10264, 10632, 11000, 11369, 11737, 12106, 12474, 12843, 13211, 13580, 13948, 14317, 14685, 15053,
                                    15422, 15790, 16159, 16527, 16896, 17264, 17633, 18001, 18370, 18738, 19106, 19475, 19843, 20212, 20580,
                                    20949, 21317, 21686, 22054, 22423, 22791, 23159, 23528, 23896, 24265, 24633, 25002, 25370, 25739, 26107,
                                    26475, 26844, 27212, 27581, 27949, 28318, 28686, 29055]]
    hit1 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.25
        self.CDR *= 0.95


class 技能15(被动技能):
    名称 = '汲血之力'
    所在等级 = 75

    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能16(主动技能):
    名称 = '浴血之怒'
    所在等级 = 75
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [int(x*1.204) for x in [0, 32861, 36195, 39529, 42863, 46197, 49530, 52864, 56198, 59532, 62866, 66199, 69533, 72867, 76201, 79535,
                                    82868, 86202, 89536, 92870, 96204, 99537, 102871, 106205, 109539, 112873, 116206, 119540, 122874, 126208,
                                    129542, 132876, 136209, 139543, 142877, 146211, 149545, 152878, 156212, 159546, 162880, 166214, 169547,
                                    172881, 176215, 179549, 182883, 186216, 189550, 192884, 196218, 199552, 202885, 206219, 209553, 212887,
                                    216221, 219554, 222888, 226222, 229556, 232890, 236224, 239557, 242891, 246225, 249559, 252893, 256226,
                                    259560, 262894]]
    hit0 = 1
    CD = 40.0
    无色消耗 = 3
    MP = [580, 4500]

    是否有护石 = 1

    def 装备护石(self, x):
        self.倍率 = 1.37


class 技能17(主动技能):
    名称 = '致命血陨'
    所在等级 = 80
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [int(x*1.20) for x in [0, 8248, 9085, 9922, 10758, 11595, 12432, 13269, 14106, 14942, 15779, 16616, 17453, 18290, 19126, 19963,
                                   20800, 21637, 22473, 23310, 24147, 24984, 25821, 26657, 27494, 28331, 29168, 30005, 30841, 31678, 32515,
                                   33352, 34189, 35025, 35862, 36699, 37536, 38373, 39209, 40046, 40883, 41720, 42557, 43393, 44230, 45067,
                                   45904, 46741, 47577, 48414, 49251, 50088, 50925, 51761, 52598, 53435, 54272, 55109, 55945, 56782, 57619,
                                   58456, 59293, 60129, 60966, 61803, 62640, 63477, 64313, 65150, 65987]]
    hit0 = 1
    data1 = [int(x*1.20) for x in [0, 10310, 11356, 12402, 13448, 14494, 15540, 16586, 17632, 18678, 19724, 20770, 21816, 22862, 23908, 24954,
                                   26000, 27046, 28092, 29138, 30184, 31230, 32276, 33322, 34368, 35414, 36460, 37506, 38552, 39598, 40644,
                                   41690, 42736, 43782, 44828, 45874, 46920, 47966, 49012, 50058, 51104, 52150, 53196, 54242, 55288, 56334,
                                   57380, 58426, 59472, 60518, 61564, 62610, 63656, 64702, 65748, 66794, 67840, 68886, 69932, 70978, 72024,
                                   73070, 74116, 75162, 76208, 77254, 78300, 79346, 80392, 81438, 82484]]
    hit1 = 1
    data2 = [int(x*1.20) for x in [0, 22683, 24984, 27285, 29586, 31887, 34189, 36490, 38791, 41092, 43393, 45695, 47996, 50297, 52598, 54899,
                                   57201, 59502, 61803, 64104, 66405, 68707, 71008, 73309, 75610, 77911, 80213, 82514, 84815, 87116, 89417,
                                   91718, 94020, 96321, 98622, 100923, 103224, 105526, 107827, 110128, 112429, 114730, 117032, 119333, 121634,
                                   123935, 126236, 128538, 130839, 133140, 135441, 137742, 140044, 142345, 144646, 146947, 149248, 151550,
                                   153851, 156152, 158453, 160754, 163055, 165357, 167658, 169959, 172260, 174561, 176863, 179164, 181465]]
    hit2 = 1

    MP = [848, 6360]
    无色消耗 = 5
    CD = 50.0

    是否有护石 = 1

    def 装备护石(self):
        self.power2 *= 1.19
        self.倍率 *= 1.21
        self.CDR *= 0.9


class 技能18(主动技能):
    名称 = '血魔弑天'
    所在等级 = 85
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    data0 = [int(x*1.201) for x in [0, 17450, 21496, 25543, 29589, 33635, 37682, 41728, 45775, 49821, 53868, 57914, 61960, 66007, 70053, 74100,
                                    78146, 82193, 86239, 90285, 94332, 98378, 102425, 106471, 110517, 114564, 118610, 122657, 126703, 130750,
                                    134796, 138842, 142889, 146935, 150982, 155028, 159075, 163121, 167167, 171214, 175260, 179307, 183353,
                                    187400, 191446, 195492, 199539, 203585, 207632, 211678, 215725, 219771, 223817, 227864, 231910, 235957,
                                    240003, 244050, 248096, 252142, 256189, 260235, 264282, 268328, 272375, 276421, 280467, 284514, 288560,
                                    292607, 296653]]
    hit0 = 2
    data1 = [int(x*1.201) for x in [0, 42656, 52547, 62438, 72329, 82221, 92112, 102003, 111894, 121786, 131677, 141568, 151459, 161351, 171242,
                                    181133, 191025, 200916, 210807, 220698, 230590, 240481, 250372, 260263, 270155, 280046, 289937, 299828,
                                    309720, 319611, 329502, 339393, 349285, 359176, 369067, 378959, 388850, 398741, 408632, 418524, 428415,
                                    438306, 448197, 458089, 467980, 477871, 487762, 497654, 507545, 517436, 527327, 537219, 547110, 557001,
                                    566893, 576784, 586675, 596566, 606458, 616349, 626240, 636131, 646023, 655914, 665805, 675696, 685588,
                                    695479, 705370, 715261, 725153]]
    hit1 = 1
    MP = [2500, 5000]
    无色消耗 = 10
    CD = 180


class 技能19(被动技能):
    名称 = '血气界限'
    所在等级 = 95

    等级上限 = 50
    学习间隔 = 3
    等级精通 = 40

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能20(主动技能):
    名称 = '疯魔血魂斩'
    所在等级 = 95
    等级上限 = 50
    学习间隔 = 2
    等级精通 = 40
    data0 = [int(x*1.204) for x in [0, 20368, 22434, 24500, 26567, 28633, 30699, 32766, 34832, 36898, 38965, 41031, 43097, 45164, 47230, 49297,
                                    51363, 53429, 55496, 57562, 59628, 61695, 63761, 65827, 67894, 69960, 72026, 74093, 76159, 78225, 80292,
                                    82358, 84424, 86491, 88557, 90623, 92690, 94756, 96822, 98889, 100955, 103021, 105088, 107154, 109220, 111287,
                                    113353, 115419, 117486, 119552, 121619, 123685, 125751, 127818, 129884, 131950, 134017, 136083, 138149,
                                    140216, 142282, 144348, 146415, 148481, 150547, 152614, 154680, 156746, 158813, 160879, 162945]]
    hit0 = 1
    data1 = [int(x*1.204) for x in [0, 9505, 10469, 11433, 12398, 13362, 14326, 15290, 16255, 17219, 18183, 19148, 20112, 21076, 22040, 23005,
                                    23969, 24933, 25898, 26862, 27826, 28791, 29755, 30719, 31683, 32648, 33612, 34576, 35541, 36505, 37469,
                                    38433, 39398, 40362, 41326, 42291, 43255, 44219, 45184, 46148, 47112, 48076, 49041, 50005, 50969, 51934,
                                    52898, 53862, 54826, 55791, 56755, 57719, 58684, 59648, 60612, 61576, 62541, 63505, 64469, 65434, 66398,
                                    67362, 68327, 69291, 70255, 71219, 72184, 73148, 74112, 75077, 76041]]
    hit1 = 5
    MP = [1017, 7632]
    无色消耗 = 7
    CD = 60.0


class 技能21(主动技能):
    名称 = '血魔极道灭世'
    所在等级 = 100
    等级上限 = 50
    学习间隔 = 5
    等级精通 = 40
    MP = [4027, 8055]
    data0 = [int(x*1.204) for x in [0, 8940, 11013, 13086, 15159, 17232, 19306, 21379, 23452, 25525, 27598, 29671, 31744, 33818, 35891, 37964, 40037, 42110, 44183, 46256, 48330, 50403, 52476, 54549, 56622, 58695, 60768, 62842, 64915, 66988, 69061, 71134, 73207, 75280, 77353, 79427, 81500,
                                    83573, 85646, 87719, 89792, 91865, 93939, 96012, 98085, 100158, 102231, 104304, 106377, 108451, 110524, 112597, 114670, 116743, 118816, 120889, 122963, 125036, 127109, 129182, 131255, 133328, 135401, 137475, 139548, 141621, 143694, 145767, 147840, 149913, 151986]]
    hit0 = 5
    data1 = [int(x*1.204) for x in [0, 16763, 20650, 24537, 28424, 32311, 36198, 40086, 43973, 47860, 51747, 55634, 59521, 63408, 67296, 71183, 75070, 78957, 82844, 86731, 90618, 94505, 98393, 102280, 106167, 110054, 113941, 117828, 121715, 125603, 129490, 133377, 137264, 141151, 145038, 148925, 152813,
                                    156700, 160587, 164474, 168361, 172248, 176135, 180022, 183910, 187797, 191684, 195571, 199458, 203345, 207232, 211120, 215007, 218894, 222781, 226668, 230555, 234442, 238329, 242217, 246104, 249991, 253878, 257765, 261652, 265539, 269427, 273314, 277201, 281088, 284975]]
    hit1 = 2
    data2 = [int(x*1.204) for x in [0, 44702, 55067, 65433, 75799, 86164, 96530, 106896, 117261, 127627, 137993, 148358, 158724, 169090, 179456, 189821, 200187, 210553, 220918, 231284, 241650, 252015, 262381, 272747, 283113, 293478, 303844, 314210, 324575, 334941, 345307, 355672, 366038, 376404, 386769, 397135,
                                    407501, 417867, 428232, 438598, 448964, 459329, 469695, 480061, 490426, 500792, 511158, 521523, 531889, 542255, 552621, 562986, 573352, 583718, 594083, 604449, 614815, 625180, 635546, 645912, 656277, 666643, 677009, 687375, 697740, 708106, 718472, 728837, 739203, 749569, 759934]]
    hit2 = 1
    data3 = [int(x*1.204) for x in [0, 7736, 9530, 11325, 13119, 14913, 16707, 18501, 20295, 22089, 23883, 25677, 27471, 29265, 31059, 32853, 34647, 36441, 38235, 40030, 41824, 43618, 45412, 47206, 49000, 50794, 52588, 54382, 56176, 57970, 59764, 61558, 63352, 65146, 66940, 68735, 70529,
                                    72323, 74117, 75911, 77705, 79499, 81293, 83087, 84881, 86675, 88469, 90263, 92057, 93851, 95645, 97440, 99234, 101028, 102822, 104616, 106410, 108204, 109998, 111792, 113586, 115380, 117174, 118968, 120762, 122556, 124350, 126145, 127939, 129733, 131527]]
    hit3 = 13

    次数 = [5, 2, 1, 13]
    无色消耗 = 15
    CD = 290


class classChange(Character):
    def __init__(self):
        self.实际名称 = 'berserker'
        self.名称 = '极诣·狂战士'
        self.角色 = '鬼剑士(男)'
        self.职业类型 = '输出'
        self.职业 = '狂战士'
        self.武器选项 = ['太刀', '钝器', '巨剑', '短剑']
        self.输出类型选项 = ['物理固伤']
        self.防具精通属性 = ['力量']
        self.类型 = '物理固伤'
        self.武器类型 = '巨剑'
        self.防具类型 = '重甲'
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
        self.buff = 2.16

        super().__init__()
