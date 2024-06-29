class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        dgree = [0] * n
        ans = [set() for _ in range(n)]
        for i,y in edges:
            dic[i].append(y)
            dgree[y] += 1
        q = deque([x for x in range(n) if dgree[x] == 0])
        # print(len(ans))
        while q:
            curr = q.popleft()
            for i in dic[curr]:
                # print(i)
                ans[i].add(curr)
                ans[i].update(ans[curr])
                dgree[i] -= 1
                if dgree[i] == 0:
                    q.append(i)
        ans = [(sorted(list(s))) for s in ans]
        return ans