# Last updated: 12/18/2025, 1:50:35 PM
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
    
        total = sum(nums)
        sumLeft = 0

        for i in range(len(nums)):
            sumRight = total - sumLeft - nums[i]

            if sumLeft == sumRight:
                return i
                
            sumLeft += nums[i]
        return -1
        