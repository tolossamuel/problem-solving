# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        temp = head
        while(temp):
            size += 1
            temp = temp.next
        print(size)
        size //= 2
        temp = head
        while(size):
            size -= 1
            temp = temp.next
        return temp