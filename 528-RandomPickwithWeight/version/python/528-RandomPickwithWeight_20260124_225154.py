# Last updated: 1/24/2026, 10:51:54 PM
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
16        return bisect.bisect_left(self.prefixes, target)
17
18
19        # l, r = 0, len(self.prefixes)
20
21        # while l <= r:
22        #     mid = (l + r) // 2
23
24
25
26
27# Your Solution object will be instantiated and called as such:
28# obj = Solution(w)
29# param_1 = obj.pickIndex()