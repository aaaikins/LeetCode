# Last updated: 12/18/2025, 1:50:34 PM
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s, l = min(nums),max(nums)

        while l:
            s, l = l, s % l
        
        return s