# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        size = 0
        temp = head
        while(temp.next):
            size += 1
            temp = temp.next
        ans = 0
        while(head):
            ans += (2**size)*head.val
            size -= 1
            head = head.next
        return ans
        