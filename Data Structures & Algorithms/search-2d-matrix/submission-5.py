# bruce force with O(m*n) complexity
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r , c = len(matrix), len(matrix[0])
        
        for i in range(r):
            if target not in matrix[i]:
                continue 
            else:
                return True 
        return False

        
