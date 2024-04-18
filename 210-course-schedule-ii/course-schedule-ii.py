class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        color = [0] * numCourses
        pre_request = defaultdict(list)
        for i,j in prerequisites:
            pre_request[i].append(j)
        courseOrder = []
        queue = []
        visited = set()
        def dfs(course):
            res = True
            for i in pre_request[course]:
                if color[i] == 1:
                    return False
                if  color[i] != 2:
                    
                    color[i] = 1
                    res = res and dfs(i)
                
            courseOrder.append(course)
            color[course] = 2
            return res
        for i in range(numCourses):
            if color[i] == 0:
                if not dfs(i):
                    return []
        return courseOrder

