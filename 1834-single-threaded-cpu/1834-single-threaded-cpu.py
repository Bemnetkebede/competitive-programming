from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed_tasks = []
        for i in range(len(tasks)):
            enqueue, process = tasks[i]
            indexed_tasks.append([enqueue, process, i])

        indexed_tasks.sort()

        res = [] 
        min_heap = []  
        time = 0
        i = 0 
        n = len(tasks)

        while i < n or min_heap:
            while i < n and indexed_tasks[i][0] <= time:
                enqueue, process, idx = indexed_tasks[i]
                heapq.heappush(min_heap, (process, idx))
                i += 1

           
            if min_heap:
                process, idx = heapq.heappop(min_heap)
                time += process
                res.append(idx)
            else:
                time = indexed_tasks[i][0]

        return res
