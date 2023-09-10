class Solution(object):
    def longestPath(self, parent, s):
        """
        :type parent: List[int]
        :type s: str
        :rtype: int

        """
        g = defaultdict(list)
        for i, u in enumerate(parent):
            g[u].append(i)
        # print(g)
        self.ans = 0
        
        def dfs(root):
            a1 = a2 = 0
            for v in g[root]:
                if s[v] == s[root]:
                    dfs(v)
                    continue
                curr = dfs(v)
                if curr >= a1:
                    a2 = a1
                    a1 = curr
                elif curr >= a2:
                    a2 = curr
            self.ans = max(self.ans, a1 + a2 + 1)
            return a1 + 1
        
        dfs(0)
        
        return self.ans