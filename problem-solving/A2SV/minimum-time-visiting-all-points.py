class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        if len(points) == 1:
            return 0
        value = points[0]
        for i  in range(len(points)):
            val = abs(value[0]- points[i][0])
            val2 = abs( value[1]-points[i][1])
            ans += max(val,val2)
            value = points[i]
        return ans