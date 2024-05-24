class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dic = defaultdict(list)
        time = 0
        for x in range(len(manager)):
            if manager[x] == -1:
                time = informTime[x]
                continue
            dic[manager[x]].append(x)
        start = deque([[headID,time]])
        level = -1
        while(start):
            n = len(start)
            for _ in range(n):
                cur,t = start.popleft()
                time = max(t,time)
                for x in dic[cur]:
                    start.append([x,t+informTime[x]])
            level += 1
        return time