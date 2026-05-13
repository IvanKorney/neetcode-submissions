class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def uniquePath(r,c):
            if r == 0 and c == 0:
                return 1
            if r < 0 or c < 0:
                return 0
            left = uniquePath(r-1,c)
            up = uniquePath(r,c-1)
            return left + up
        return uniquePath(n-1,m-1)