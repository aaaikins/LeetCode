class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        row = len(matrix)
        col = len(matrix[0])

        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zeros.append((r,c))

        for zero_row, zero_col in zeros:
            for r in range(row):
                matrix[r][zero_col] = 0

            for c in range(col):
                matrix[zero_row][c] = 0

        