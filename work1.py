def find_max_and_min(a):
    # 验证数组是否为空
    if len(a) == 0:
        return None, None

    # 初始化最大值和最小值
    if len(a) % 2 == 0:  # 数组长度为偶数
        if a[0] > a[1]:
            maxe, mine = a[0], a[1]
        else:
            maxe, mine = a[1], a[0]
        start_index = 2
    else:  # 数组长度为奇数
        maxe = mine = a[0]
        start_index = 1

    # 成对比较
    for i in range(start_index, len(a) - 1, 2):
        if a[i] > a[i + 1]:
            if a[i] > maxe:
                maxe = a[i]
            if a[i + 1] < mine:
                mine = a[i + 1]
        else:
            if a[i + 1] > maxe:
                maxe = a[i + 1]
            if a[i] < mine:
                mine = a[i]

    # 如果数组长度为奇数，检查最后一个元素
    if len(a) % 2 != 0:
        if a[-1] > maxe:
            maxe = a[-1]
        if a[-1] < mine:
            mine = a[-1]

    return maxe, mine


