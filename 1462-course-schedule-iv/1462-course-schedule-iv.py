

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        def bfs(x , y):
            visited = set()
            q = deque([x])
            while q:
                node = q.popleft()
                if node == y:
                    return True
                for n in graph[node]:
                    if n not in visited:
                        q.append(n)
                        visited.add(n)
            return False
        return [bfs(x,y) for x,y in queries]

    
        

        