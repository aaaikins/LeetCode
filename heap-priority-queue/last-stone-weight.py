class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = [-stone for stone in stones]
        heapify(nums)

        while len(nums) > 1:
            y = heappop(nums)
            x = heappop(nums)
            diff = y - x
            if y < x:
                heappush(nums, diff)

        if not nums:
            return 0
        else:
            return -heapq.heappop(nums)
        