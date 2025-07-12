class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heappushpop(min_heap, num)
            
        return min_heap[0]