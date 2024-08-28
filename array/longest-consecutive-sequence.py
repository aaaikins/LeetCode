class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)

        for num in nums:
            if num - 1 not in numsSet:
                cur = 0
                while num + cur in numsSet:
                    cur += 1
                longest = max(cur, longest)

        return longest
        






        