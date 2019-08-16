"""
判断是否为平衡二叉树（左右子节点的高度差小于等于1，且所有子树也为平衡二叉树）
"""


def isBalancedBst(root):
    # 空树也是平衡的
    if not root:
        return True
    left = getDepth(root.left)
    right = getDepth(root.right)
    # 判断条件
    if right-left <= 1 and isBalancedBst(root.left) and isBalancedBst(root.right):
        return True
    return False


def getDepth(root):
    if not root:
        return 0
    left = getDepth(root.left)
    right = getDepth(root.right)
    return max(left, right) + 1