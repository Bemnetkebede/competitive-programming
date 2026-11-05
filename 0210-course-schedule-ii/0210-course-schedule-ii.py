class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        indegree = [0] * (numCourses)
        q = deque()
        for i , j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        print(indegree)
        print(graph)
        for k in range(numCourses):
            if indegree[k] == 0:
                res.append(k)
                q.append(k)
        while q:
            x = q.popleft()
            for i in graph[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    res.append(i)
                    q.append(i)
        return res if len(res) == numCourses else []


            

