class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
class Solution:
    def __init__(self):
        self.root = Trie()
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        for x in wordDict:
            cur = self.root
            for y in x:
                t = ord(y)%97
                if not cur.children[t]:
                    cur.children[t] = Trie()
                cur = cur.children[t]
            cur.is_end = True
        # print(self.root.child)
        ans = []
        temp = []
        cur = self.root
        def solve(index,word,cur):
            nonlocal temp
            if index >= len(s):
                temp.append(word)
                if cur.is_end:
                # print(temp)
                    ans.append(" ".join(temp))
                temp.pop()
                return 
            if not cur.children[ord(s[index])%97]:
                # print(s[index],word,cur.is_end,temp)
                if cur.is_end:
                    temp.append(word)
                    solve(index,"",self.root)
                    if temp:
                        temp.pop()
                    
                
                return 
            if cur.is_end:
                temp.append(word)
                solve(index,"",self.root)
                if temp:
                    temp.pop()
                solve(index+1,word+s[index],cur.children[ord(s[index])%97])
            else:
                
                solve(index+1,word+s[index],cur.children[ord(s[index])%97])
        solve(0,"",self.root)
        print(ans)
        return ans

