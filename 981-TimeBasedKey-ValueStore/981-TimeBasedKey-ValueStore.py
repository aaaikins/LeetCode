# Last updated: 1/5/2026, 3:13:36 PM
1from collections import defaultdict
2
3class TimeMap:
4
5    def __init__(self):
6        self.map = defaultdict(list)
7
8    def set(self, key: str, value: str, timestamp: int) -> None:
9        self.map[key].append((value, timestamp))
10
11    def get(self, key: str, timestamp: int) -> str:
12        val_time = self.map[key]
13        # if not 
14        value = ""
15
16        l, r = 0, len(val_time) - 1
17        while l <= r:
18            m = (l + r) // 2
19            val, time = val_time[m]
20            if time <= timestamp:
21                value = val
22                l = m + 1
23            else:
24                r = m - 1
25        return value
26        
27
28
29# Your TimeMap object will be instantiated and called as such:
30# obj = TimeMap()
31# obj.set(key,value,timestamp)
32# param_2 = obj.get(key,timestamp)