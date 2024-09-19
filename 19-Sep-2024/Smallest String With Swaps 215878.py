# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def find(self,x):
        if x == self.dic[x]:
            return x
        self.dic[x] = self.find(self.dic[x])
        return self.dic[x]
    def union(self,x,y):
        xparent = self.find(x)
        yparent = self.find(y)
        if self.size[xparent] >= self.size[yparent]:
            self.dic[yparent] = xparent
            self.size[xparent] += self.size[yparent]
        else:
            self.dic[xparent] = yparent
            self.size[yparent] = self.size[xparent]
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.dic = {x:x for x in range(len(s))}
        self.size = {x:1 for x in range(len(s))}
        for x,y in pairs:
            self.union(x,y)
        for x in range(len(s)):
            self.find(x)
        ans = defaultdict(list)
        for key in self.dic:
            ans[self.dic[key]].append(s[key])
        for key in ans:
            ans[key] = sorted(ans[key],reverse = True)
        value = []
        for x in range(len(s)):
            value.append(ans[self.dic[x]].pop())
        return "".join(value)
