class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict (list)
        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set() 
        stack = [source]
        while stack:
            la = stack.pop()
            if la == destination:
                return True
            if la not in visited:
                visited.add(la)
                for neighbor in graph[la]:
                    if neighbor not in visited:
                        stack.append(neighbor)

        return False
                

