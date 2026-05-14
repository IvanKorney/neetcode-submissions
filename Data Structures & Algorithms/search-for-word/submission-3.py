class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        l1 = word[0]
        n = len(word)
        visit = set()


        def dfs(r,c,i):
            if i == n:
                return True
            if r not in range(rows) or c not in range(cols) or board[r][c] != word[i] or (r,c) in visit:
                return False
            visit.add((r,c))
            res = False

            for dr,dc in dirs:
                row, col = dr+r, dc+c
                res = res or dfs(row,col,i+1)

            visit.remove((r,c))
            return res 

            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == l1:
                    if dfs(i,j,0):
                        return True

        return False