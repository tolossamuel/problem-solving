# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        demmy = ListNode(0,head)
        left = demmy
        right = demmy
        x = 0
       
        while(right.next):
            if x< n:
                right = right.next
            else:
                right = right.next
                left = left.next
            x += 1
        # print(left.val)
        left.next = left.next.next


        return demmy.next
