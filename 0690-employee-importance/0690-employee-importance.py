"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(tuple)
        for emp in employees:
            graph[emp.id] = (emp.importance, emp.subordinates)
        stack = [id]
        visited = set()
        total = 0

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            impo , subs = graph[node]
            total += impo
            for sub in subs:
                if sub not in visited:
                    stack.append(sub)
        return total
                
