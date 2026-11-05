class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {tuple((i)) : tuple((i)) for i in stones}
        rank = {tuple((i)) : 1 for i in stones}
        def find(n):
    
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return True
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1

            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            
            else:
                parent[p1] = p2
                rank[p2] += 1

            return True
            
        for node1 in stones:
            for node2 in stones:
                node1 = tuple((node1))
                node2 = tuple((node2))
                if node1 != node2:
                    if find(node1) != find(node2) and (node1[0] == node2[0] or node1[1] == node2[1]):
                        union(node1, node2)

        table = defaultdict(int)
        for node in stones:
            table[find(tuple(node))] += 1
        
        res = 0
        for val in table.values():
            res += val - 1
        
        return res

        