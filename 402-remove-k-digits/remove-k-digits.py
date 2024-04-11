class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        stack  = deque([num[0]])
        size = len(num) - k
        for i in range(1,len(num)):
            while(stack and stack[-1] > num[i] and k > 0):
                stack.pop()
                k -= 1
            if len(stack) < size:
                stack.append(num[i])
            else:
                k -= 1
        # print(stack)
        stack = deque(stack)
        while(stack and stack[0] == "0"):
            stack.popleft()
    
        stack = "".join(stack) if stack else "0"
        return stack