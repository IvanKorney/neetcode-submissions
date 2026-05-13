class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        pac, atl = set(), set()
        res = []
        def dfs(sets,r,c,prev):
            if (r,c) in sets or r not in range(rows) or c not in range(cols) or heights[r][c] < prev:
                return
            sets.add((r,c))
            for row, col in dirs:
                dr,dc = row+r, col+c
                dfs(sets,dr,dc,heights[r][c])
        
        for r in range(rows):
            dfs(pac,r,0,heights[r][0])
            dfs(atl,r,cols-1,heights[r][cols-1])
        for c in range(cols):
            dfs(pac,0,c,heights[0][c])
            dfs(atl,rows-1,c,heights[rows-1][c])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res