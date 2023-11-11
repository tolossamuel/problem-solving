class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # rotate = nums[len(nums)-k:]
        # print(rotate)
        # nums = rotate+ nums[:len(nums)-k]
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k] #
       
        