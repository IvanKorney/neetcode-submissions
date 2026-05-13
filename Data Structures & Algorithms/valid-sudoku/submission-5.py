class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        diag = collections.defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else:
                    sq = board[r][c]
                    if sq in rows[r] or sq in cols[c] or sq in diag[(r//3,c//3)]:
                        return False
                    else:
                        rows[r].add(sq)
                        cols[c].add(sq)
                        diag[(r//3,c//3)].add(sq)

        return True