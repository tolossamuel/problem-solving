class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<1:
            return 0
        left = 0
        result = 0
        for i in range(len(nums)-1):

            left = i + 1
            while(left +1<= len(nums)):
                if nums[i]== nums[left]:
                    result += 1
                left += 1
        return result
        