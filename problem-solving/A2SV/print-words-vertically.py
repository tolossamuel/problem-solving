class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # lsit1 = list(s).spliet("")
        s = s.split(" ")
        

        m = max(s, key = len)
        ans = []
        
        for i in range(len(m)):
            temp = ""
            for y in range(len(s)):
                if i < len(s[y]):
                    temp +=(s[y][i])
                else:
                    temp += " "
            while(temp[-1] == " "):
                temp = temp[:len(temp) - 1]
            ans.append(temp)
        return ans