class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        sort_num = sorted(nums)
        return sort_num[n//2]
        
        