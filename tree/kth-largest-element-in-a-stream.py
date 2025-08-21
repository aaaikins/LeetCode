class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-num for num in nums]

    def add(self, val: int) -> int:
        self.nums.append(-val)
        heapify(self.nums)
        
        top_k=[]
        for _ in range(self.k):
            top_k.append(heappop(self.nums))

        self.nums.extend(top_k)
        
        return -top_k[-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, self.)
# param_1 = obj.add(val)