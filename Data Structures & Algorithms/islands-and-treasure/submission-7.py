class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        # add all gates (0s)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                    continue

                if grid[nr][nc] != inf:
                    continue

                grid[nr][nc] = grid[r][c] + 1
                q.append((nr, nc))