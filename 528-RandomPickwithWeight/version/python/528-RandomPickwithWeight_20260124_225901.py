# Last updated: 1/24/2026, 10:59:01 PM
1class Solution:
2
3    def __init__(self, w: List[int]):
4        self.prefixes = []
5
6        total = 0
7        for i in range(len(w)):
8            total += w[i]
9            self.prefixes.append(total)
10
11        self.total = total
12
13
14    def pickIndex(self) -> int:
15        target = random.randint(1, self.total)
16
17        l, r = 0, len(self.prefixes) - 1
18
19        while l <= r:
20            mid = (l + r) // 2
21
22            if self.prefixes[mid] < target:
23                l = mid + 1
24            else:
25                r = mid - 1
26            
27        return l
28
29
30
31
32# Your Solution object will be instantiated and called as such:
33# obj = Solution(w)
34# param_1 = obj.pickIndex()