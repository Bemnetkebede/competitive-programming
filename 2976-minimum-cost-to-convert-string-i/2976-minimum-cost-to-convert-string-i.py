class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(len(original)):
            adj[original[i]].append((changed[i], cost[i]))
        
        
        memo = {}
        
        def dijkstra(src, dest):
            if src == dest:
                return 0
                
            if (src, dest) in memo:
                return memo[(src, dest)]
            
        
            dist = {}
            dist[src] = 0
            heap = [(0, src)]
            
            while heap:
                current_dist, node = heapq.heappop(heap)
                
                
                if node == dest:
                    memo[(src, dest)] = current_dist
                    return current_dist
                
                
                if current_dist > dist.get(node, float('inf')):
                    continue
                
                
                for neighbor, weight in adj.get(node, []):
                    new_dist = current_dist + weight
                    if new_dist < dist.get(neighbor, float('inf')):
                        dist[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))
            
            result = dist.get(dest, -1)
            if result == float('inf'):
                result = -1
            memo[(src, dest)] = result
            return result
        
        total_cost = 0
        for i in range(len(source)):
            if source[i] != target[i]:
                cost_val = dijkstra(source[i], target[i])
                if cost_val == -1:
                    return -1
                total_cost += cost_val
        
        return total_cost