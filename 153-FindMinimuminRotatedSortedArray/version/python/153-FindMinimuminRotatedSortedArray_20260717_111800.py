# Last updated: 7/17/2026, 11:18:00 AM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        minNum = float('inf')
4
5        for num in nums:
6            minNum = min(num, minNum)
7
8        return minNum