# Last updated: 1/10/2026, 5:00:58 PM
1from collections import OrderedDict
2
3class LRUCache:
4
5    def __init__(self, capacity: int):
6        self.capacity = capacity
7        self.cache = OrderedDict()
8
9    def get(self, key: int) -> int:
10
11        if key not in self.cache:
12            return -1
13
14        value = self.cache[key]
15        self.cache.move_to_end(key)
16        # print(self.cache)
17        return value
18
19    def put(self, key: int, value: int) -> None:
20        if key in self.cache:
21            self.cache[key] = value
22            self.cache.move_to_end(key)
23        self.cache[key] = value
24        
25
26        if len(self.cache) > self.capacity:
27            self.cache.popitem(last=False)
28
29
30
31# Your LRUCache object will be instantiated and called as such:
32# obj = LRUCache(capacity)
33# param_1 = obj.get(key)
34# obj.put(key,value)