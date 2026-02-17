# Last updated: 2/17/2026, 6:47:36 PM
1class MyHashMap:
2
3    def __init__(self):
4        self.hashmap = [[]] * (10**6 + 1)
5
6    def put(self, key: int, value: int) -> None:
7        self.hashmap[key] = value
8
9    def get(self, key: int) -> int:
10        return self.hashmap[key] if self.hashmap[key] != [] else -1
11
12    def remove(self, key: int) -> None:
13        if self.hashmap[key] != []:
14            self.hashmap[key] = []
15
16
17# Your MyHashMap object will be instantiated and called as such:
18# obj = MyHashMap()
19# obj.put(key,value)
20# param_2 = obj.get(key)
21# obj.remove(key)