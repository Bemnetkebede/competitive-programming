class Solution(object):
    def equationsPossible(self, equations):
        parent = {}

        def find(x):
            if x != parent.setdefault(x, x):
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

       
        for eq in equations:
            if eq[1:3] == "==":
                a, b = eq[0], eq[3]
                union(a, b)

        for eq in equations:
            if eq[1:3] == "!=":
                a, b = eq[0], eq[3]
                if find(a) == find(b):
                    return False

        return True

                
                

            
        