class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        dic = defaultdict(list)
        dgree = [0]*n
        time_max = defaultdict(int)
        for x,y in relations:
            dic[x].append(y)
            dgree[y-1] += 1
        q = deque([(x,time[x-1]) for x in range(1,n+1) if dgree[x-1] ==0])
        _max = 0
        while(q):
            cur,times = q.popleft()
            _max = max(times,_max)
            for c in dic[cur]:
                time_max[c] = max(time_max[c],times)
                dgree[c-1] -= 1
                if dgree[c-1] == 0:
                    time[c-1] += time_max[c]
                    q.append((c,time[c-1]))
        return _max
                

                
