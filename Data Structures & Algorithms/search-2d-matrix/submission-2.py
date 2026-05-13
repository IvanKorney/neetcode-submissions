class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1

        while top <= bottom:
            midrow = (top+bottom)//2
            if matrix[midrow][0] > target:
                bottom = midrow -1
            elif matrix[midrow][-1] < target:
                top = midrow +1
            else:
                break
        
        if top > bottom:
            return False
        
        midrow = (top+bottom)//2
        l,r = 0, len(matrix[0])-1
        while l <= r:
            mid = (l+r)//2
            if matrix[midrow][mid]> target:
                r = mid -1
            elif matrix[midrow][mid] < target:
                l = mid +1
            else:
                return True
        return False
