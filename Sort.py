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
    pass


test_list = [1, 5, 3, 7, 9, 6, 4, 2, 8]
result = bubble_sort(test_list)
for item in result:
    print(item)
