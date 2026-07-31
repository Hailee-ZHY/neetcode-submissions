# 这里就是要维护三个的hashmap来看有没有重复
# 但是检查的时候事三个hashmap一起检查的
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols_hash = collections.defaultdict(set) # key: col_index, value: set(int)
        rows_hash = collections.defaultdict(set) # key: row_index, value: set(int)
        matrix_hash = collections.defaultdict(set) # key: (m_row, m_col), value: set(int)

        for c in range(9):
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in cols_hash[c] or 
                    board[r][c] in rows_hash[r] or 
                    board[r][c] in matrix_hash[(r//3, c//3)]):
                    return False
                else:
                    cols_hash[c].add(board[r][c])
                    rows_hash[r].add(board[r][c])
                    matrix_hash[(r//3, c//3)].add(board[r][c])
        return True
