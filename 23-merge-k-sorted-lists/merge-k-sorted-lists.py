# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        def travel(nums):
            if not nums:
                return 
            travel(nums.next)
            heapq.heappush(heap,nums.val)
            return nums
        for i in lists:
            travel(i)
        ans = None
        head = None
        while(heap):
            x = heapq.heappop(heap)
            if not ans:
                ans = ListNode(x)
                head = ans
            else:
                ans.next = ListNode(x)
                ans = ans.next
        return head