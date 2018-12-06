class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.pre = None
        self.next = None


class DoubleListLink(object):
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.length = 0

    def append(self, data):
        node = Node(data)
        if self.head.data is None:
            self.head = node
        pre = self.tail.pre
        pre.next = node
        node.next = self.tail
        self.tail.pre = node
        node.pre = pre
        self.length += 1

    def show(self):
        if self.length == 0:
            print('doubleListLink is None')
        else:
            tmp = self.head
            while tmp:
                print(tmp.data, end=" ")
                tmp = tmp.next
            print('\n')


if __name__ == "__main__":
    dl = DoubleListLink()
    dl.append(2)
    dl.append(3)
    dl.show()