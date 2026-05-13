class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        diag = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                cell = board[r][c]
                if cell in rows[r] or cell in cols[c] or cell in diag[(r//3,c//3)]:
                    return False
                else:
                    rows[r].add(cell)
                    cols[c].add(cell)
                    diag[(r//3,c//3)].add(cell)

        return True