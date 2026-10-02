# Last updated: 10/2/2026, 2:30:40 PM
1class Solution:
2    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
3        result = []
4
5        def backtrack(idx, total, comb):
6            if total == target:
7                result.append(comb[:])
8                return
9
10            if total > target:
11                return
12
13            for i in range(idx, len(candidates)):
14                comb.append(candidates[i])
15                backtrack(i, total + candidates[i], comb)
16                comb.pop()
17            
18        
19
20        backtrack(0, 0, [])
21        return result