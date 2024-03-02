class Solution:
   
    def longestNiceSubstring(self, s: str) -> str:
        up = set()
        low = set()
        _max = []
        ans = []
        checker = set()
        for i in range(len(s)):
            for y in range(i,len(s)):
                if s[y].islower():
                    low.add(s[y])
                else:
                    up.add(s[y])
                checker.add(s[y].lower())
                ans.append(s[y])
                if len(low) == len(up) and checker == low:
                    _max = max(_max,ans.copy(), key = len)
                # print(ans,up,low,checker)
            checker = set()
            up = set()
            low = set()
            ans = []
        # print(_max)
        return "".join(_max)