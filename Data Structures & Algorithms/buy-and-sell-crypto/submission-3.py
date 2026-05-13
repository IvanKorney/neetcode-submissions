class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0,1
        maxProfit = 0
        while r < len(prices):
            profit = prices[r]-prices[l]
            if profit < 0:
                l = r
            else:
                maxProfit = max(profit,maxProfit)
            r += 1
        return maxProfit
