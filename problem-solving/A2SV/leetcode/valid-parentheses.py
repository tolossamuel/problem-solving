class Solution:
    def isValid(self, s: str) -> bool:
        dic = defaultdict(int)
        stack = []
        for i in range(len(s)-1,-1,-1):
            if s[i] == ")" or s[i] == "}" or s[i] == "]":
                dic[s[i]] += 1
                stack.append(s[i])
            elif s[i] == "(":
                if dic[")"] > 0 and stack and stack[-1] == ")":
                    dic[")"] -= 1
                    stack.pop()
                else:
                    return False
            elif s[i] == "{":
                if dic["}"] > 0 and stack and stack[-1] == "}":
                    dic["}"] -= 1
                    stack.pop()
                else:
                    return False
            elif s[i] == "[":
                if dic["]"] > 0 and stack and stack[-1] == "]":
                    dic["]"] -= 1
                    stack.pop()
                else:
                    return False
        return max(dic.values()) == 0 
            