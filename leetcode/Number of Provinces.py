class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)
        visited = set()
        counter = 0
        for start in range(len(isConnected)):
            if start not in visited:
                counter += 1
                dfs(start)
        return counter