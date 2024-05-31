class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        print(path)
        for i in path:

            if i == "..":
                if stack:
                    stack.pop()
            elif i and i != ".":
                stack.append(i)
            
            
        return "/"+ "/".join(stack)