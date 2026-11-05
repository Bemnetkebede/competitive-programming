class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = list(range(1 , n + 1))
        x = 0
        idx = 0
        while len(arr) > 1:
            x += 1
            if k == x:
                arr.pop(idx)
                x = 0
            else:
                idx +=1 
        
            idx = idx % len(arr)
        return arr[0]
                
           

                
                
        


