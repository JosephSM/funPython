class Node(object):
    def __init__(self, item, other=None):
        self.item = item
        self.other = other

    def getItem(self):
        return self.item

    def getOther(self):
        return self.other

    def setItem(self, item):
        self.item = item

    def setOther(self, other):
        self.other = other


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, item):
        newNode = Node(item)
        if self.head:
            node = self.head
            while node.getOther():
                node = node.getOther()
            node.setOther(newNode)
        else:
            self.head = newNode

    def getItem(self, idx):
        node = self.head
        for i in range(idx):
            node = node.getOther()
        return node.getItem()

    def setItem(self, idx, item):
        node = self.head
        for i in range(idx):
            node = node.getOther()
        node.setItem(item)

