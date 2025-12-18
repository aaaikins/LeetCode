# Last updated: 12/18/2025, 1:49:57 PM
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        count = 0
        for num in range(low, high + 1):
            num = str(num)
            if len(num) % 2 != 0:
                continue
            m = len(num)//2
            left = sum(int(ch) for ch in num[:m])
            right = sum(int(ch) for ch in num[m:])
            if left == right:
                count += 1
        
        return count
            
                

            