# Last updated: 7/13/2026, 3:55:47 PM
1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        l, r = 0, len(people) - 1
5        boats = 0
6
7        while l <= r:
8            if people[l] + people[r] <= limit:
9                l += 1
10            r -= 1
11            boats += 1
12        
13        return boats