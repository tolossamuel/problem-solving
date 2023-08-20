class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        incoming_node = collections.defaultdict(list)
        for x, y in edges:
            incoming_node[y].append(x)
        res = []
        for i in range(n):
            if not incoming_node[i]:
                res.append(i)
        return res