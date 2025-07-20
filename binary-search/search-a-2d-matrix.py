class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, r = 1, (row * col) - 1

        while l <= r:
            m = (l + r) // 2
            r = m // row
            c = m % col
            # print(m)
            # print(r, c)
            print(l, r)

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                l = m + 1
            else:
                r = m - 1

        
        return False


        