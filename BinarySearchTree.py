"""
二叉搜索树(Binary Search Tree)，又名二叉排序树(Binary Sort Tree)。
（1）若左子树不为空，则左子树上所有节点的值均小于或等于它的根节点的值。
（2）若右子树不为空，则右子树上所有节点的值均大于或等于它的根节点的值。
（3）左、右子树也分别为二叉搜索树.
"""


class TreeNode(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BST(object):
    """
    二叉搜索树基本操作
    """
    def insert(self, bin_tree, x):
        """插入操作"""
        if bin_tree is None:
            bin_tree = TreeNode(data=x)
        elif x < bin_tree.data:
            bin_tree.left = self.insert(bin_tree.left, x)
        elif x > bin_tree.data:
            bin_tree.right = self.insert(bin_tree.right, x)
        return bin_tree

    def find(self, bin_tree, x):
        """搜索操作, 递归实现"""
        if bin_tree is None:
            return False
        if x < bin_tree.data:
            return self.find(bin_tree.left, x)
        elif x > bin_tree.data:
            return self.find(bin_tree.right, x)
        elif x == bin_tree.data:
            print("Found")
            return bin_tree

    def iter_find(self, bin_tree, x):
        """搜索操作，迭代实现"""
        while bin_tree:
            if x < bin_tree.data:
                bin_tree = bin_tree.left
            elif x > bin_tree.data:
                bin_tree = bin_tree.right
            else:
                print("Found")
                return bin_tree
        print("Not found")

    def find_max(self, bin_tree):
        """查询最大值，递归实现"""
        if bin_tree is None:
            return
        elif bin_tree.right:
            return self.find_max(bin_tree.right)
        else:
            return bin_tree

    def find_min(self, bin_tree):
        """查询最小值，迭代实现"""
        if bin_tree:
            while bin_tree.left:
                bin_tree = bin_tree.left
        return bin_tree

    def delete(self, bin_tree, x):
        """删除操作，删除值为x的点"""
        if bin_tree is None:
            print('element not found')
        if x < bin_tree.data:
            bin_tree.left = self.delete(bin_tree.left, x)
        elif x > bin_tree.data:
            bin_tree.right = self.delete(bin_tree.right, x)
        elif x == bin_tree.data:
            # 当找到时，分为两种情况：无子树+有单个子树、有左右两个子树
            if bin_tree.left and bin_tree.right:
                # 即有左子树，又有右子树时
                # 先找到右子树中的最小值节点，用其代替被删除节点，再删除右子树中的最小节点
                tmp = self.find_min(bin_tree.right)
                bin_tree.data = tmp.data
                bin_tree.right = self.delete(bin_tree.right, tmp.data)
            else:
                # 若没有子树或者只有一个子树
                if bin_tree.left is None:
                    bin_tree = bin_tree.right
                elif bin_tree.right is None:
                    bin_tree = bin_tree.left
        return bin_tree

    def print_tree(self, bin_tree):
        """中序遍历"""
        if bin_tree is None:
            return
        self.print_tree(bin_tree.left)
        print(bin_tree.data, end=' ')
        self.print_tree(bin_tree.right)


List = [17, 5, 35, 2, 11, 29, 38, 9, 16, 8]
tree = None
bst = BST()
for val in List:
    tree = bst.insert(tree, val)
print('中序打印二叉搜索树：', end=' ')
bst.print_tree(tree)

print('\n查询值16')
print(bst.iter_find(tree, 7))

print('树中最大值为:', bst.find_max(tree).data)
print('树中最小值为:', bst.find_min(tree).data)

print('删除树中值为5的节点:', end=' ')
tree = bst.delete(tree, 5)
bst.print_tree(tree)
