class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        ans = 0
        for l in s:
            if x >= y:
                if l == "a":
                    stack.append("a")
                elif l == "b":
                    if stack and stack[-1] == "a":
                        stack.pop()
                        ans += x
                    else:
                        stack.append("b")
                else:
                    stack.append(l)
            else:
                if l == "b":
                    stack.append("b")
                elif l == "a":
                    if stack and stack[-1] == "b":
                        stack.pop()
                        ans += y
                    else:
                        stack.append("a")
                else:
                    stack.append(l)
        s = "".join(stack)
        stack = []
        for l in s:
            if y < x:
                if l == "b":
                    stack.append("b")
                elif l == "a":
                    if stack and stack[-1] == "b":
                        stack.pop()
                        ans += y
                    else:
                        stack.append("a")
                else:
                    stack.append(l)
            else:
                if l == "a":
                    stack.append("a")
                elif l == "b":
                    if stack and stack[-1] == "a":
                        stack.pop()
                        ans += x
                    else:
                        stack.append("b")
                else:
                    stack.append(l)
        return ans

                
