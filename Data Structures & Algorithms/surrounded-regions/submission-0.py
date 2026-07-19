class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def capture(r, c):
            if r >= len(board) or c >= len(board[0]) or r < 0 or c < 0 or board[r][c] != "O":
                return
            
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        #capture unsurrounded region(O -> T)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (r in [0, len(board) - 1] or c in [0, len(board[0]) - 1]):
                    capture(r,c)

        #capture surrounded region(O -> X)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"

        #uncapture unsurrounded region(T -> O)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "T":
                    board[r][c] = "O"