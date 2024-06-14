class LinkedList:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def get(self, index: int) -> int:
        
        temp = self.head
        if index >= self.size:
            return -1
        while(temp and index > 0):
            temp = temp.next
            index -= 1
        if index == 0:
            return temp.val
        return -1

    def addAtHead(self, val: int) -> None:
        if not self.head:
            self.head = LinkedList(val)
            self.tail = self.head
        else:
            self.head = LinkedList(val,self.head)
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = LinkedList(val)
            self.tail = self.head
        else:
            self.tail.next = LinkedList(val)
            self.tail = self.tail.next
        self.size += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        
        if index > self.size:
       
            return 
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            temp = self.head
            while(index > 1):
                temp = temp.next
                index -= 1
            newNode = LinkedList(val,temp.next)
            temp.next = newNode
            self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        if index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = self.head
        else:
            prev = None
            current = self.head
            for _ in range(index):
                prev = current
                current = current.next
            prev.next = current.next
            if current == self.tail:
                self.tail = prev
        self.size -= 1
       


    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)