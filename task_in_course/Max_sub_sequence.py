def max_subseq_sum(my_list):
    """在线处理方法"""
    num = len(my_list)
    this_sum = max_sum = 0
    for i in range(num):
        this_sum += my_list[i]
        if this_sum > max_sum:
            max_sum = this_sum
        # 如果当前的子列和this_sum小于0，就置为0
        # 说明其无法使后续部分的和增大，舍弃之
        elif this_sum < 0:
            this_sum = 0
    return max_sum


l = [-1, 3, 5, 4, -6, 1, 6, -1]
print(max_subseq_sum(l))
