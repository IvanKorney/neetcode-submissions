class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        diag = collections.defaultdict(set)
        b = board
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                v = board[r][c]
                if v in rows[r] or v in cols[c] or v in diag[(r//3,c//3)]:
                    return False
                rows[r].add(v)
                cols[c].add(v)
                diag[(r//3,c//3)].add(v)

        
        return True