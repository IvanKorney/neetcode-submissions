class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def checkWays(n):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            else:
                oneStep = checkWays(n-1)
                twoStep = checkWays(n-2)
                memo[n] = oneStep + twoStep
                return memo[n]
        return checkWays(n)