# Last updated: 3/2/2026, 6:04:42 PM
1class MyCalendar:
2
3    def __init__(self):
4        self.bookings = []
5
6    def book(self, startTime: int, endTime: int) -> bool:
7        for start, end in self.bookings:
8            if startTime < end and endTime > start:
9                return False
10        self.bookings.append([startTime, endTime])
11        return True
12        
13
14
15# Your MyCalendar object will be instantiated and called as such:
16# obj = MyCalendar()
17# param_1 = obj.book(startTime,endTime)