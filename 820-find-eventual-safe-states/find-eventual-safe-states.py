class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outGoing = [0] * len(graph)
        path = defaultdict(list)
        for i in range(len(graph)):
            path[i] += graph[i]
        valid = []
        cyclic = set()
        print(outGoing)
        def dfs(point):
            # print(point)
            
            res = True
            for i in path[point]:
                if outGoing[i] == 1:
                    cyclic.add(i)
                    return False
                if outGoing[i] != 2:
                    outGoing[point] = 1
                    res = res and dfs(i)
            if not res:
                cyclic.add(point)
                return res
            outGoing[point] = 2
            valid.append(point)
            return res
        for i in range(len(graph)):
            # print(i)
          
            if outGoing[i] == 0:
                
                dfs(i)
        valid.sort()
        # print(valid,cyclic)
        return valid