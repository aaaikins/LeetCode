import heapq as hq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        hq.heapify(nums)
        while len(nums) > self.k:
            hq.heappop(nums)
        self.minHeap = nums
        

    def add(self, val: int) -> int:
        hq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            hq.heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)