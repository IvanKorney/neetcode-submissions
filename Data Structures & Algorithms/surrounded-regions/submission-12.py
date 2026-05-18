class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        vis = set()

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or board[r][c] == "X" or (r,c) in vis:
                return
            
            vis.add((r,c))
            for dr, dc in dirs:
                row, col = dr + r, dc + c
                dfs(row,col)
            

        for i in range(cols):
            if board[0][i] == "O" and (0,i) not in vis:
                dfs(0,i)
            if board[rows-1][i] == "O" and (rows-1,i) not in vis:
                dfs(rows-1,i)

        for i in range(rows):
            if board[i][0] == "O" and (i,0) not in vis:
                dfs(i,0)
            if board[i][cols-1] == "O" and (i,cols-1) not in vis:
                dfs(i,cols-1)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in vis:
                    board[r][c] = "X"

            