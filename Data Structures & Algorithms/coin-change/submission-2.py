class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(i,count,cur):
            if i == len(coins) or count > amount:
                return float('inf')
            if count == amount:
                return cur
            if (i,count,cur) in memo:
                return memo[(i,count,cur)]
            take = dfs(i,count + coins[i], cur + 1)
            skip = dfs(i+1,count,cur)
            memo[(i,count,cur)] = min(take,skip)
            return memo[(i,count,cur)]
        return dfs(0,0,0) if dfs(0,0,0) != float("inf") else -1
