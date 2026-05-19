class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        n = len(cost)
        memo = {}
        def dfs(i):
            if i >= n:
                return 0
            
            if i in memo:
                return memo[i]
            
            jump1 = dfs(i+1) + cost[i]
            jump2 = dfs(i+2) + cost[i]
            memo[i] = min(jump1,jump2)
            return memo[i]
        
        return min(dfs(0),dfs(1))