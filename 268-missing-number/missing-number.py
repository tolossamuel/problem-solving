class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = [-1] * (len(nums)+1)
        
        for i in nums:
            temp[i] = i
        for i in range(len(temp)):
            if temp[i] == -1:
                return i