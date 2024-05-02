class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        right = len(nums)-1
        left = 0
        while(left < right):
            if -nums[left] == nums[right]:
                return nums[right]
            elif -nums[left] > nums[right]:
                left += 1
            else:
                right -= 1
        return -1