class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        if k >= 25:
            return len(s)
        letter = "abcdefghijklmnopqrstuvwxyz"
        dic = {}
        def cal(x,c):
            val = 0
            for i in range(max(0,x-k),min(len(letter),x+k+1)):
                if letter[i] in dic:
                    if dic[letter[i]] > val:
                        val = dic[letter[i]]
            dic[c] = val + 1
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            index = ord(c) - 97
            cal(index,c)
        ans = max(dic.values())
        return ans
