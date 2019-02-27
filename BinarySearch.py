def binary_search(sort_list, data):
    left = 0
    right = len(sort_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sort_list[mid] < data:
            left = mid + 1              # 一定要+1或者-1，
        elif sort_list[mid] > data:     # 否则会导致循环在未找到data情况下 无法跳出
            right = mid - 1
        else:
            return mid
    return 'not found'


l = list(range(0, 30, 2))
res = binary_search(l, 13)
print(res)