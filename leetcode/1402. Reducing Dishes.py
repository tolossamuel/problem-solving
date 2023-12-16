class Solution(object):
    def maxSatisfaction(self, satisfaction):
        """
        :type satisfaction: List[int]
        :rtype: int
        """
        satisfaction.sort()
        s = sorted(satisfaction, reverse = True)
        extra = 0
        ans = extra
        for i in s:
            extra += i
            if extra < 0:
                return ans
            ans += extra
        return ans
        s = sorted(satisfaction, reverse = True)
