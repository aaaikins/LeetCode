class Solution:
    def minOperations(self, n: int) -> int:

        count = -1
        while n:
            n &= n - 1
            count += 1
            

        return count
        