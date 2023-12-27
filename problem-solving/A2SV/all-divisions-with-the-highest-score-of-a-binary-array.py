class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans =[0]
        _max = 0
        zeros = 0
        ones = nums.count(1)
        for i in range(len(nums)+1):
            if i > 0 and nums[i-1] == 0:
                zeros += 1
            temp =zeros +ones
            if _max < temp:
                ans = [i]
                _max = temp
            elif _max == temp:
                ans.append(i)
            if  i == len(nums):
                ones = 0
            elif nums[i] == 1:
                ones -= 1
        return ans
