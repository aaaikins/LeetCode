# Last updated: 2/8/2026, 3:04:03 PM
1class Solution:
2    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        stack = []
4        idx_map = {}
5        res = [-1] * len(nums1)
6
7        for i, n in enumerate(nums1):
8            idx_map[n] = i
9
10        for n in nums2:
11            while stack and n > stack[-1]:
12                num = stack.pop()
13                if num in idx_map:
14                    idx = idx_map[num]
15                    res[idx] = n
16            stack.append(n)
17
18        return res