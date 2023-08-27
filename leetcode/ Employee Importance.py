"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        hash_map = {employee.id: employee for employee in employees }
        def dfs(id):
            sum_of = hash_map[id].importance
            for x in hash_map[id].subordinates:
                sum_of += dfs(x)
            return sum_of
        return dfs(id)