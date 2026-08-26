class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        vis = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    vis.add((r,c))


        time = 0


        while q:
            for _ in range(len(q)):
                row,col = q.popleft()
                grid[row][col] = time
                for dr,dc in dirs:
                    r,c = row+dr, col+dc
                    if r not in range(rows) or c not in range(cols) or grid[r][c] != INF or (r,c) in vis:
                        continue
                    q.append((r,c))
                    vis.add((r,c))
                
            

            time += 1
