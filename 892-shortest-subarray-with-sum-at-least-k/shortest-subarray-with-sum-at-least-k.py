class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        stack = deque()
        _sum = 0
        ans = float("inf")
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum >= k:
                ans = min(ans,i+1)
            front = [-1,-1]
            while(stack and (_sum - stack[0][0]) >= k):
                front = stack.popleft()
            if front != [-1,-1]:
                ans = min(ans,i - front[1])
            while(stack and stack[-1][0] > _sum):
                stack.pop()
            stack.append([_sum,i])
        if ans == float("inf"):
            return -1
        return ans
                    
            
