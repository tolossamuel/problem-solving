class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        stack = deque()
        size = float("inf")
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum >= k:
                size = min(size,i+1)
            front = [-1,-1]
            while(stack and (_sum - stack[0][0]) >= k):
                front  = stack.popleft()
            if front != [-1,-1]:
                size = min(size,(i - front[1]))
            while(stack and stack[-1][0] >= _sum):
                stack.pop()
            stack.append([_sum,i])
        return size if size  != float("inf") else -1
        # while(stack):
        #     if (stack[-1] - stack[0]) >= k:
                
        #         stack.popleft()
        #         size = min(size,len(stack))
        #     else:
        #         break
        # print(size)
        # return 3

                    
            
