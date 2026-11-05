class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for start, dest, price in flights:
            graph[start].append((dest, price))
        
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):  
            temp = dist.copy() 
            for u in graph:
                if dist[u] == float('inf'):
                    continue
                for dest, cost in graph[u]:
                    if dist[u] + cost < temp[dest]:
                        temp[dest] = dist[u] + cost
            dist = temp

        return dist[dst] if dist[dst] != float('inf') else -1


            


        