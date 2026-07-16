# Last updated: 7/16/2026, 7:59:52 PM
1class Solution:
2    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
3        l, r = 0, len(letters) - 1
4        if target >= letters[r]:
5            return letters[l]
6
7        while l < r:
8            m = (l + r) // 2
9
10            if letters[m] <= target:
11                l = m + 1
12            else:
13                r = m
14        
15        return letters[r]