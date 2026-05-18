class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        vis = set()
        n = len(word)
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r,c,i):
            if i == n:
                return True
            if r not in range(rows) or c not in range(cols) or (r,c) in vis or board[r][c] != word[i]:
                return False
            
            vis.add((r,c))
            res = False

            for dr,dc in dirs:
                row, col = dr+r, dc+c
                res = dfs(row,col,i+1) or res

            vis.remove((r,c))

            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True

        return False