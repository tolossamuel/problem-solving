class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        _sum = sum(nums)
        checker = 0
        for i in range(len(nums)):
            _sum -= nums[i]
            if checker == _sum:
                return i
            checker += nums[i]
        return -1