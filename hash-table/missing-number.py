class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet= set(nums)
        numsRange=set([n for n in range(len(nums)+1)])
        missNum = numsRange-numsSet
        return next(iter(missNum))

        