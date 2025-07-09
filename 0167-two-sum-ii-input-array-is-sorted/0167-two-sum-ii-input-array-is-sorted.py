class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [2,7,11,15]
        l  r

        total = 2 + 7 = 9
        target = 9
        [l+1, r+ 1] = [1, 2]
        """
        l, r = 0, len(nums) - 1

        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                return [l+1, r+ 1]
            elif total > target:
                r -= 1
            else:
                l += 1
        