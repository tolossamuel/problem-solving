class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        pref = [0]
        ans = 0
        for i in gain:
            pref.append(pref[-1]+i)
            ans = max(ans,pref[-1])
        return ans