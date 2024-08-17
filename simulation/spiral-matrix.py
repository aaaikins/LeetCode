class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []
        
        while left < right and top < bottom: 

            for l in range(left, right):
                res.append(matrix[top][l])
            top += 1
            # print(res)

            for t in range(top, bottom):
                res.append(matrix[t][right-1])
            right -= 1
            # print(res)

            for r in range(right -1, -1, -1):
                res.append(matrix[bottom -1][r])
            bottom -= 1
            # print(res)
            
            for c in range(left, right):
                res.append(matrix[bottom-1][c])

            if left <= right and top <= bottom:
                break


        return res

        



        