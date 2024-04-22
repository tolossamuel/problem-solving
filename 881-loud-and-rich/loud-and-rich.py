class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        dic = defaultdict(set)
        dependet  = [0] * len(quiet)
        
        for x,y in richer:
            dic[x].add(y)
            dependet[y] += 1
        order =  list(range(len(quiet)))
        visited = [True] * (len(quiet)-1)
        def travel():
          
            q = deque([index for index in range(len(quiet)) if dependet[index] == 0])
            while(q):
                curr = q.popleft()
                for i in dic[curr]:
                    dependet[i] -= 1
                    order[i] = order[i] if quiet[order[curr]] > quiet[order[i]] else order[curr]
                    if dependet[i] == 0:
                        q.append(i)
        travel()
        return order