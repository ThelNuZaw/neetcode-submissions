class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posD = set() #(r + c)
        negD = set() #(r - c)
        board = [["."] * n for _ in range(n)] #[[".", ".", ".", "."],
                                             # [".", ".", ".", "."], ]
        res = []
        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in posD or (r - c) in negD:
                    continue
                col.add(c)
                posD.add(r + c)
                negD.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                col.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

        
        