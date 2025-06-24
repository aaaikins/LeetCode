class Solution:
    def mySqrt(self, x: int) -> int:
        i, j = 0, x - 1

        while i < j:
            mid = (i + j) // 2

            if mid ** 2 > x:
                j = mid - 1
            elif mid**2 < x:
                i = mid + 1
            else:
                return mid
        
        return i