# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
      
        dummy = ListNode(-1,head)
        temp = dummy
        dummy
        nums = set(nums)
        while(temp.next):
            if temp.next.val in nums:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return dummy.next