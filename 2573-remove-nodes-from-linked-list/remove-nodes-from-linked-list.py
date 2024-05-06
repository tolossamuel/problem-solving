# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_node = None
        def remove(node):
            nonlocal new_node
            if not node:
                return 
            remove(node.next)
            if not new_node:
                new_node = ListNode(node.val)
            else:
                if new_node.val <= node.val:
                    temp = ListNode(node.val,new_node)
                    new_node = temp
            return node
        remove(head)
        return new_node