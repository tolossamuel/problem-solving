class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        heap = defaultdict(list)
        degree = [0] * n
        for x,y in edges:
            heap[x].append(y)
            heap[y].append(x)
            degree[x] += 1
            degree[y] += 1
        
        root = set(list(range(n)))
        start = deque([x for x in range(len(degree)) if degree[x] == 1])
        print(start)
        ans = deque([])
        while(len(root) > 2):
            length = len(start)
            for _ in range(length):
                current = start.popleft()
                root.remove(current)
                
                for x in heap[current]:
                  
                    degree[x] -= 1
                    if degree[x] == 1:
                        start.append(x)
                   
  

        return list(root)
