# Last updated: 12/18/2025, 1:50:31 PM
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        lowest = nums[0]
        maxDiff = -float('inf')

        for price in nums[1:]:
            if price < lowest:
                lowest = price
            maxDiff = max(maxDiff, price - lowest)
        
        return maxDiff if maxDiff > 0 else -1