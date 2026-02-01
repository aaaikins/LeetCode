# Last updated: 1/31/2026, 7:05:07 PM
1class StockSpanner:
2
3    def __init__(self):
4        self.stack = []
5
6    def next(self, price: int) -> int:
7        if not self.stack:
8            self.stack.append((price, 1))
9            return 1
10
11        span = 1
12        while self.stack and price >= self.stack[-1][0]:
13            span += self.stack[-1][1]
14            self.stack.pop()
15        
16        self.stack.append((price, span))
17
18        return span
19        
20
21
22# Your StockSpanner object will be instantiated and called as such:
23# obj = StockSpanner()
24# param_1 = obj.next(price)