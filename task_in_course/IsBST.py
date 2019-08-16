"""
判断一棵二叉树是不是二叉搜索树
对其进行中序遍历，若遍历结果是递增的，即是
可以用递归方法或者非递归方法
"""


def isBst(root):
    if not root:
        return False
    pre_num = -100000
    node = root
    stack = []
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        # 如果遍历过程中，有一个node比前一个小，则不是bst
        # 反之，则将当前node值赋给pre_num，用于下次的比较
        if node.val < pre_num:
            return False
        else:
            pre_num = node.val
        node = node.right
    return True
