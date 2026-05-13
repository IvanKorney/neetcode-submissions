class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visit = set()

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or board[r][c] == "X":
                return False
            if r == 0 or c == 0 or r == rows -1 or c == cols -1:
                return True
            visit.add((r,c))
            res = dfs(r+1,c) or dfs(r-1,c) or dfs(r,c+1) or dfs(r,c-1)
            visit.remove((r,c))
            return res
            
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and r != 0 and r != rows-1 and c != 0 and c != cols-1:
                    if not dfs(r,c):
                        board[r][c]= "X"
        