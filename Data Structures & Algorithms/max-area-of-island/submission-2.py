class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows,cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            if (r,c) in visited or r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                return 0
            visited.add((r,c))
            res = 1 + dfs(r+1,c)+ dfs(r-1,c)+ dfs(r,c+1)+ dfs(r,c-1)
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    maxArea = max(area,maxArea)
        
        return maxArea