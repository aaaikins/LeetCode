class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missNum = len(nums)
        for i in range(len(nums)):
            missNum += (i - nums[i])
        
        return missNum

        