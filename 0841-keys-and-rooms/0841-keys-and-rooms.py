class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        queue = deque(rooms[0])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                    queue.extend(rooms[node])
        return len(rooms) == len(visited)
