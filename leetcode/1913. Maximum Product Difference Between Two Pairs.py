class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        l = nums[0]*nums[1]
        r = nums[-1]*nums[-2]
        return (r-l)