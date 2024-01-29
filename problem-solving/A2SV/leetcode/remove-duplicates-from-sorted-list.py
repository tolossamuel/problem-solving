# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head
        left = head
        right = head.next
        while(right):
            if right.val == left.val:
                left.next = right.next
                right.next = None
                right = left.next
            else:
                right = right.next
                left = left.next
        return head