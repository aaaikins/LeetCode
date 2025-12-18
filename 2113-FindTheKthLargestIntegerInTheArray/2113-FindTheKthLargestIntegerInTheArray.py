# Last updated: 12/18/2025, 1:50:33 PM
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = lambda x: int(x))
        # print(nums)
        k = len(nums) - k

        return nums[k]
        