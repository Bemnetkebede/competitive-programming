class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res =[]
        visited = set()
        q = deque()
        g = defaultdict(list)
        outdegree = [0] * len(graph)
        for i in range(len(graph)):
            outdegree[i] = len(graph[i])
            for nei in graph[i]:
                g[nei].append(i) 
        for k in range(len(outdegree)):
            if outdegree[k] == 0:
                q.append(k)
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                res.append(x)
                for j in g[x]:
                    outdegree[j] -= 1
                    if outdegree[j] == 0:
                        q.append(j)

                    

        return sorted(res)

            
        