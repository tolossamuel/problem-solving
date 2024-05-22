class Trie:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
class Solution:
    def __init__(self):
        self.root = Trie()
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for x in strs:
            cur = self.root
            if len(x) <= 0:
                return ""
            for y in x:
                t = ord(y)%97
                if not cur.children[t]:
                    cur.children[t] = Trie()
                cur = cur.children[t]
            cur.is_end = True
        cur = self.root
        ans = []
        while(True):
            child = []
            for x in range(len(cur.children)):
                if cur.children[x]:
                    child.append(x)
                if cur.is_end:
                    return "".join(ans)
                
                if len(child) > 1:
                    return "".join(ans)
            if child:
                ans.append(chr(child[0]+97))
                cur = cur.children[child[0]]
            else:
                break
        return "".join(ans)