# Last updated: 7/10/2026, 5:55:23 PM
1class Solution:
2    def sumOfThree(self, num: int) -> List[int]:
3        n = num // 3
4        res = [i for i in range(n-1, n+2)]
5        total = sum(res)
6        # print(res)
7        return res if total == num else []