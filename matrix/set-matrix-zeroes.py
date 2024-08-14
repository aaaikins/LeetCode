class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = set()
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zeros.add((r,c))

        for pos in zeros:
            zero_row, zero_col = pos

            for r in range(row):
                matrix[r][zero_col] = 0

            for c in range(col):
                matrix[zero_row][c] = 0

        return matrix

        