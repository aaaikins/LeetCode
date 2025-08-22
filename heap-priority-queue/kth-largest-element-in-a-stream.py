class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapify(self.nums)
        for _ in range(len(self.nums)-self.k):
            heappop(self.nums)


    def add(self, val: int) -> int:
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, self.)
# param_1 = obj.add(val)