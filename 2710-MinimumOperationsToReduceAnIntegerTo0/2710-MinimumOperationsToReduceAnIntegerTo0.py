# Last updated: 12/18/2025, 1:50:22 PM
class Solution:
    def minOperations(self, n: int) -> int:
        numOperations = 0
        while n != 0:
            lower = n - 2**int(log2(n))
            upper = 2**int(log2(n) + 1) - n
            numOperations += 1
            n = min(lower, upper)

        return numOperations