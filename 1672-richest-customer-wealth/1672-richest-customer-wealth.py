class Solution(object):
    def maximumWealth(self, accounts):
        rich = 0
        for i in accounts:
            summ = sum(i)
            if summ > rich:
                rich = summ
        return rich

            
           
        