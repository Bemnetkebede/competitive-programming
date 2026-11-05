class Solution(object):
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0

            q = deque()
            q.append((start, 1.0))
            visited = set([start])

            while q:
                node, value = q.popleft()
                if node == end:
                    return value
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, value * graph[node][neighbor]))
            
            return -1.0
        return [bfs(a, b) for a, b in queries]


        
        
        