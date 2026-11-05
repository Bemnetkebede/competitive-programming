from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def checker(mid , matrix, target):
            return matrix[mid][0] > target
        low = 0
        high = len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
            if checker(mid , matrix, target):
                high = mid - 1
            else:
                low = mid + 1
        
        l = 0
        h = len(matrix[high]) - 1
        print(high , matrix[high])
        while l <= h:
            mid = (l + h) // 2
            print(matrix[high][mid])
            if matrix[high][mid] == target:
                    return True
            elif matrix[high][mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        return False
        
     