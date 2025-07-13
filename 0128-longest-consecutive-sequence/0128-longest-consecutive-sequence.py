class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numsSet = set(nums)

        res = 0

        for num in numsSet:
            if (num - 1) not in numsSet:
                cur_streak = 0
                while (num + cur_streak) in numsSet:
                    cur_streak += 1
                res = max(res, cur_streak)
        
        return res


