class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
      cols = collections.defaultdict(set)
      rows = collections.defaultdict(set)
      squares = collections.defaultdict(set)
      for r in range(9):
        for c in range(9):
            s = board[r][c]
            if s == ".":
                continue;
            else:
                if s in rows[r] or s in cols[c] or s in squares[(r//3,c//3)]:
                    return False
                else:
                    rows[r].add(s)
                    cols[c].add(s)
                    squares[(r//3,c//3)].add(s)
      return True