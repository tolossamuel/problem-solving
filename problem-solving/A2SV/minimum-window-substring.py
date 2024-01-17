class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
          
            return ""
        if s == t:
            return s
        dic = Counter(t)
        ans = float("inf")
        string = []
        x = 0
        y = 0
        set1 = set(t)
        set2 = set()
        dic2 = defaultdict(int)
        while(y < len(s) or x < len(s)):
            # print(11)
            if y < len(s) and len(set1) > len(set2):
                # print(y)
                if s[y] in dic:
                    dic2[s[y]]  += 1
                    if dic2[s[y]] >= dic[s[y]]:
                        set2.add(s[y])
                
                y += 1
            else:
                if ans > (y-x):
                    if (y-x >= len(t) and len(dic2) == len(dic)) and set1 == set2:
                        # print(123)
                        string = [x,y]
                        ans = (y-x)
                    # print(string)
                if s[x] in dic:
                    dic2[s[x]] -= 1
                    if dic2[s[x]] < dic[s[x]]:
                        try:
                            set2.remove(s[x])
                        except:
                            pass
                    if dic2[s[x]] == 0:
                    
                        dic2.pop(s[x])
                
                x += 1
        if string == []:
            return ""
        return s[string[0]:string[1]]
            
