# https://blog.csdn.net/qq_41431457/article/details/85262605
# https://www.jianshu.com/p/0954097a444e 稳定性分析
# 单链表可使用的排序：冒泡、选择、快排、归并 # https://blog.csdn.net/qq_36528114/article/details/79566285
def bubble_sort(arr):
    """
    冒泡排序
    时间复杂度：O(n^2), 空间复杂度：O(1)
    稳定性：由于交换的if条件是a[j]>a[j+1]，所以如果等于的话并没有交换，所以冒泡排序是一种稳定排序算法。

    冒泡排序较稳定，可用于链式存储结构，时间复杂度较高，当n较大，初始记录无序时，不宜采用此方法
    """
    list_length = len(arr)
    for i in range(list_length-1):
        # flag 用于判断在一次遍历过程中，是否发生交换
        # 若没有发生交换，则说明已经排序完成，无需继续循环，跳出
        flag = False
        for j in range(list_length-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if flag is False:
            break
    return arr


def insertion_sort(arr):
    """
    插入排序：类似于抓牌的方法, 基本操作是将一条元素插入到已排号的序列当中，从而得到一个有序的序列。
    时间复杂度：O（n^2)， 空间复杂度：O（1）
    稳定性：稳定排序

    算法简单稳定，容易实现，也适用于链式存储结构，在单链表中只需修改指针，更适用于初始记录基本有序的情况。
    对于查找插入位置，我们可以用二分查找获取位置
    """
    list_length = len(arr)
    # 默认已经有一张牌（一个元素），从第二个开始循环
    for i in range(1, list_length):
        # tmp为新抓的牌
        tmp = arr[i]
        j = i - 1
        # 从后往前循环，比较大小
        while j >= 0 and tmp < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tmp
    return arr


def shell_sort(arr):
    """
    希尔排序：分组插入排序,插入排序的改进版
    定义一个增量序列（逐渐减小直至为1），按照序列中元素的大小，间隔地进行插入排序
    插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位

    时间复杂度：时间复杂度比较复杂，通常认为O(n*logn)，当n趋近于无穷大时，可以为O（n(logn)^2)
    空间复杂度：O（1）
    稳定性：不稳定

    希尔排序只能用于顺序存储结构，不能用于链式存储结构，增量gap可以有各种取法，但最后一次gap必须等于1,
    总比较次数和移动次数较直接插入排序少，当n越大，序列越无序时，效果越明显。
    """
    list_length = len(arr)
    gap = list_length // 2
    while gap > 0:
        # 对每隔gap的元素集合，进行简单插入排序
        for i in range(gap, list_length, gap):
            # 默认已有一张牌j，从i开始作比较
            tmp = arr[i]
            j = i - gap
            # 从后往前循环，比较大小
            while j >= 0 and tmp < arr[j]:
                arr[j + gap] = arr[j]
                j -= gap
            # 将新牌tmp插入保存的插入位置，因为上一步循环最后j减去了一个gap，需要加上
            arr[j + gap] = tmp
        gap //= 2
    return arr


def selection_sort(arr):
    """
    选择排序：最简单直观的排序
    在未排序序列中找到最小元素，存放到排序序列的起始位置。再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾
    优点：简单，稳定
    缺点：O(N^2)的复杂度
    """
    list_length = len(arr)
    for i in range(list_length-1):
        min_idx = i
        for j in range(i+1, list_length):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def heap_sort(arr):
    """
    堆排序：利用最大堆进行改进，也是选择排序的思路演变而来
    时间复杂度：小于O（nlogn），空间复杂度：O（nlogn）
    缺点：不稳定
    """
    def adjust_down(arr, parent_idx, length):
        tmp = arr[parent_idx]
        while parent_idx*2 + 1 <= length:
            child_idx = parent_idx * 2 + 1
            # 找左右子节点中更大的那个，与parent互换
            if child_idx != length and arr[child_idx] < arr[child_idx+1]:
                child_idx += 1
            if tmp < arr[child_idx]:
                arr[parent_idx] = arr[child_idx]
            else:
                break
            parent_idx = child_idx
        arr[parent_idx] = tmp

    def creat_max_heap(arr, length):
        for parent_idx in range(length//2, -1, -1):
            adjust_down(arr, parent_idx, length)

    # 建立最大堆
    length = len(arr) - 1
    creat_max_heap(arr, length)
    for i in range(length, 0, -1):
        # 将last元素与堆顶最大元素互换
        arr[i], arr[0] = arr[0], arr[i]
        # 再在循环进行下沉过程中,不断剔除当前的最大项(第i项)
        adjust_down(arr, 0, i - 1)
    return arr


def merge_sort(arr):
    """
    归并排序：采用分治法，结合二叉树性质
    优点：无适应性问题，无论对于什么样的序列它都要做logN遍的递归，时间复杂度是固定的NlogN，算法稳定
    缺点：空间复杂度为N，较大
    特点：适用于外排序
    """
    def merge(left, right):
        """将两个有序的子序列，合并为一个序列"""
        i, j = 0, 0  # 设置两个指针，分别在一开始指向两个子序列的第一项
        merged = []  # 返回的合并后的序列
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        if len(left[i:]) > 0:
            merged.extend(left[i:])
        if len(right[j:]) > 0:
            merged.extend(right[j:])
        return merged

    # 递归方法：不断对子序列进行merge_sort再合并
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[0:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

    # # 非递归方法
    # # 第一层循环表示归并的次数:第一次分成n个长度为1的子数组，进行归并,第二次分成n/2个长度为2的子数组....
    # # 一个长度为n的数组需要归并logN次。第二层循环表示把两个子数组进行归并
    # sub_list_len = 1
    # list_len = len(my_list)
    # while sub_list_len < list_len:
    #     low = 0
    #     while low < len(my_list):
    #         middle = low + sub_list_len
    #         height = min(low + 2*sub_list_len, list_len)
    #         if middle < height:
    #             left = my_list[low: middle]
    #             right = my_list[middle: height]
    #             tmp = merge(left, right)
    #             my_list[low: height] = tmp
    #         low += 2*sub_list_len
    #     sub_list_len *= 2
    # return my_list


def quick_sort(arr):
    """
    快速排序算法，是最实用的排序算法，各大语言标准库的排序函数也基本都是基于快排实现的
    优点：平均时间复杂度O(NlogN), 空间复杂度至少O(logN)
    缺点：不稳定；对于小规模数据，递归效果并不好，可以调用简单排序如插入排序
    """
    def q_sort(array, low, high):
        # 如果说明子集已经划分到最小，无需再排序
        if low >= high:
            return
        # 取最后一个元素为基准，这里的选基准方案是快排的一个改进空间
        pivot = array[high]
        # i,j分别为指针
        i, j = low, high

        while i < j:
            # 将i右移到第一个大于pivot的位置
            while i < j and array[i] <= pivot:
                i += 1
            # 将j左移到第一个小于pivot的位置
            while i < j and array[j] >= pivot:
                j -= 1
            # 交换二者的位置
            array[i], array[j] = array[j], array[i]
        # 再将pivot与i和j的位置交换（二者此时指向同一位置），pivot此时处于其最终的位置
        array[i], array[high] = array[high], array[i]
        # 对子集进行递归
        q_sort(array, low, i - 1)
        q_sort(array, i + 1, high)

    q_sort(arr, 0, len(arr) - 1)
    return arr


def radix_sort(arr):
    """
    基数排序：桶排序的改进版
    优点：时间复杂度O(D(N+R)),D为轮次（最大数有几位，即有及轮次），N为元素数，R为桶的数量（进制数）
    可以看出广义上的线性排序方法，空间复杂度O(N+R),算法稳定
    """
    digit = 1  # 初始位数为个位，“次位优先”
    max_digit = 1  # 最大数的位数有几位
    max_item = max(arr)
    while max_item >= 10 ** max_digit:
        max_digit += 1

    while digit <= max_digit:
        bucket = {}  # 用字典构建桶
        for i in range(10):
            bucket.setdefault(i, [])  # 将每个桶置空
        for i in arr:
            radix = int(i / (10**(digit-1)) % 10)  # 获取每个元素在当前位数的基数
            bucket[radix].append(i)  # 将对应基数的元素加到对应的桶当中
        # 再将桶中的元素串接起来
        tmp_list = []

        for i in range(10):
            if len(bucket[i]) > 0:
                for j in bucket[i]:
                    tmp_list.append(j)
        arr = tmp_list
        # 位数进一，以进行下一轮次的排序
        digit += 1

    return arr


test_list = [1, 12, 5, 5, 3, 7, 10, 143, 9, 6, 11, 4, 155, 13, 2, 8]
# test_list = [1, 5, 3, 2]
result = quick_sort(test_list)
for item in result:
    print(item, end=' ')
