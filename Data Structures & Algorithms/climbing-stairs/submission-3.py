class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def checkWays(n):
            if n <= 1:
                return 1
            else:
                oneStep = checkWays(n-1)
                twoStep = checkWays(n-2)
                return oneStep + twoStep
        return checkWays(n)