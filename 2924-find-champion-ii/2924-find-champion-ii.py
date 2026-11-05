class Solution(object):
    def findChampion(self, n, edges):
        ad = defaultdict(list)
        for a , b in edges:
            ad[b].append(a)
        
        res = []
        for i in range(n):
            if i not in ad:
                res.append(i)
                
        if len(res) == 1:
            return res[0]
        else:
            return -1





        
        