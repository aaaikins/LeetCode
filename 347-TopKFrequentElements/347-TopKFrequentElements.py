# Last updated: 7/14/2026, 10:40:06 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        # create a hashmap to store freqs
4        hashmap = {}
5        for num in nums: # O(N)
6            hashmap[num] = hashmap.get(num, 0) + 1
7        
8        arr = []
9        for num, freq in hashmap.items(): # O(N)
10            arr.append((freq, num))
11        
12        arr.sort() # O(nlogn)
13
14        res = []
15        while len(res) < k: # O(k)
16            freq, num = arr.pop()
17            res.append(num)
18        
19        return res
20        