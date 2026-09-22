# Last updated: 9/22/2026, 5:11:30 PM
1class Solution:
2    def getRow(self, rowIndex: int) -> list[int]:
3        if rowIndex == 0:
4            return [1]
5
6        dp = [0] * (rowIndex + 1)
7        dp[0] = dp[rowIndex] = 1
8
9        for i in range(1, rowIndex):
10            dp[i] = dp[i-1] * (rowIndex - i + 1) // i
11
12        return dp