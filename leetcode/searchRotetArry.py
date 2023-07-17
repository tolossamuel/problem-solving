class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            result_dict = {num: index for index, num in enumerate(nums)}
            return result_dict[target]
        else:
            return -1