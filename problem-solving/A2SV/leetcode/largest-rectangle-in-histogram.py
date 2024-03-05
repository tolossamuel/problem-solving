class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        _max = 0
        inc = 1
        for i in heights:
            if not stack:
                stack.append(i)
            elif stack[-1] <= i:
                stack.append(i)
            else:
                count = 0
                
                while(stack and stack[-1] > i):
                    x = stack.pop()
                    count += 1
                    _max = max(_max,(inc * x))
                    inc += 1
                stack.append(i)
                stack += ([stack[-1]] * count)
                count = 0
                inc = 1
        while(stack):
            x = stack.pop()
            _max = max(_max,(inc * x))
            inc += 1
        return _max