# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head == None or head.next == None:
        #     return head
        def recurtions(node):
            if node.next:
                self.left.next = recurtions(node.next)
                self.left = self.left.next
                self.left.next = None
            # print(node.val)
            return node
        dummy = ListNode(0,head)
        self.left = dummy
        self.left.next = recurtions(dummy)
        self.left.next = None
        return dummy.next