# Last updated: 1/2/2026, 7:50:42 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        nums = nums1 + nums2
4        nums.sort()
5
6        n = len(nums)
7
8        if n % 2 == 1:
9            return nums[n // 2]
10        else:
11            # print(nums[(n // 2) + 1])
12            return (nums[n // 2] + nums[(n // 2) - 1]) / 2