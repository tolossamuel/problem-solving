class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indices = {num: i for i, num in enumerate(nums)}

        for k in range(len(operations)):
            target, new_value = operations[k]
            if target in indices:
                index = indices[target]
                nums[index] = new_value
                indices[new_value] = index
                del indices[target]

        return nums
