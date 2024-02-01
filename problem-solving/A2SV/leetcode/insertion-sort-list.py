# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if head.next == None:
            return head
        def pre(node,prevs):
            prevs.prev = node
        head.prev = None
        while(temp.next):
            pre(temp,temp.next)
            temp = temp.next
        left = head
        right = head
        while(left.next):
            right = left.next
            while(right.prev and right):
                if right.val < right.prev.val:
                    right.val,right.prev.val = right.prev.val,right.val
                    right = right.prev
                else:
                    break
            left = left.next
        return head
