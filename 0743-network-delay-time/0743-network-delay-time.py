class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
        
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        
        heap = [(0, k)]
        
        while heap:
            time, node = heapq.heappop(heap)
            
            if time > distances[node]:
                continue  
            for neighbor, w in graph[node]:
                new_time = time + w
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(heap, (new_time, neighbor))

        max_time = max(distances.values())
        return max_time if max_time < float('inf') else -1
   





        
            