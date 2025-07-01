class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = [-num for num in nums]
        heapify(heap)
        a = -heappop(heap)
        b = -heappop(heap)
        maxVal = (a-1)*(b-1)
        return maxVal

        