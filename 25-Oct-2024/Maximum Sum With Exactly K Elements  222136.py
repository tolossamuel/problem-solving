# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        _max = max(nums)
        _sum = 0
        for x in range(k):
            _sum += (_max+x)
            
            print(_sum,_max)
        return _sum