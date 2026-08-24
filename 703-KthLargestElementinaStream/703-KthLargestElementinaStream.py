# Last updated: 8/24/2026, 5:21:39 PM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.heap = nums
5        self.k = k
6        heapify(self.heap)
7
8        while len(self.heap) > self.k:
9            heappop(self.heap)
10        print(self.heap)
11
12    def add(self, val: int) -> int:
13        heappush(self.heap, val)
14        if len(self.heap) > self.k:
15            heappop(self.heap)
16            
17        return self.heap[0]
18        
19
20
21# Your KthLargest object will be instantiated and called as such:
22# obj = KthLargest(k, nums)
23# param_1 = obj.add(val)