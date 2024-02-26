class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [[height[0],0]]
        between = 0
        ans = 0
        for i in range(1,len(height)):
            if stack[-1][0] > height[i]:
                diff = i - stack[-1][1] - 1
                ans += (min(stack[-1][0],height[i]) * diff)
                stack.append([height[i],i])
            else:
                diff = i - stack[-1][1] - 1
                ans += ((min(stack[-1][0],height[i]) * diff))
                while(stack and stack[-1][0] <= height[i]):
                    if len(stack) > 1:
                        diff = i - stack[-2][1] - 1
                        between = (stack[-1][0]) * (i- stack[-2][1] - 1)
                        ans += ((min(stack[-2][0],height[i]) * diff))
                        ans -= between
                    stack.pop()
                stack.append([height[i],i])
                between = 0
        return ans

