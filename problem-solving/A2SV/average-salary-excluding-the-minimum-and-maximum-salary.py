class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        ans = float(sum(salary))
        ans -= (min(salary) + max(salary))
        ans /= (len(salary) - 2)
        return ans