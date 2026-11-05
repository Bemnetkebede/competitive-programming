import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            prob = succProb[i]
            adj[u].append((v, prob))
            adj[v].append((u, prob))

        
        max_heap = [(-1.0, start_node)]  
        dist = [0.0] * n
        dist[start_node] = 1.0

        while max_heap:
            current_prob_neg, node = heapq.heappop(max_heap)
            current_prob = -current_prob_neg  

            
            if current_prob < dist[node]:
                continue

            for neighbor, edge_prob in adj[node]:
                new_prob = current_prob * edge_prob
                if new_prob > dist[neighbor]:
                    dist[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))

        return dist[end_node]
                

        
        
        