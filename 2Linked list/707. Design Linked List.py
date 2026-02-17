class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    # Dummy head and dummy tail nodes
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    # ***** Add (Insert) *****

    def add_last(self, e):
        x = Node(e)
        temp = self.tail.prev

        temp.next = x
        x.prev = temp
        # temp <-> x

        x.next = self.tail
        self.tail.prev = x
        # temp <-> x <-> tail
        self.size += 1

    def add_first(self, e):
        x = Node(e)
        temp = self.head.next
        # head <-> temp

        temp.prev = x
        x.next = temp

        self.head.next = x
        x.prev = self.head
        # head <-> x

if __name__ == "__main__":
    list = MyLinkedList()
    list.add_last(1)
    list.add_last(2)
    list.add_last(3)
    list.add_first(0)
    list.add(2, 100)

    list.display()
    # size = 5
    # 0 <-> 1 <-> 100 <-> 2 <-> 3 <-> null