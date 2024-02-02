# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def recurtions(node,x):
            self.last = node.next
            if x < right:
                self.left.next = recurtions(node.next,x +1)
                self.left = self.left.next
                self.left.next = None
            print(node.val)
            return node
        dummy = ListNode(0,head)
        self.left = dummy
        x = 1
        while(self.left):
            if x < left:
                
                self.left = self.left.next
                x +=1
            else:
                # print(self.left.val)
                self.left.next = recurtions(self.left.next,x)
                self.left = self.left.next
                self.left.next = None
                break
        self.left.next = self.last
        # print(self.last.val)
        return dummy.next

