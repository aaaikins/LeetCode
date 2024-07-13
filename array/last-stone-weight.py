class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [-stone for stone in stones]
        heapq.heapify(nums)

        while len(nums) > 1:
            y = heapq.heappop(nums)
            x = heapq.heappop(nums)
            diff = y - x
            if diff < 0:
                heapq.heappush(nums, diff)

        if not nums:
            return 0
        else:
            return -heapq.heappop(nums)
        