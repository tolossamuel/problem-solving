# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        remider = 0
        new_node = None
        def travel(node):
            nonlocal new_node
            nonlocal remider
            if not node:
                return 
            travel(node.next)
            value = (node.val*2) + remider
            remider = value//10
            value %= 10
            temp = ListNode(value,new_node)
            new_node = temp
            return node
        travel(head)
        if remider:
            temp = ListNode(remider,new_node)
            new_node = temp
        return new_node
