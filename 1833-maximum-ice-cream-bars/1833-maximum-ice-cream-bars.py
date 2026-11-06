class Solution(object):
    def maxIceCream(self, costs, coins):
       total = 0
       count = 0
       costs.sort()
       for i in range(len(costs)):
            if total + costs[i] <= coins:
                total += costs[i]
                count += 1
       else:
            return count

       

          
