class Solution(object):
    def isBipartite(self, graph):
        color = {}

        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if neighbor not in color:
                    if not dfs(neighbor, -c):
                        return False
                elif color[neighbor] == c:
                    return False
            return True

        for node in range(len(graph)):  
            if node not in color:
                if not dfs(node, 1):
                    return False
        return True
