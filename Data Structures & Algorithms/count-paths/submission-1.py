class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = [1] * n #1D last row

        for i in range(m - 1):
            temp = [1] * n # row currently building
            for j in range(n - 2, -1, -1):
                temp[j] = rows[j] + temp[j + 1] #down + right
            rows = temp
        return rows[0]