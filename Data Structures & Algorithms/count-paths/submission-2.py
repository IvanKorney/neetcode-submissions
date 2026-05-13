class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * m for _ in range(n)]
        def uniquePath(r,c):
            if r == 0 and c == 0:
                return 1
            if r < 0 or c < 0:
                return 0
            if memo[r][c] != -1:
                return memo[r][c]
            memo[r][c] = uniquePath(r-1,c) + uniquePath(r,c-1)
            return memo[r][c]
        return uniquePath(n-1,m-1)