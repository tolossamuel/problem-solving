class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        dic = Counter(t)
        ans = float("inf")
        string = []
        x,y = 0,0
        set1 = set(t)
        set2 = set()
        dic2 = defaultdict(int)
        while(y < len(s) or x < len(s)):
            if y < len(s) and len(set1) > len(set2):
                if s[y] in dic:
                    dic2[s[y]]  += 1
                    if dic2[s[y]] >= dic[s[y]]:
                        set2.add(s[y])
                y += 1
            else:
                if ans > (y-x):
                    if (y-x >= len(t) and len(dic2) == len(dic)) and set1 == set2:
                        string = [x,y]
                        ans = (y-x)
                if s[x] in dic:
                    dic2[s[x]] -= 1
                    if dic2[s[x]] < dic[s[x]] and len(set2) >= len(set1):
                        set2.remove(s[x])
                    if dic2[s[x]] == 0:
                        dic2.pop(s[x])
                x += 1
        if string == []:
            return ""
        return s[string[0]:string[1]]
            
