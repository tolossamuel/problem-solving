class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 1
        right = 0
        counter = 0
        while (right + 2 != len(nums)):
            if left == len(nums):
                right += 1
                left = right + 1
            if (nums[left] + nums[right] < target):
                counter += 1
            left += 1
        
        return counter
            