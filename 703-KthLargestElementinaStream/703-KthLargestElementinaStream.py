# Last updated: 8/24/2026, 5:44:55 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        heapify(nums)
4        
5        while len(nums) > k:
6            heappop(nums)
7            
8        
9        return nums[0]