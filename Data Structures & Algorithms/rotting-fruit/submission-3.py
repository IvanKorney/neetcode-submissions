class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]

        good = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    good += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        while good != 0 and q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    row,col = dr+r, dc+c
                    if row not in range(rows) or col not in range(cols) or grid[row][col] != 1:
                        continue
                    q.append((row,col))
                    good -= 1
                    grid[row][col] = 2 
            res += 1
        
        return res if good == 0 else -1

