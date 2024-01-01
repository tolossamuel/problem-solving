class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        arr = []
        for i in points:
            arr.append([sqrt(i[0]**2 + i[1]**2),i])
        arr.sort()
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        return ans
