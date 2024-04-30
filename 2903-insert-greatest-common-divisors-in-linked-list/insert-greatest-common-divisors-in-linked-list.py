# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head
        next_temp = head.next
        while(next_temp):
            x = math.gcd(temp.val,next_temp.val)
            new = ListNode(x,next_temp)
            temp.next = new
            next_temp = next_temp.next
            temp = temp.next.next

        return head
        