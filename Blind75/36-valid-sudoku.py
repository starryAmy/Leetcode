import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 每一個cols是一個dict，key為第幾個col，value為一set
        # 每一個rols也是
        # 每一個square的key為(col / 3, rows / 3)
        cols = collections.defaultdict(set) # 創建一個默認字典，默認值為集合
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (rows/3, cols/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
