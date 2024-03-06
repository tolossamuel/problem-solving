class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start = [[intervals[i][0],i] for i in range(len(intervals))]
        start.sort()
        ans = []
        for i in range(len(intervals)):
            x = bisect.bisect_left(start,[intervals[i][1],0])
            if x >= len(start):
                ans.append(-1)
            else:
                ans.append(start[x][1])
        return ans

