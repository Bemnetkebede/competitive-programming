class Solution:
    def maxProfit(self, prices, fee):
        hold, cash = -prices[0], 0

        for price in prices[1:]:
            hold = max(hold, cash - price)             
            cash = max(cash, hold + price - fee)       

        return cash
