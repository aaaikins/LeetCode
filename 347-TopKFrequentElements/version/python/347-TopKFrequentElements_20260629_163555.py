# Last updated: 6/29/2026, 4:35:55 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count = Counter(nums)
4        buckets = [[] for _ in range(len(nums) + 1)]
5
6        for num, freq in count.items():
7            buckets[freq].append(num)
8
9        res = []
10        for i in range(len(nums), 0, -1):
11            for num in buckets[i]:
12                res.append(num)
13                if len(res) == k:
14                    return res
15
16        return res