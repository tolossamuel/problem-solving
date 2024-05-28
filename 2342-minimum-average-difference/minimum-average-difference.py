class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        _sum = sum(nums)
        
        average_dif = float("inf")
        pos = 0
        prefix = 0
        for x in range(len(nums)):
            _sum -= nums[x]
            prefix += nums[x]
            prefix_average = prefix//(x+1)
            if len(nums)-x-1 == 0:
                _sum_average = 0
            else:
                _sum_average = _sum//(len(nums)-x-1)
            temp = abs(prefix_average - _sum_average)
            if average_dif > temp:
                average_dif = temp
                pos = x
        return pos