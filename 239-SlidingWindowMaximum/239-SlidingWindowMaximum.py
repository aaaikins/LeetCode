# Last updated: 2/5/2026, 6:46:05 PM
1class Solution:
2    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
3        l = 0
4        res = []
5        q = deque()
6        # curMax = -inf
7        for r, n in enumerate(nums):
8            while q and nums[q[-1]] < n:
9                q.pop()
10
11            q.append(r)
12
13            if q[0] <= r - k:
14                q.popleft()
15            
16            if r >= k - 1:
17                res.append(nums[q[0]])
18                
19            
20        return res
21            