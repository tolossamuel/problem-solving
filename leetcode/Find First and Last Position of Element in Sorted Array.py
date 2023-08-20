class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c=0
        b=0
        if(target in nums):
            b=nums.index(target)
            for i in range(len(nums)):
                if(target==nums[i]):
                    c=i
        else:
            b=-1
            c=-1
        d=[b,c]
        return (d)
        zl