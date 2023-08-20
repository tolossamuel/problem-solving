class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        center = [0]*(len(edges)+2)
        for i in range(len(edges)):
            for y in range(len(edges[i])):
                center[edges[i][y]]+=1
        return center.index(max(center))