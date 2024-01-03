class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        unique_ptr = 1
        for ix in range(1, len(nums)):
            if nums[ix] != nums[ix-1]:
                nums[unique_ptr] = nums[ix]
                unique_ptr += 1

        return unique_ptr
