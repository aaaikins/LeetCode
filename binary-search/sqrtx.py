class Solution:
    def mySqrt(self, x: int) -> int:
        if x== 0 or x == 1:
            return x
        nums = [i for i in range(1, x)]
        print(nums)
        l, r = 0, len(nums) - 1
        base = 1
        while l != r:
            mid = (l + r)//2
            num = nums[mid]
            base = num
            if (num ** 2) < x:
                l = mid + 1
            elif (num ** 2) > x:
                r = mid - 1
            else:
                break
        
        return base

                
        