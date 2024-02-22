class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        current = ""
        for i in path +"/":
            if i == "/":
                if current == "..":
                    if stack:
                        stack.pop()
                elif current and current != ".":
                    stack.append(current)
                current = ""
            else:
                current += i
        return "/"+"/".join(stack)