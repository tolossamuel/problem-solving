class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        val = []
        maxNum = max(candies)
        for i in candies:
            if (i + extraCandies) >= maxNum:
                val.append(True)
            else:
                val.append(False)
        return val