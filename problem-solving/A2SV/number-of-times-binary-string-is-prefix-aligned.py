class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        n = len(flips)
        zeros = "0"*n
        ans = 0
        _max = 0
        for i in range(n):
            zeros = zeros[:flips[i]-1] + "1" + zeros[flips[i]:]
            _max = max(_max,flips[i]-1)
            if zeros[:_max+1] == "1"*(_max+1) and zeros[_max+1:] == "0"*(n-_max-1):
                ans += 1
        return ans