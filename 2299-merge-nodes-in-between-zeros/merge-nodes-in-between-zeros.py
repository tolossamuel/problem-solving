# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        travel = ans
        temp = head
        _sum = 0
        temp = temp.next
        while(temp):
            if temp.val == 0:
                if ans.val == 0:
                    ans. val = _sum
                else:
                    crete = ListNode(_sum)
                    travel.next= crete
                    travel = travel.next
                _sum = 0
            
            _sum += temp.val
            temp = temp.next
        return ans

