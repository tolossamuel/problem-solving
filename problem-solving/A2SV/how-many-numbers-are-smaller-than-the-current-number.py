class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        list1 = list(nums)
        list1.sort()
        dic = {}
        for i in range(len(list1)):
            
            if list1[i] not in dic:
                dic[list1[i]] = i
        for i in range(len(nums)):
            list1[i] = dic[nums[i]]
        return list1

        