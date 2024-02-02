# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left = head
        right = head.next
        
        while(right and right.next):
            new = right.next
            right.next = right.next.next
            new.next = left.next
            left.next = new
            left = left.next
            right = right.next
        return head
