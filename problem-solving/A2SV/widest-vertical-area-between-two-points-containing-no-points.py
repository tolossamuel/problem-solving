class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort()
        max_diff = 0
        
        for i in range(len(points)-1):
            max_diff = max(points[i+1][0] - points[i][0],max_diff)
        return max_diff