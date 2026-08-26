class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        rows, cols = len(grid),len(grid[0])
        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
                
        time = 0
        while fresh > 0 and q:

            for _ in range(len(q)):
                rottenX, rottenY = q.popleft()
                for dr,dc in dirs:
                    r,c = rottenX+dr,rottenY+dc
                    if r not in range(rows) or c not in range(cols) or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    fresh -= 1
                    q.append((r,c))

            
            time += 1



        return time if fresh == 0 else -1