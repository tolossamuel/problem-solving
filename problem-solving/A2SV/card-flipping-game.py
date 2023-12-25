class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        good = 2000
        cant = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                cant.add(fronts[i])
        for i in (fronts + backs):
            if i not in cant:
                good = min(good,i)
        if good == 2000:
            return 0
        return good