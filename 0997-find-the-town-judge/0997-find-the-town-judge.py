class Solution(object):
    def findJudge(self, n, trust):
        g = [[] for _ in range(n)]
        for u , v in trust:
            g[u-1].append(v)
        for i in range(len(g)):
            if len(g[i]) == 0:
                for j in range(len(g)):
                    if i+1!=j+1 and  i+1 not in g[j]:
                       return -1
                return i + 1
        return -1
