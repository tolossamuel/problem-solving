class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        stack = deque()
        _sum = 0
        ans = float("inf")
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum >= k:
                ans = min(ans,i+1)
            front = []
            while(stack and (_sum - stack[0][0] >= k)):
                front = stack.popleft()
            if front:
                ans = min(ans,i - front[1])
            while(stack and stack[-1][0] > _sum):
                stack.pop()
            stack.append([_sum,i])
        return ans if ans != float("inf") else -1
                    
            
