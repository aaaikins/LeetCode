class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while l <= r:
            mid = (l+r) // 2
            product = mid * mid

            if product == num:
                return True

            if product < num:
                l = mid + 1
            else:
                r = mid - 1
            
        return False