class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[-1]
        _sum = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            _sum = max(nums[i],_sum + nums[i])
            ans = max(ans,(_sum))
        return ans