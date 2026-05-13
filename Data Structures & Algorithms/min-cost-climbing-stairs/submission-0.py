class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def minFrom(i,cur):
            if i >= len(cost):
                return cur
            cur += cost[i]
            stepOnce = minFrom(i+1,cur)
            stepTwice = minFrom(i+2,cur)
            return min(stepOnce,stepTwice)
        
        return min(minFrom(0,0),minFrom(1,0))
