class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        diag = collections.defaultdict(set)
        b = board
        
        for r in range(9):
            for c in range(9):
                cell = b[r][c]
                if cell == ".":
                    continue
                if cell in rows[r] or cell in cols[c] or cell in diag[(r//3,c//3)]:
                    return False
                else:
                    rows[r].add(cell)
                    cols[c].add(cell)
                    diag[(r//3,c//3)].add(cell)

        return True