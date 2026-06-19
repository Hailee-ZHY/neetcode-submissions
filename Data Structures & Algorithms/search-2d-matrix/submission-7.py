class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])

        top, bottom = 0, r-1

        while top <= bottom:
            mid_c = (top+bottom)//2
            if target < matrix[mid_c][0]:
                bottom = mid_c -1
            elif target > matrix[mid_c][-1]:
                top = mid_c + 1
            else:
                break

        # check the break is because we find the valid interval or didn't
        if not (top <= bottom):
            return False
        
        left, right = 0, c-1 
        row = mid_c
        while left <= right:
            mid_r = (left+right)//2
            if target < matrix[row][mid_r]:
                right = mid_r - 1
            elif target > matrix[row][mid_r]:
                left = mid_r + 1
            else:
                return True 
        return False
