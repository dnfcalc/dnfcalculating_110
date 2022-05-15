fumo_func_list = {}

# done


def fumo_0(char={}, mode=0, text=False, rate=1.0):
    if text:
        return "无附魔"
    if mode == 0:
        pass
    if mode == 1:
        pass


# 附魔效果列表
for i in range(20):
    try:
        if i not in fumo_func_list.keys():
            fumo_func_list[i + 20000] = [eval('fumo_{}'.format(i))]
    except:
        pass

# 附魔效果id范围 20000~20999
