# Problem: Maximum Gap - https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_dif = 0
        for i in range(len(nums)-1):
            if max_dif < (nums[i+1] - nums[i]):
                max_dif = nums[i+1] - nums[i]
        return max_dif