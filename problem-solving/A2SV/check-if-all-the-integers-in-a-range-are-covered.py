class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        ranges.sort()
        for i in range(len(ranges)):
            if ranges[i][0] <= left and ranges[i][1] >= left:
                left = ranges[i][1]+1
                # print(left)
                if left > right:
                    return True
        return False

        