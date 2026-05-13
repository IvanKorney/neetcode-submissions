class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rset = set()
        cset = set()
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]== 0:
                    rset.add(r)
                    cset.add(c)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rset or c in cset:
                    matrix[r][c]=0
        