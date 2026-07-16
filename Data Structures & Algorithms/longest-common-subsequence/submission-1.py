class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m , n = len(text1), len(text2)
        holder = [[0]* (n+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    holder[i][j] = 1 + holder[i+1][j+1]
                else:
                    holder[i][j] = max(holder[i+1][j], holder[i][j+1])
        return holder[0][0]