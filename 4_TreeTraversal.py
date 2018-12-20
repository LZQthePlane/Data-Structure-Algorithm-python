class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = Node()
        self.my_queue = []

    def append_node(self, data):
        node = Node(data)
        if self.root.data is None:
            self.root = node
            self.my_queue.append(self.root)
        else:
            tree_node = self.my_queue[0]
            if not tree_node.left:
                tree_node.left = node
                self.my_queue.append(tree_node.left)
            else:
                tree_node.right = node
                self.my_queue.append(tree_node.right)
                self.my_queue.pop(0)


def get_depth(root):
    """
    树的高度
    """
    node = root
    if node is None:
        return 0
    left_depth = get_depth(node.left)
    right_depth = get_depth(node.right)
    return max(left_depth, right_depth) + 1


def level_order_traversal(root):
    """
    层序遍历
    """
    if not root:
        return None
    queue = [root]
    while queue:
        tree_node = queue.pop(0)
        print(tree_node.data, end=',')
        if tree_node.left:
            queue.append(tree_node.left)
        if tree_node.right:
            queue.append(tree_node.right)


def pre_order_recursion(root):
    """
    递归实现前序遍历
    """
    if not root:
        return None
    print(root.data, end=',')
    pre_order_recursion(root.left)
    pre_order_recursion(root.right)


def in_order_recursion(root):
    """
    递归实现中序遍历
    """
    if not root:
        return None
    in_order_recursion(root.left)
    print(root.data, end=',')
    in_order_recursion(root.right)


def post_order_recursion(root):
    """
    递归实现后序遍历
    """
    if not root:
        return None
    post_order_recursion(root.left)
    post_order_recursion(root.right)
    print(root.data, end=',')


def pre_order_stack(root):
    """
    堆栈实现前序遍历
    """
    if not root:
        return None
    my_stack = []
    node = root
    while my_stack or node:
        # 从根节点开始，一直访问左子树
        while node:
            # 第一次访问到node时即打印
            print(node.data, end=',')
            my_stack.append(node)
            node = node.left
        # 当前节点没有左子树，开始访问其右子树
        node = my_stack.pop()
        node = node.right


def in_order_stack(root):
    """
    堆栈实现中序遍历
    """
    if not root:
        return None
    my_stack = []
    node = root
    while my_stack or node:
        while node:
            my_stack.append(node)
            node = node.left
        node = my_stack.pop()
        # 第二次访问到node时打印
        print(node.data, end=',')
        node = node.right


def post_order_stack(root):
    """
    堆栈实现后序遍历
    """
    # 先遍历根节点，再遍历右子树，最后是左子树
    # 这样就可以转化为和先序遍历一个类型了
    # 最后把遍历结果逆序输出
    if not root:
        return None
    my_stack1 = []
    my_stack2 = []
    node = root
    while my_stack1 or node:
        while node:
            my_stack1.append(node)
            my_stack2.append(node)
            node = node.right
        node = my_stack1.pop()
        node = node.left
    while my_stack2:
        print(my_stack2.pop().data, end=',')


if __name__ == '__main__':
    test_tree = BinaryTree()
    for i in range(1, 10):
        test_tree.append_node(data=i)

    print(get_depth(test_tree.root))

    level_order_traversal(test_tree.root)
    print('\n')

    pre_order_recursion(test_tree.root)
    print('')
    pre_order_stack(test_tree.root)
    print('\n')

    in_order_recursion(test_tree.root)
    print('')
    in_order_stack(test_tree.root)
    print('\n')

    post_order_recursion(test_tree.root)
    print('')
    post_order_stack(test_tree.root)
