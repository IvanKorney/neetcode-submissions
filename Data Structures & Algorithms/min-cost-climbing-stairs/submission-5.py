class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)

        for i in range(n-1,-1,-1):
            step1 = cost[i]
            if i + 1 < n:
                step1 += dp[i+1]
            step2 = cost[i]
            if i+2 < n:
                step2 += dp[i+2]
            dp[i] = min(step1,step2)

        return min(dp[0],dp[1])


        def dfs(i):
            if i >= n:
                return 0
            step1 = cost[i] + dfs(i+1)
            step2 = cost[i] + dfs(i+2)
            return min(step1,step2)

        return min(dfs(0),dfs(1))