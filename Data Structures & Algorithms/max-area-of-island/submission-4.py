class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        vis = set()
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in vis or grid[r][c] == 0:
                return 0
            
            vis.add((r,c))
            cur = 1
            for dr,dc in dirs:
                row, col = dr+r, dc+c
                cur += dfs(row,col)
            
            return cur
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in vis:
                    res = max(res,dfs(r,c))
        return res