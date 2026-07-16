class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        holder = [[1]* n for _ in range(m)]
        
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                holder[i][j] = holder[i+1][j] + holder[i][j+1]
        return holder[0][0]