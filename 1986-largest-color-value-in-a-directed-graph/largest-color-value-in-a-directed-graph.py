class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        visit = set()
        cycle = set()
        graph = defaultdict(list)
        for edge in edges: graph[edge[0]].append(edge[1])
        def dfs(node) -> bool:
            if not graph[node]: return True
            cycle.add(node)
            for child in graph[node]:
                if child in cycle:
                    return False
                if child not in visit:
                    if not dfs(child): return False
            cycle.remove(node)
            visit.add(node)
            return True
        for node in range(n):
            if not dfs(node): return -1
        cache = {}
        color_types = list(Counter(colors).keys())
        def dp(node):
            if node in cache: return cache[node]
            local_result = defaultdict(int)
            for child in graph[node]:
                child_result = dp(child)
                for color in color_types:
                    local_result[color] = max(local_result[color], child_result[color])
            local_result[colors[node]] += 1
            cache[node] = local_result
            return local_result
        res = 0
        for node in range(n):
            local_result = dp(node)
            res = max(res, max(list(local_result.values())))
        return res
            

        
            
            
