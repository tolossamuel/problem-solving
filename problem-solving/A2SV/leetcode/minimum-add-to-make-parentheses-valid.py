class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        counter = 0
        dic ={")":0}
        for i in range(len(s)-1,-1,-1):
            if s[i] == ")":
                dic[")"] += 1
            else:
                if dic[")"] == 0:
                    counter += 1
                else:
                    dic[")"] -= 1
        return counter + dic[")"]