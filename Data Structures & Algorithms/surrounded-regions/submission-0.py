class Solution:
    def solve(self, board: List[List[str]]) -> None:
        vis = set()
        q = collections.deque()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        rows, cols = len(board), len(board[0])

        for i in range(rows):
            if board[i][0] == "O":
                q.append((i,0))
            if board[i][cols-1] == "O":
                q.append((i,cols-1))

        for i in range(cols):
            if board[0][i] == "O":
                q.append((0,i))
            if board[rows-1][i] == "O":
                q.append((rows-1,i))

        while q:
            row, col = q.popleft()
            vis.add((row,col))
            for dr, dc in dirs:
                r,c = row+dr, col + dc
                if r not in range(rows) or c not in range(cols) or board[r][c] != "O" or (r,c) in vis:
                    continue
                q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in vis:
                    board[r][c] = "X"
                












