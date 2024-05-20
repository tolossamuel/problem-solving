class Solution:
    def calculate(self, s: str) -> int:
        s.strip()
        s.rstrip()
        stack = []
        val = []
        num = 0
        def cal(x,y,sign):
            if sign == "+":
                return x+y
            elif sign == "/":
                return x//y
            elif sign == "*":
                return x*y
            elif sign == "-":
                return x-y
        s += "("
        for i in s:
            if i == " ":
                continue
            if i in "+*/-(":
                if stack and (stack[-1] == "/" or stack[-1] == "*"):
                    x = val.pop()
                    y = num
                    sign = stack.pop()
                    ans = cal(x,y,sign)
                    val.append(ans)
                else:
                    val.append(num)
                if i == "(":
                    continue
                stack.append(i)
                num = 0
                continue
            num *= 10
            num += int(i)
        stack.reverse()
        val.reverse()
        while(stack):
            y = val.pop()
            x = val.pop()
            val.append(cal(y,x,stack.pop()))
        return val[-1]