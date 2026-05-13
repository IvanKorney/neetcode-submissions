class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*m for _ in range(n)]
        dp[0][0] = 1
        for r in range(n):
            for c in range(m):
                left, up = 0,0
                if r-1 >= 0:
                    left = dp[r-1][c]
                if c-1 >= 0:
                    up = dp[r][c-1]
                dp[r][c] += up + left
        return dp[n-1][m-1]
