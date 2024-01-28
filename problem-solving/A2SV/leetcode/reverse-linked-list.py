# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        if not head.next:
            return head
        temp = ListNode(head.val)
        head = head.next
        index = head.next
        while(index):
            head.next = temp
            temp = head
            head = index
            index = index.next
        head.next = temp
   
        return head
