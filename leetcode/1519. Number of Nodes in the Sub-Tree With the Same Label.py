class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        node = defaultdict(list)
        for a, b in edges : 
            node[a].append(b)
            node[b].append(a)
        
        ans = [0] * n
        
        def dfs(n, parent) : 
            
            c = '' 
            for child in node[n] : 
               
                if child != parent : 
                    c += dfs(child, n) 
            c += labels[n]
            ans[n] = c.count(labels[n])
            return c 
        
        dfs(0, -1)
        return ans
		