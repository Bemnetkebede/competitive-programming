class Solution(object):
    def pivotInteger(self, n):
        total_sum = sum(range(1 , n+1))
        ls = 0
        for i in range(1 , n+1):
            rs = total_sum - ls - i
            if ls == rs:
                return i
            ls += i
        return -1 

