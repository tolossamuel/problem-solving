class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for i in range(len(nums)):
            left.append(left[-1] * nums[i])
            right.append(right[-1] * nums[-i - 1])
        right = right[::-1]
        ans = []
        for i in range(1, len(nums) + 1):
            ans.append(left[i-1] * right[i])
        
        return ans