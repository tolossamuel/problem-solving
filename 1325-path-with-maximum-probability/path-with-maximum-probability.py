class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            adj[a].append((b, succProb[i]))
            adj[b].append((a, succProb[i]))
        
        prob = [0] * n
        prob[start] = 1.0
        
        pq = [(-1.0, start)]
        while pq:
            curr_prob, node = heapq.heappop(pq)
            curr_prob = -curr_prob
            
            if node == end:
                return curr_prob
            
            for neighbor, edge_prob in adj[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
        
        return 0.0