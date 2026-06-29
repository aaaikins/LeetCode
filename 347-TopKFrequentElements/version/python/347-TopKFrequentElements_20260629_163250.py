# Last updated: 6/29/2026, 4:32:50 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count = Counter(nums)
4        n = len(nums)
5        buckets = [[] for i in range(n + 1)]
6
7        for num, val in count.items():
8            buckets[val].append(num)
9
10        res = []
11        for i in range(n, -1, -1):
12            for num in buckets[i]:
13                if len(res) == k:
14                    return res
15                res.append(num)
16        
17        return res
18