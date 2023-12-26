class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for y in range(len(nums)-1):
                if(nums[y]>nums[y+1]):
                    nums[y],nums[y+1]=nums[y+1],nums[y]
