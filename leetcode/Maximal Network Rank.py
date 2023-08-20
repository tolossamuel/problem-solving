class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        maxval = 0
        graph = defaultdict(set)
        for src,dest in roads:
            graph[src].add(dest)
            graph[dest].add(src)
        for x in range(n):
            for y in range(x+1,n):
                curentmax = len(graph[x]) + len(graph[y])
                if y in graph[x]:
                    curentmax -= 1
                maxval = max(maxval, curentmax)
        return maxval