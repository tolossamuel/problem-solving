# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        _max = float("-inf")
        _min = float("inf")
        left = 0
        right = indexDifference
        max_index = -1
        min_index = -1
        while(right < len(nums)):
            max_index = left if _max < nums[left] else max_index
            min_index  = left if _min > nums[left] else min_index
            _max = max(_max,nums[left])
            _min = min(_min,nums[left])
            if abs(_max - nums[right])>=valueDifference:
                
                return [max_index,right]
            if abs(_min - nums[right]) >= valueDifference:

                return [min_index, right]
            left += 1
            right += 1
        return [-1,-1]
