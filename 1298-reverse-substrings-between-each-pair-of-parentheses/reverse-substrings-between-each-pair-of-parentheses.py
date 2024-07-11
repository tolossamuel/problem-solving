class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        ans = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(len(ans))
            elif s[i] == ")":
                pos = stack.pop()
                n = len(ans)-1
                ans = ans[:pos] + ans[pos:][::-1]
            else:
                ans.append(s[i])
           
        ans = "".join(ans)
        return ans