class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        midle = float("-inf")
        for i in range(len(nums)-1,-1,-1):
            while(stack and stack[-1] < nums[i]):
                midle = max(stack.pop(),midle)
            if not stack:
                stack.append(nums[i])
            else:
                if nums[i] < stack[0] and nums[i] < midle:
                    return True
                stack.append(nums[i])
        return False
