class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]*(len(cost)+1)
        for i in range(len(cost)-1,-1,-1):
            take = cost[i] + dp[i+1]
            if i + 2 < len(dp):
                skip = cost[i] + dp[i+2]
            else:
                skip = cost[i]
            dp[i] = min(take,skip)
        return min(dp[0],dp[1])
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     take = cost[i] + dfs(i+1)
        #     skip = cost[i] + dfs(i+2)
        #     memo[i] = min(take,skip)
        #     return memo[i]
        # return min(dfs(0),dfs(1))