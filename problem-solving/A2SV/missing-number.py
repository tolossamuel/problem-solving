class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        b=0
        for i in range(len(nums)):
            if (b not in nums):
                return b
            b+=1
        return b