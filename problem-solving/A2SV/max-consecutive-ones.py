class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        value = 0
        counter = 0
        for i in nums:
            if i!= 1:
                value = max(value,counter)
                counter = 0
            else:
                counter+= 1
        value = max(value,counter)
        return value