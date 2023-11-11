class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=-1*k
        d=0
        a=-1
        for i in range(1,k+1,+1):
            d=nums[a]
            nums.pop()
            nums.insert(0,d)