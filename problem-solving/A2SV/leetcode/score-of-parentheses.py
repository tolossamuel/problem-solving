class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        counter = 0
        for i in s:
            if i == "(":
                stack.append(0)
            else:
                mul = stack.pop()
                if mul == 0:
                    counter = 1
                else:
                    counter = mul * 2
                if not stack:
                    ans += counter
                else:
                    stack[-1] += counter
        return ans