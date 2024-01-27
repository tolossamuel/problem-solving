class node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        temp = self.head
        size = 0
        while temp is not None:
            if size == index:
                return temp.val
            temp = temp.next
            size += 1
        return -1

    def addAtHead(self, val: int) -> None:
        temp = node(val)
        temp.next = self.head
        self.head = temp

    def addAtTail(self, val: int) -> None:
        newval = node(val)
        if self.head is None:
            self.head = newval
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newval

    def addAtIndex(self, index: int, val: int) -> None:
        size = 0
        newval = node(val)
        if index == 0:
            newval.next = self.head
            self.head = newval
            return
        temp = self.head
        while temp is not None and size < index - 1:
            temp = temp.next
            size += 1
        if temp is None:
            return
        newval.next = temp.next
        temp.next = newval

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        size = 0
        temp = self.head
        while temp is not None and size < index - 1:
            temp = temp.next
            size += 1
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)