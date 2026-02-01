# Last updated: 1/31/2026, 7:05:48 PM
1class StockSpanner:
2
3    def __init__(self):
4        self.stack = []
5
6    def next(self, price: int) -> int:
7        span = 1
8        while self.stack and price >= self.stack[-1][0]:
9            span += self.stack[-1][1]
10            self.stack.pop()
11        
12        self.stack.append((price, span))
13
14        return span
15        
16
17
18# Your StockSpanner object will be instantiated and called as such:
19# obj = StockSpanner()
20# param_1 = obj.next(price)