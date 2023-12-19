class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        stack = ""
        ans = ""
        for i in command:
            if i == ")":
                if stack[-1] == "(":
                    ans += "o"
                    stack = ""
                else:
                    ans += stack[1:]
                    stack = ""
            elif i == "(":
                stack += "("
            elif stack:
                stack += i
            else:
                ans += i
        return ans



