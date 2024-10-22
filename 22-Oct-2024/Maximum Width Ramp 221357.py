# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def bisect_left_deque(self,dq, x):
        low, high = 0, len(dq)
        while low < high:
            mid = (low + high) // 2
            if dq[mid] < x:
                low = mid + 1
            else:
                
                high = mid
                
        return low

    def maxWidthRamp(self, nums: List[int]) -> int:
       
        ans = 0
        
        stack = deque([])
        for x in range(len(nums)):
            curr = nums[x]
            if not stack:
                stack.appendleft([curr,x])
                continue
            index = self.bisect_left_deque(stack,[curr,-1])
            
            if index < len(stack) and stack[index][0] > curr:
                index -= 1
            if index >= len(stack):
                index -= 1
       
            if index < 0 or index >= len(stack):
                if stack[-1][0] > curr:
                    stack.appendleft([curr,x])
                continue
     
            ans = max(ans,x - stack[index][1]) 
          
            if stack[0][0] > curr:
                stack.appendleft([curr,x])
        return ans