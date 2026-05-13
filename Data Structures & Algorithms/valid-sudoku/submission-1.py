class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        diag = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else:
                    if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in diag[(r//3,c//3)]:
                        return False
                    else:
                        rows[r].add(board[r][c])
                        cols[c].add(board[r][c])
                        diag[(r//3,c//3)].add(board[r][c])
        return True