class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        n = len(prices)

        def dfs(i,cp):
            if i >= n:
                return 0
            if (i,cp) in memo:
                return memo[(i,cp)]
            price = 0
            if cp == -1:
                price = max(dfs(i+1,cp),dfs(i+1,prices[i]))
            else:
                price = max(dfs(i+2,-1)+prices[i]-cp,dfs(i+1,cp))
            
            memo[(i,cp)] = price
            return price

        return dfs(0,-1)