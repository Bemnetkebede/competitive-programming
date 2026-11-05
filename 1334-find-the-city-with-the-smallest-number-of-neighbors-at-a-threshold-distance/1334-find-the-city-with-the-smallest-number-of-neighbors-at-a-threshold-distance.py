class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for v, u, w in edges:
            adj[v].append((u, w))
            adj[u].append((v, w))

        def dijkstra(src):
            dist = [float('inf')] * n
            dist[src] = 0
            heap = [(0, src)]
            while heap:
                d, node = heapq.heappop(heap)
                if d > dist[node]:
                    continue
                for nei, w in adj[node]:
                    if d + w < dist[nei]:
                        dist[nei] = d + w
                        heapq.heappush(heap, (dist[nei], nei))
            return sum(1 for d in dist if d <= distanceThreshold) - 1

        res, min_count = -1, n
        for src in range(n):
            count = dijkstra(src)
            if count < min_count or (count == min_count and src > res):
                res, min_count = src, count
        return res
