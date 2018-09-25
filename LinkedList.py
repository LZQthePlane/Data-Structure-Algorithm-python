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
    def append(self, node):
        # 首先判断node是否为一个Node对象, 若不是则转换其类型
        if not isinstance(node, Node):
            node = Node(data=node)
        # 判断列表是否为空，若是则将head指向当前添加的node
        if self.is_empty():
            self.head = node
        else:
            # 遍历该list的node,直到某node不存在next，将要添加的node赋给其作为next，并且length+1
            tmp_node = self.head
            while tmp_node.next:
                tmp_node = tmp_node.next
            tmp_node.next = node
        self.length += 1

    # 链表的插入操作
    def insert(self, value, index):
        if type(index) is int:
            if index > self.length:
                print('index value is out of range')
            else:
                # 获取要插入的node，以及要被插入位置的前一项node（初始化为head）
                insert_node = Node(data=value)
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
                # 无论插入位置，length均 + 1
                self.length += 1
        else:
            print('index value is not int')

    # 链表的删除操作
    def delete(self, index):
        if type(index) is int:
            if index <= self.length:
                # 若要删除的位置为0，将head指向原先head的next
                if index == 0:
                    self.head = self.head.next
                else:
                    # 将位置移动到要delete的位置
                    current_node = self.head
                    while index-1 >0:
                        current_node = current_node.next
                        index -= 1
                    # 将要删除的node的前一个node的next指向该要删除node的next，即可在链表中去除指定node
                    current_node.next = current_node.next.next
                # 无论插入位置，length均 -1
                self.length -= 1
            else:
                print("index value out of range")
        else:
            print("index value is not int")

    # 链表的清空操作
    def clear(self):
        self.head = None
        self.length = 0
        print('linked list cleared')

    # 链表整体打印操作
    def print_linked_list(self):
        if self.length == 0:
            print("Linked list's length is 0")
        else:
            tmp_node = self.head
            print("head:", tmp_node.data, end=' ')
            while tmp_node.next:
                tmp_node = tmp_node.next
                print("-->", tmp_node.data, end=' ')
            print('   length = {}\n'.format(self.length))


if __name__ == "__main__":
    l = Linkedlist()
    l.append(2)
    l.append(3)
    l.append(5)
    l.insert(4, 2)
    l.insert(1, 0)
    l.print_linked_list()
    l.delete(4)
    l.print_linked_list()
    l.clear()
    l.print_linked_list()