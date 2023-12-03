class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        stack = []
        if not s:
           return 0
        
        negative = 1
        checker = True
        for i in range(len(s)):
            if s[i] == "-" and not stack and checker:
                negative *= -1
                checker = False
            elif s[i] == "+" and not stack and checker:
                negative *= 1
                checker = False
            elif s[i].isdigit():
                stack.append(s[i])
            else:
                if not stack:
                    stack.append("0")
                break
     
        if not stack:
            return 0
        ans = "".join(stack)
        print(ans)
        ans = int(ans)
        ans *= negative
        if ans>(2**31 - 1):
            return (2**31 - 1)
        if ans < (-2**31):
            return -2**31
        return ans
