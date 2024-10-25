# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        dic = {x:float("-inf") for x in range(n)}
        graph = defaultdict(list)
        for i in range(len(edges)):
            x,y = edges[i]
            p = succProb[i]
            graph[x].append([p,y])
            graph[y].append([p,x])

        dic[start] = 1
        queue = deque([(1,start)])
        while(queue):
            p,curr = queue.popleft()
           
            for x,y in graph[curr]:
                if p*x > dic[y]:
                    dic[y] = p*x
                    queue.append((p*x,y))

                

        if dic[end] == float("-inf"):
            return 0
        return dic[end]