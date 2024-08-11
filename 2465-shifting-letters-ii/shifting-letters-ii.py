class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref = [0]*len(s)
        for i in shifts:
            pref[i[0]] += 1 if i[2] == 1 else -1
            if i[1]+1 < len(s):
                pref[i[1]+1] += -1 if i[2] == 1 else 1
        #     print(pref)
        # print(pref)
        for i in range(1,len(s)):
            pref[i] += pref[i-1]
        ans = []
        # print(pref)
        for i in range(len(pref)):
            x =(ord(s[i])-97 + pref[i])%26
            ans.append(chr(x+97))
        
        return "".join(ans)
