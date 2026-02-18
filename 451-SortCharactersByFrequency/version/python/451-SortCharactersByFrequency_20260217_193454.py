# Last updated: 2/17/2026, 7:34:54 PM
1class Solution:
2    def frequencySort(self, s: str) -> str:
3        count = Counter(s)
4        heap = [(-cnt, ch) for ch, cnt in count.items()]
5        heapify(heap)
6
7        new_s = ""
8
9        while heap:
10            cnt, ch = heappop(heap)
11            new_s += -cnt * ch
12        
13        return new_s