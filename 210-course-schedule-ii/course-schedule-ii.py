class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        pre_request = defaultdict(list)
        for i,j in prerequisites:
            indegree[i] += 1
            pre_request[j].append(i)
        courseOrder = []
        queue = []
        # print(indegree,pre_request)
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        queue = deque(queue)
        while(queue):
            curr = queue.popleft()
            courseOrder.append(curr)
            for i in pre_request[curr]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        if len(courseOrder) !=  numCourses:
            return []
        return courseOrder