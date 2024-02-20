class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for i in range(len(s)-1,-1,-1):
            if s[i] in dic:
                stack.append(s[i])
            else:
                if stack and dic[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            