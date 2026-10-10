class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row = len(matrix)
        col = len(matrix[0])

        firstRow = False

        #mark first row and first column to record which rows and cols need to be zero
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        firstRow = True

        #interior cells turns zero
        for r in range(1, row):
            for c in range(1, col):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        #make zero in first col 
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0] = 0

        #make zero in first row 
        if firstRow:
            for c in range(col):
                matrix[0][c] = 0
        

        