class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        res = 0
        visit = set()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        def dp(r,c):
            if (r,c) in visit or r not in range(ROWS) or c not in range(COLS) or grid[r][c] == "0":
                return
            visit.add((r,c))
            for dr,dc in dirs:
                row = r+dr
                col = c +dc
                dp(row,col)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dp(r,c)
                    res += 1
        return res
