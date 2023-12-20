class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num = 0
        if (s):
            num = dic[s[-1]]
        for i in range(len(s)-1,0,-1):
            print(s[i-1], s[i])
            if dic[s[i-1]] < dic[s[i]]:
                print(dic[s[i-1]], dic[s[i]])
                print()
                num -= dic[s[i-1]] 
            else:
                num += dic[s[i-1]]
        return num
