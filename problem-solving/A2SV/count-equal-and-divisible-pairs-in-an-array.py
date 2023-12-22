class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 0
        for i in range(len(nums)-1):
            for y in range(i+1,len(nums)):
                if (i*y)%k==0  and nums[i] == nums[y]:
                    counter += 1
        return counter
        