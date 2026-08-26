class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        rows, cols = len(board), len(board[0])
        vis = set()
        n = len(word)
        def bt(i,r,c):
            if i == n:
                return True
            if r not in range(rows) or c not in range(cols) or (r,c) in vis or board[r][c] != word[i]:
                return False
            d = False
            vis.add((r,c))
            for dr,dc in dirs:
                row, col = r+dr, c+dc
                d = d or bt(i+1,row,col)
            vis.remove((r,c))
            return d
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and bt(0,r,c):
                    return True
        return False



