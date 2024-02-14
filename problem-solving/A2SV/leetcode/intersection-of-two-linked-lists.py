# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        left = headA
        dic = {}
        while(left):
            dic[left] = 1
            left = left.next
        
        right = headB
        while(right):
            if right in dic:
                return right
            right = right.next