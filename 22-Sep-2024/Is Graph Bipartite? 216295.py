# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def __init__(self):
        self.colors = defaultdict(bool)
    
    def dfs(self, i, graph, parent_color):
        for edge in graph[i]:
            if edge in self.colors:
                if self.colors[edge] == parent_color:
                    return False
            else:
                self.colors[edge] = not parent_color
                if not self.dfs(edge, graph, self.colors[edge]):
                    return False
        return True

        
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        for i in range(len(graph)):
            if i not in self.colors:
                self.colors[i] = True
                if not self.dfs(i, graph, self.colors[i]):
                    return False
        
        return True
