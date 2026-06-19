class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        top, bottom = 0, row-1

        while top <= bottom:
            middle_r = (top + bottom) // 2
            
            if target < matrix[middle_r][0]:
                bottom = middle_r-1
            elif target > matrix[middle_r][-1]:
                top = middle_r + 1
            else:
                break

        
        left, right = 0, col -1 
        while left <= right:
            middle_c = (left + right) // 2
            
            if target < matrix[middle_r][middle_c]:
                right = middle_c - 1
            elif target > matrix[middle_r][middle_c]:
                left = middle_c + 1 
            else: 
                return True 
        return False
