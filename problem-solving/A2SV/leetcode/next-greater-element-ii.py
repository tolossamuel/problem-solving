class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        stack = list(nums)
        stack.reverse()
        ans = []
        for i in range(len(nums)-1,-1,-1):
            if stack[-1] > nums[i]:
                ans.append(stack[-1])
                stack.append(nums[i])
            else:
                while(stack and stack[-1] <= nums[i]):
                    stack.pop()
                if not stack:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
                stack.append(nums[i])
        ans.reverse()
        return ans