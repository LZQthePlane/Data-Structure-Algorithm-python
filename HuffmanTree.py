"""
哈夫曼树又称最优二叉树，哈夫曼编码是一种变长编码方式
基于最小堆，构造哈夫曼树，效率较高
"""
import queue


class HuffmanTreeNode(object):
    def __init__(self, value=' ', weight=0, left=None, right=None):
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right


class MinHeap(object):
    def __init__(self, n=0):
        self.size = 0
        self.heap = [HuffmanTreeNode()] * n

    def get_parent_node(self, pos):  # 获取父结点
        if (pos-1)/2 >= 0:
            return int((pos-1)/2)
        else:
            return 0

    def sift_up(self, pos):  # 向上调整
        if pos > 0:
            tmppos = pos
            tmp = self.heap[pos]
            while tmppos > 0 and tmp.weight < self.heap[self.get_parent_node(tmppos)].weight:
                self.heap[tmppos] = self.heap[self.get_parent_node(tmppos)]
                tmppos = self.get_parent_node(tmppos)
            self.heap[tmppos] = tmp

    def insert(self, node):  # 插入结点
        self.heap[self.size] = node
        self.size += 1
        self.sift_up(self.size - 1)

    def remove_min(self):  # 移除最小值
        minnode = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        tmp = self.heap[0]
        i = 0
        j = 2*i + 1  # 完全二叉树的子结点
        while j < self.size:
            if j < self.size-1 and self.heap[j].weight > self.heap[j+1].weight:
                j += 1
            if tmp.weight > self.heap[j].weight:
                self.heap[i] = self.heap[j]
                i = j
                j = 2*i + 1
            else:
                break
        self.heap[i] = tmp
        return minnode


def merge_tree(left, right):
    parent = HuffmanTreeNode()  # 零初始化
    parent.left = left
    parent.right = right
    parent.weight = left.weight + right.weight
    return parent


def build_huffman_tree(tree_node_array):
    n = len(tree_node_array)
    # 构造根节点
    root = HuffmanTreeNode()
    # 构建一个大小为n的最小堆，通过insert方法将node依次添加
    min_heap = MinHeap(n)
    for i in range(n):
        tree_node = HuffmanTreeNode(value=tree_node_array[i][0], weight=tree_node_array[i][1])
        min_heap.insert(tree_node)
    heap = min_heap.heap
    print('生成的最小堆为：', end=' ')
    for i in range(min_heap.size):
        print(heap[i].value, end='-')
        print(heap[i].weight, end='\t')
    print()

    # 哈夫曼树的构造过程
    for i in range(n-1):
        # 不断将min_heap中weight最小的两个节点merge，生成的父节点的weight大小为两个子节点weight的和
        child1 = min_heap.remove_min()
        child2 = min_heap.remove_min()
        parent = merge_tree(child1, child2)
        # 将生成的parent节点再插入min_heap中
        min_heap.insert(parent)
        root = parent
    return root


if __name__ == '__main__':
    treenodearray = [['a', 5],
                     ['b', 29],
                     ['c', 7],
                     ['d', 8],
                     ['e', 14],
                     ['f', 23],
                     ['g', 3],
                     ['h', 11]]
    root = build_huffman_tree(treenodearray)
    tmp = root
    encodedict = {}
    rootcode = [root, '']
    deque = queue.Queue()
    deque.put(rootcode)
    while not deque.empty():  # 对字符生成Huffman编码，左边加0，右边加1
        node = deque.get()
        treenode = node[0]
        strnode = node[1]
        if treenode.left is not None:
            deque.put([treenode.left, strnode+'0'])
        if treenode.right is not None:
            deque.put([treenode.right, strnode+'1'])
        if treenode.left is None and treenode.right is None:
            encodedict.setdefault(treenode.value, strnode)
    for key in encodedict.keys():
        print(key, end='--')
        print(encodedict[key])
