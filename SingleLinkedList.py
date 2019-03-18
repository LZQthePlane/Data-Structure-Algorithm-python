class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist(object):
    def __init__(self):
        self.head = None
        self.length = 0

    # 判断链表是否为空
    def is_empty(self):
        return self.length == 0

    # 链表添加值操作
    def append(self, data):
        # 转换输入值类型
        node = Node(data)
        # 判断列表是否为空，若是则将head指向当前添加的node
        if self.head is None:
            self.head = node
        else:
            # 遍历该list的node,直到某node不存在next，将要添加的node赋给其作为next，并且length+1
            tmp_node = self.head
            while tmp_node.next:
                tmp_node = tmp_node.next
            tmp_node.next = node
        self.length += 1

    # 链表的插入操作
    def insert(self, data, index):
        if type(index) is int:
            if index > self.length:
                print('index out of range')
            else:
                # 获取要插入的node，以及要被插入位置的前一项node（初始化为head）
                insert_node = Node(data)
                current_node = self.head
                # 若要插入的索引位置为0，即将要插入的node作为head，且其next为原先的head
                if index == 0:
                    insert_node.next = current_node
                    self.head = insert_node
                else:
                    # 将insert的位置移到指定位置
                    while index - 1 > 0:
                        current_node = current_node.next
                        index -= 1
                    # 切换两个node的next指向
                    insert_node.next = current_node.next
                    current_node.next = insert_node
                self.length += 1
        else:
            print('index not int')

    # 链表反转
    def reverse(self):
        # 三指针法
        if not self.head or not self.head.next:
            return self.head
        cur = self.head
        pre = None
        nex = None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        self.head = pre

    # 链表的删除操作
    def delete(self, index):
        if type(index) is int:
            if index < self.length:
                if index == 0:
                    self.head = self.head.next
                else:
                    cur = self.head
                    while index - 1 > 0:
                        cur = cur.next
                        index -= 1
                    cur.next = cur.next.next  # 核心操作
                self.length -= 1
            else:
                print("index out of range")
        else:
            print("index not int")

    # 将某处的节点与其下一节点位置互换
    def swap_pair(self, index):
        if type(index) is not int:
            print('index not int')
            return
        if index < self.length - 1:
            # 链表头两位的swap，双指针法
            if index == 0:
                node1 = self.head
                node2 = self.head.next

                self.head = node2
                node1.next = node2.next
                node2.next = node1
            else:
                # 将指针移动到待置换位置的前一位，四指针法
                cur = self.head
                while index - 1 > 0:
                    cur = cur.next
                    index -= 1
                node1 = cur.next
                node2 = node1.next
                late = node2.next

                cur.next = node2
                node2.next = node1
                node1.next = late
        else:
            print('index out of range')

    # 链表的清空操作
    def clear(self):
        self.head = None
        self.length = 0

    # 链表整体打印操作
    def show(self):
        if self.length == 0:
            print("Linkedlist's is None")
        else:
            tmp = self.head  # 注意这里要将head赋给一个tmp，不能直接使用head进行遍历
            while tmp:
                print(tmp.data, end=' ')
                tmp = tmp.next
            print('\n')


if __name__ == "__main__":
    l = Linkedlist()
    l.append(2)
    l.append(3)
    l.append(5)
    l.append(8)
    l.insert(4, 2)
    l.insert(1, 0)
    l.show()
    l.reverse()
    l.show()
    l.delete(4)
    l.show()
    l.swap_pair(0)
    l.show()
    l.clear()
    l.show()
