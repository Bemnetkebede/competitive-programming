class Solution(object):
    def minStartValue(self, nums):
        min_sum = float('inf')
        current_sum = 0
        
        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)
            print(current_sum)
            print(min_sum)
            print(max(1, 1 - min_sum))
        return max(1, 1 - min_sum)

               
            
        