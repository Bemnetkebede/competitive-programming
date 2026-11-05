class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        g = defaultdict(list)
        ans = list(range(len(quiet) ))
        print(ans)
        indegree = [0] *  len(quiet) 
        q = deque()
        for i,j in richer:
            g[i].append(j)
            indegree[j] += 1 
        for i , j in enumerate(indegree):
            if j == 0:
                q.append(i)
      
        while q:
                 u = q.popleft()
                 for v in g[u]:
                    if quiet[ans[u]] < quiet[ans[v]]:
                        ans[v] = ans[u]
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        q.append(v)
        return ans

        
        

        