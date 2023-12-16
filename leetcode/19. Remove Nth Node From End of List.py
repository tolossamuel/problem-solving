# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        left = head
        for i in range(n):
            if left == None:
                return head.next
            left = left.next
        if left == None:
            return head.next
        while(left.next):
            left = left.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
            
        
