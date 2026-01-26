# Last updated: 1/26/2026, 6:38:13 PM
1class Solution:
2    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
3        arr.sort()
4        minDiff = inf
5
6        for i in range(1, len(arr)):
7            minDiff = min(minDiff, abs(arr[i - 1] - arr[i]))
8
9        res = []
10        for i in range(1, len(arr)):
11            if abs(arr[i - 1] - arr[i]) == minDiff:
12                res.append([arr[i - 1], arr[i]])
13
14        return res
15