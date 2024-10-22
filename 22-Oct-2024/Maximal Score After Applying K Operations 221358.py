# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        heapify(nums)
        ans = 0
        for _ in range(k):
            curr = -heappop(nums)
            ans += curr
            curr = ceil(curr/3)
            heappush(nums,-curr)
        return ans