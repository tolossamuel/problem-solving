class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zeros = []
        non_zeros = []
        for x in range(1,len(nums)):
            if nums[x] == nums[x-1]:
                nums[x]  = 0
                nums[x-1] *= 2
            if nums[x-1] == 0:
                zeros.append(nums[x-1])
            else:
                non_zeros.append(nums[x-1])
        if nums[-1] == 0:
            zeros.append(nums[-1])
        else:
            non_zeros.append(nums[-1])
        return non_zeros+zeros