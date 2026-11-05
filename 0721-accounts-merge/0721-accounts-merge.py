from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        d = defaultdict(list)
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(y, j):
            rooty = find(y)
            rootj = find(j)
            if rooty != rootj:
                parent[rooty] = rootj

        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            for i in acc[1:]:
                if i not in parent:
                    parent[i] = i
                email_to_name[i] = name
                union(acc[1], i) 

        group = defaultdict(list)
        for email in parent:
            root = find(email)
            group[root].append(email)

        res = []
        for root_email, emails in group.items():
            name = email_to_name[root_email]
            res.append([name] + sorted(emails))
        return res
