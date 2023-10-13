# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        small = head
        temp = head
        index = small.next
        char = False
        while small.next != None:
            temp = small
            index = small.next
            while index != None:
                if temp.val > index.val:
                    temp = index
                    char = True
                
                index = index.next
            if char:
                small.val, temp.val = temp.val,small.val
                char = False
            small = small.next
        return head
        
        
                        