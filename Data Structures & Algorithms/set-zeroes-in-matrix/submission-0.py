class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        set_row = set()
        set_col = set()

        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    set_row.add(i)
                    set_col.add(j)
    
        for i in set_row:
            matrix[i] = [0 for _ in range(n)]
        for j in set_col:
            for k in range(m):
                matrix[k][j] = 0

