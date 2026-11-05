class Solution(object):
    def findRedundantConnection(self, edges):
        n = len(edges)
        res  = []
        parent = [i for i in range(n + 1)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(y,j):
            rooty = find(y)
            rootj = find(j)
            if rooty == rootj:
                return False
            elif rooty != rootj:
                parent[rooty] = rootj
                return True
        for i in edges:
            r , l = i
            if not union(r ,l):
                return i


         
        