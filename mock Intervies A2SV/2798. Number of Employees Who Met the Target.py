class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        counter = 0
        for _ in hours:
            if _ >= target :
                counter += 1
        return counter 