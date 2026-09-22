# Last updated: 9/22/2026, 5:00:28 PM
1class Solution:
2    def getRow(self, rowIndex: int) -> list[int]:
3        if rowIndex == 0:
4            return [1]
5
6        dp = [1] * (rowIndex + 1)
7        dp[1] = rowIndex
8        dp[rowIndex - 1] = rowIndex
9
10        for i in range(2, rowIndex):
11            dp[i] = dp[i-1] * (rowIndex - i + 1) // i
12        
13
14
15        return dp