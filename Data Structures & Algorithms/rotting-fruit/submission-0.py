class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        fresh = 0
        rows,cols = len(grid), len(grid[0])
        q = collections.deque()
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        while fresh > 0 and q:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr,dc in dirs:
                    r, c = row+dr,col+dc
                    if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                        continue
                    else:
                        q.append((r,c))
                        grid[r][c] = 2
                        fresh -= 1
            res += 1

            
        return res if fresh == 0 else -1

                
