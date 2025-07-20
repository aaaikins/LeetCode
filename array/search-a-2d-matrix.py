class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        left, right = 0, (row * col) - 1

        while left <= right:
            m = (left + right) // 2
            r = m // row
            c = m % col

            if matrix[r][c] > target:
                right = m - 1
            elif matrix[r][c] < target:
                left = m + 1
            else:
                return True

        
        return False


        