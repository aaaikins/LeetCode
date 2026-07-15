# Last updated: 7/14/2026, 11:00:06 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        hashmap = {}
4        for num in nums: # O(N)
5            hashmap[num] = hashmap.get(num, 0) + 1
6        
7        buckets = [[] for i in range(len(nums) + 1)]
8
9        for num, freq in hashmap.items(): 
10            buckets[freq].append(num)
11        
12        res = []
13
14        for i in range(len(buckets) - 1, -1, -1):
15            # print(i)
16            if buckets[i] is None:
17                continue
18            for num in buckets[i]:
19                if len(res) == k:
20                    return res
21                res.append(num)
22        
23        return res
24        