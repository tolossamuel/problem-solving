class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max_dif = 0
        for i in range(len(nums)-1):
            if max_dif < (nums[i+1] - nums[i]):
                max_dif = nums[i+1] - nums[i]
        return max_dif
