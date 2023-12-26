class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        n = len(flips)
        counter = 0
        ans = 0
        _max = 0
        for i in range(n):
            _max = max(_max,flips[i])
            counter += 1
            if _max == counter :
                ans += 1
        return ans