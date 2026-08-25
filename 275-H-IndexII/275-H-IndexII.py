# Last updated: 8/25/2026, 5:04:19 PM
1class Solution:
2    def hIndex(self, citations: List[int]) -> int:
3        n = len(citations)
4
5        left = 0
6        right = n - 1
7
8        while left <= right:
9            mid = (left + right) // 2
10
11            if citations[mid] >= n - mid:
12                right = mid - 1
13            else:
14                left = mid + 1
15
16        return n - left