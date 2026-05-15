class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1
        m = -1
        while top <= bot:
            m = (top+bot)//2
            if target < matrix[m][0]:
                bot = m-1
            elif target > matrix[m][-1]:
                top = m+1
            else:
                break
            
        if not top <= bot:
            return False

        l,r = 0, len(matrix[0])-1
        while l <= r:
            mid = (l+r)//2
            if target == matrix[m][mid]:
                return True
            elif target < matrix[m][mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False
        
