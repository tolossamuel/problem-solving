class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
            dic [nums[i]] = 0
        for i in range(len(nums)):
            dic [nums[i]]  += 1
        
        dic = list(dic.keys())
        return max(dic)
        
        
        