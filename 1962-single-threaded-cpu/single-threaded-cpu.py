class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
        heapify(tasks)
        heap = []
        ans = []
        time = tasks[0][0]
     
        # print(tasks)
        while(tasks or heap):

            while(tasks and time >= tasks[0][0]):
                x = heappop(tasks)
                # print(tasks)
                heappush(heap,[x[1],x[2],x[0]])
            # print(heap)
            if heap:
                x = heappop(heap)
                ans.append(x[1])
                time += x[0]
            else:
                if tasks:
                    time = tasks[0][0]

        # print(heap)
        return ans
