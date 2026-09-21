# Last updated: 9/21/2026, 7:38:02 PM
1class Solution:
2    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
3        count = Counter(barcodes)
4        maxHeap = [[-cnt, code] for code, cnt in count.items()]
5        heapify(maxHeap)
6        res = []
7        prev = None
8
9        while maxHeap or prev:
10            # if prev and not maxHeap:
11            #     return ""
12
13            if maxHeap:
14                cnt, code = heappop(maxHeap)
15                res.append(code)
16                cnt += 1
17
18            if prev:
19                heappush(maxHeap, prev)
20                prev = None
21
22            if cnt !=0:
23                prev = [cnt, code]
24
25        return res
26        