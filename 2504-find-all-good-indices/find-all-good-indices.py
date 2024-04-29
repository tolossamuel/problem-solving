class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        stack = []
        visited = set()
        for i in range(len(nums)):
            if len(stack) >= k:
                visited.add(i)
            if (stack and stack[-1] < nums[i]):
                stack = []
            stack.append(nums[i])
    
        stack = []
        ans = []
        for i in range(len(nums)-1,-1,-1):
           
            if len(stack) >= k and i in visited:
                ans.append(i)
            if (stack and stack[-1] < nums[i]):
                stack = []
            stack.append(nums[i])
        ans.reverse()
        return ans

