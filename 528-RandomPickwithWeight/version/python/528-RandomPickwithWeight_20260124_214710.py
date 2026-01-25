# Last updated: 1/24/2026, 9:47:10 PM
1import random
2import bisect
3from typing import List
4
5class Solution:
6    def __init__(self, w: List[int]):
7        self.prefix = []
8        curr = 0
9        for weight in w:
10            curr += weight
11            self.prefix.append(curr)
12        self.total = curr
13
14    def pickIndex(self) -> int:
15        target = random.randint(1, self.total)
16        return bisect.bisect_left(self.prefix, target)
17
18
19
20# Your Solution object will be instantiated and called as such:
21# obj = Solution(w)
22# param_1 = obj.pickIndex()