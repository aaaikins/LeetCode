# Last updated: 12/18/2025, 1:50:42 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_list = []
        for i in range(len(nums)):
            if i + n < len(nums):
                new_list.append(nums[i])
                new_list.append(nums[n+i])
        return new_list
        