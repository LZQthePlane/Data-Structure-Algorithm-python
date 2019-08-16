"""
判断一棵二叉树是否为完全二叉树（除最后一层外，其他层都完全填充，且最后一层向左对其）

"""


def isCbt(root):
    if not root:
        return False
    