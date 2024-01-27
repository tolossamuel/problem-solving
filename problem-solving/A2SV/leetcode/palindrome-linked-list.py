# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list1 = []
        list2 = deque()
        while(head):
            list1.append(head.val)
            list2.appendleft(head.val)
            head = head.next
        # print(list2,list1)
        if list1 == list(list2):
            return True
        
        return False