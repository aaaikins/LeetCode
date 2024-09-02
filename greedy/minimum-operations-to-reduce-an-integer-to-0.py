class Solution:
    def minOperations(self, n: int) -> int:
        count = 0

        while n > 0:
            lower = n - 2**(int(log2(n)))
            upper = 2**(int(log2(n)) + 1) - n

            n = min(lower, upper)
            count += 1
        
        return count
