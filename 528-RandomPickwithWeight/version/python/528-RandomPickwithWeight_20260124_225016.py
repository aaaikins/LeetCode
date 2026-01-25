# Last updated: 1/24/2026, 10:50:16 PM
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
17        for prefix in self.prefixes:
18            if prefix >= target:
19                target = prefix
20                break
21        return self.prefixes.index(target)
22
23
24        # l, r = 0, len(self.prefixes)
25
26        # while l <= r:
27        #     mid = (l + r) // 2
28
29
30
31
32# Your Solution object will be instantiated and called as such:
33# obj = Solution(w)
34# param_1 = obj.pickIndex()