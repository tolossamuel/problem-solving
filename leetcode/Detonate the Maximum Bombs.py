class Solution(object):
    def maximumDetonation(self, bombs):
        """
        :type bombs: List[List[int]]
        :rtype: int
        """
        adj = collections.defaultdict(list)
        for i in range(len(bombs)):
            for y in range(i+1, len(bombs), +1):
                x1,y1,r1 = bombs[i]
                x2,y2,r2 = bombs[y]
                distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
                if distance <= r1:
                    adj[i].append(y)
                if distance <= r2:
                    adj[y].append(i)
        def dfs(distance, visited):
            if distance in visited:
                return 0
            visited.add(distance)
            for x in adj[distance]:
                dfs(x, visited)
            return len(visited)
        result = 0
        for i in range(len(bombs)):
            result = max(result, dfs(i, set()))
        return result