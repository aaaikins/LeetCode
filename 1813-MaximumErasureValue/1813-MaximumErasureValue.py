# Last updated: 12/18/2025, 1:50:39 PM
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxScore = 0
        curScore = 0
        visited = set()

        l, r = 0, 0

        while r < len(nums):
            while nums[r] in visited:
                curScore -= nums[l]
                visited.remove(nums[l])
                l += 1

            visited.add(nums[r])
            curScore += nums[r]
            
            maxScore = max(maxScore, curScore)
            r += 1
            
        return maxScore
        