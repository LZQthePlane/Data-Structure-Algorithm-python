def bubble_sort(my_list):
    """
    冒泡排序
    优点：只在相邻元素之间操作（适用于链表结构的list）；不会破环相同大小元素的相对位置，稳定
    缺点：O(N^2)的复杂度，较大
    """
    list_length = len(my_list)
    for i in range(list_length-1):
        # flag 用于判断在一次遍历过程中，是否发生交换
        # 若没有发生交换，则说明已经排序完成，无需继续循环，跳出
        flag = False
        for j in range(list_length-1-i):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                flag = True
        if flag is False:
            break
    return my_list


def insertion_sort(my_list):
    """
    插入排序：类似于抓牌的方法
    优点：同样不会破坏相同大小元素的相对位置，比较稳定；对于基本有序的序列，排序速度很快
    缺点：O(N^2)的复杂度，较大
    """
    list_length = len(my_list)
    # 默认已经有一张牌（一个元素），从第二个开始循环
    for i in range(1, list_length):
        # tmp为新抓的牌
        tmp = my_list[i]
        # 如果新抓的牌比已有的最后一个元素（最大元素）大，则无需进行排序
        if my_list[i] < my_list[i-1]:
            # 初始化插入位置
            insert_idx = 0
            # 从后往前循环，比较大小
            for j in range(i-1, -1, -1):
                # 如果新牌小于当前元素，将当前元素往后移，并更新插入位置
                if tmp < my_list[j]:
                    my_list[j+1] = my_list[j]
                    insert_idx = j
                # 否则跳出循环
                else:
                    break
            # 将新牌tmp插入保存的插入位置
            my_list[insert_idx] = tmp
    return my_list


def shell_sort(my_list):
    """
    希尔排序：分组插入排序,插入排序的改进版
    定义一个增量序列（逐渐减小直至为1），按照序列中元素的大小，间隔地进行插入排序
    插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位
    缺点：非稳定
    """
    list_length = len(my_list)
    gap = list_length // 2
    while gap > 0:
        for i in range(gap, list_length):
            # 间隔地进行插入排序，这里用的是比较大小交换位置的方法
            # 上述的插入排序中用的是比较并向后移位的方法
            # 看视频更易理解
            while i > gap and my_list[i] < my_list[i-gap]:
                my_list[i], my_list[i-gap] = my_list[i-gap], my_list[i]
                i -= gap
        gap //= 2
    return my_list


def selection_sort(my_list):
    """
    选择排序：最简单直观的排序
    在未排序序列中找到最小元素，存放到排序序列的起始位置。再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾
    优点：简单，稳定
    缺点：O(N^2)的复杂度
    """
    list_length = len(my_list)
    for i in range(list_length-1):
        min_idx = i
        for j in range(i+1, list_length):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list


def heap_sort(my_list):
    """
    堆排序：利用最大堆进行改进，也是选择排序的思路演变而来
    时间复杂度：小于O（nlogn），空间复杂度：O（nlogn）
    缺点：不稳定
    """
    def adjust_down(l, parent_idx, length):
        tmp = l[parent_idx]
        while True:
            child_idx = parent_idx * 2 + 1
            if child_idx > length:
                break
            if child_idx != length and l[child_idx] < l[child_idx+1]:
                child_idx += 1
            if tmp < l[child_idx]:
                l[parent_idx] = l[child_idx]
            else:
                break
            parent_idx = child_idx
        l[parent_idx] = tmp

    def creat_maxheap(l):
        length = len(l) - 1
        for parent_idx in range(length//2, -1, -1):
            adjust_down(l, parent_idx, length)
        return l

    # 建立最大堆
    creat_maxheap(my_list)
    for i in range(len(my_list)-1, 0, -1):
        # 将last元素与堆顶最大元素互换
        my_list[i], my_list[0] = my_list[0], my_list[i]
        # 再在循环进行下沉过程中,不断剔除当前的最大项(第i项)
        adjust_down(my_list, 0, i-1)
    return my_list


test_list = [1, 5, 3, 7, 10, 9, 6, 4, 2, 8]
result = heap_sort(test_list)
for item in result:
    print(item)
