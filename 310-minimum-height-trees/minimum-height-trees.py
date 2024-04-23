class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        degree = [0] * n
        root = set(list(range(n)))
        for x,y in edges:
            dic[x].append(y)
            degree[y] += 1
            dic[y].append(x)
            degree[x] += 1
        q = deque([x for x in range(n) if degree[x] == 1])
        # print(q)
        # print(dic)
        while(len(root) > 2):
            length = len(q)
            for _ in range(length):
                curr = q.popleft()
                root.remove(curr)
                for i in dic[curr]:
                    degree[i] -= 1
                    if degree[i] == 1:
                        q.append(i)
        # print(root)
        return list(root)
