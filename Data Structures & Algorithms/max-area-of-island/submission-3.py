class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS,COLS = len(grid),len(grid[0])
        visit = set()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        def dp(r,c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 or (r,c) in visit:
                return 0
            visit.add((r,c))
            amt = 0
            for dr,dc in dirs:
                amt += dp(r+dr,c+dc) 
            return 1 + amt
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    amt = dp(r,c)
                    res = max(res,amt)
        return res

            
