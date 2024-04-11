class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        ans[0] = 0
        dic = defaultdict(list)
        dic2 = defaultdict(list)
        for i,y in redEdges:
            dic[i].append(y)
        for i,y in blueEdges:
            dic2[i].append(y)
        
        def path(choose):
          
            nonlocal ans
            visited = set((0,0,))
            start = deque([0])
            level = 0
            while(start):
                length = len(start)
                for i in range(length):
                    curr = start.popleft()
                    if ans[curr] == -1:
                        ans[curr] = level
                    else:
                        ans[curr] = min(ans[curr],level)
                    # print("=",level,curr)
                    lists = dic[curr] if choose == 0 else dic2[curr]
                    for y in lists:
                        # print(y)
                        if (curr,y,choose) not in visited:
                            
                            visited.add((curr,y,choose))
                            start.append(y)
                choose = 1 if choose == 0 else 0
                level += 1
        path(0)
        # print("====")
        path(1)
        return ans   