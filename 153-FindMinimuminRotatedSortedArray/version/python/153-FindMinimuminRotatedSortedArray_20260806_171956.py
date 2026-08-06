# Last updated: 8/6/2026, 5:19:56 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        """
4        nums = [3,4,5,1,2]
5
6        left = 0 -> nums[left] = 3 -> left = 3 -> nums[left] = 1
7
8        right = 4 -> nums[right] = 2
9
10        mid = (left + right) // 2 = 2
11
12        nums[mid] = 5
13
14        res = inf
15
16        if nums[left] < nums[right]:
17            res = min(res, nums[left])
18
19        if nums[mid] < nums[right]:
20            right = mid
21        else:
22            left = mid + 1
23
24
25        return res
26        """
27        l, r = 0, len(nums) - 1
28
29        res = nums[l]
30
31        while l < r:
32            m = (l + r) // 2
33            
34            if nums[m] < nums[r]:
35                r = m
36            else:
37                l = m + 1
38
39            res = min(res, nums[l])
40
41            
42        return res
43        
44        # return nums[l]