class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        graph = defaultdict(list)
        for i in range(len(manager)):
            if manager[i] != -1:
                graph[manager[i]].append(i)
        print(graph)
        def dfs(node):
            max_time  = informTime[node]
            for child in graph[node]:
                max_time = max(max_time, informTime[node] + dfs(child))
                
            return max_time

                
        return dfs(headID)