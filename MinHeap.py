from math import inf
"""
优先队列(priority queue)是一种特殊的队列，
取出元素的顺序是按照元素的优先权(关键字)大小，而不是进入队列的顺序，
堆就是一种优先队列的实现。
堆一般是由数组实现的，逻辑上堆可以被看做一个完全二叉树
"""


class MinHeap(object):
    """一个二叉堆, 小顶堆 利用列表实现"""
    def __init__(self, max_size=inf):
        """设置最大size(无限大)，哨兵-inf（最小堆）"""
        self.max_size = max_size
        self.heap = [-inf]  # 用数组实现，逻辑上为完全二叉树，第一个数为最小的哨兵

    def __len__(self):
        """求长度，不包括哨兵元素"""
        return len(self.heap) - 1

    def insert(self, data):
        """向堆中插入元素，复杂度O(logN)"""
        self.heap.append(data)  # heap列表append新元素
        pos = self.__len__()

        if pos > self.max_size:
            print('Heap is full.')
            return
        # 元素插入后，与父节点（pos//2）比较大小，若小则进行上浮操作
        while data < self.heap[pos//2]:
            self.heap[pos] = self.heap[pos//2]
            pos //= 2
        self.heap[pos] = data

    def delete_min(self):
        """删除堆顶元素，复杂度logN"""

        if self.__len__() < 1:
            print('Heap is empty.')
            return
        # 用堆中的最后一个元素替换到根节点，再进行下沉到合适位置
        last_item = self.heap.pop()
        if self.__len__() > 1:  # 如果pop之后只有哨兵，无需进行下沉
            parent_idx = 1
            while True:
                # child_idx为左子节点
                child_idx = parent_idx * 2
                # 如果左子节点的idx大于heap长度，说明该左子节点已经在堆外，即该节点无子节点，应跳出循环
                if child_idx > self.__len__():
                    break
                # 在左右子节点中找更小的那个，即是与父节点进行位置交换的子节点
                # 如果左子节点不为heap的最后一个元素（有右儿子），且右子节点更小，则将待置换的节点换为右子节点
                if child_idx < self.__len__() and self.heap[child_idx] > self.heap[child_idx+1]:
                    child_idx += 1
                # 如果last_item比儿子节点的值大，则不断用儿子替代父节点
                if last_item > self.heap[child_idx]:
                    self.heap[parent_idx] = self.heap[child_idx]
                else:
                    break
                # 儿子节点变为新的父节点
                parent_idx = child_idx
            # 将tmp放到到合适位置
            self.heap[parent_idx] = last_item

    def create_heap(self, list_data):
        """
        直接创建一个小顶堆，效果同insert一个个插入, 效率更高,时间复杂度为n
        """
        # 先将全部元素按输入顺序存入，而后再进行位置上的调整
        self.heap.extend(list_data)
        # 存在父节点的个数
        parent_num = self.__len__()//2
        # 对每一个父节点，进行下沉操作，由下至上，由右至左
        # 与delete_min中的下沉操作相同
        for parent_idx in range(parent_num, 0, -1):
            tmp = self.heap[parent_idx]
            while True:
                child_idx = parent_idx * 2
                if child_idx > self.__len__():
                    break
                if child_idx < self.__len__() and self.heap[child_idx] > self.heap[child_idx+1]:
                    child_idx += 1
                if tmp > self.heap[child_idx]:
                    self.heap[parent_idx] = self.heap[child_idx]
                else:
                    break
                parent_idx = child_idx
            self.heap[parent_idx] = tmp

    def get_min(self):
        if self.__len__() >= 1:
            return self.heap[1]
        else:
            print('Heap is empty')

    def clear(self):
        """清空堆"""
        self.heap = [-inf]


if __name__ == '__main__':
    min_heap = MinHeap()
    min_heap.create_heap([14, 17, 18, 13, 9, 28])
    min_heap.insert(5)
    min_heap.insert(10)
    min_heap.insert(4)
    min_heap.insert(-10)
    min_heap.insert(7)
    min_heap.insert(3)

    min_heap.delete_min()
    min_heap.delete_min()
    min_heap.delete_min()
    min_heap.delete_min()
    a = min_heap.get_min()
    print(a)
    print(min_heap.heap)