# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        _prev_val = head.val
        temp = head.next
        cr_point = []
        point = 2
        _min = float("inf")
        ans = [-1,-1]
        if not temp:
            return ans
        while(temp.next):
            curr = temp.val
            next_val = temp.next.val
            if curr < next_val and curr < _prev_val:
                cr_point.append(point)
               
                
            elif curr > next_val and curr > _prev_val:
                cr_point.append(point)
                
            if len(cr_point) >= 2:
                _min = min(cr_point[-1] - cr_point[-2], _min)
            _prev_val = curr
            point += 1
            temp = temp.next
     
        if len(cr_point) < 2:
            return ans
        ans = [_min,cr_point[-1] - cr_point[0]]
        return ans
        
