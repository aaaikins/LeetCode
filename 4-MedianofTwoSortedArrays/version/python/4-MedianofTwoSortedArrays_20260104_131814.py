# Last updated: 1/4/2026, 1:18:14 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        if len(nums1) > len(nums2):
4            nums2, nums1 = nums1, nums2
5   
6        m, n = len(nums1), len(nums2)
7        total = m + n
8        left_size = (total + 1)//2
9
10
11        low, high = 0, m
12        NEG_INF = float("-inf")
13        POS_INF = float("inf")
14
15        while low <= high:
16            i = (low + high) // 2
17            j = left_size - i
18
19            left1  = nums1[i - 1] if i > 0 else NEG_INF
20            right1 = nums1[i]     if i < m else POS_INF
21
22            left2  = nums2[j - 1] if j > 0 else NEG_INF
23            right2 = nums2[j]     if j < n else POS_INF
24
25            if left1 <= right2 and left2 <= right1:
26                if total % 2 == 1:
27                    return float(max(left1, left2))
28                return (max(left1, left2) + min(right1, right2)) / 2.0
29
30            if left1 > right2:
31                high = i - 1
32            else:
33                low = i + 1
34
35