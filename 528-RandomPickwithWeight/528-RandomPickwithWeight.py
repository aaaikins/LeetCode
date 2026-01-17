# Last updated: 1/17/2026, 1:05:58 AM
1import random as rd
2
3class Solution:
4
5    def __init__(self, w: List[int]):
6        self.cum_weights = []
7        total = 0
8        for weight in w:
9            total += weight
10            self.cum_weights.append(total)
11        self.total = total
12
13    def pickIndex(self) -> int:
14        rand_num = random.uniform(0, self.cum_weights[-1])
15        
16        # Perform a manual binary search to find the index
17        low, high = 0, len(self.cum_weights) - 1
18        while low < high:
19            mid = (low + high) // 2
20            if rand_num > self.cum_weights[mid]:
21                low = mid + 1
22            else:
23                high = mid
24        return low
25
26        
27
28
29# Your Solution object will be instantiated and called as such:
30# obj = Solution(w)
31# param_1 = obj.pickIndex()