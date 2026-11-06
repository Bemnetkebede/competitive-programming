class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtracking(i , path):
            if len(path) == k:
               ans.append(path.copy())
               return
            for j in range(i , n+1):
                path.append(j)
                backtracking(j+1 , path)
                path.pop()
        backtracking(1,[])
        return ans
                
