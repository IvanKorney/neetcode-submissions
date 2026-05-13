class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def minFrom(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo [i]
            stepOnce = cost[i] + minFrom(i+1)
            stepTwice = cost[i] + minFrom(i+2)
            memo[i] = min(stepOnce,stepTwice)
            return memo[i]
        
        return min(minFrom(0),minFrom(1))
