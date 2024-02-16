class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        counter = 1
        pos = points[0][1]
        for i in range(1,len(points)):
            if pos < points[i][0]:
                counter += 1
                pos = points[i][1]
            else:
                pos = min(pos,points[i][1])
        return counter
