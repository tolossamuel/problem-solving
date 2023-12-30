class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        counter = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                counter += (len(nums)-1-i)
        return counter

