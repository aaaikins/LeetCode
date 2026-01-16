# Last updated: 1/15/2026, 7:38:12 PM
1from collections import defaultdict
2
3class Solution:
4    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
5        graph = defaultdict(list)
6
7        # Sort tickets so we can pop smallest lex destination last
8        for src, dst in sorted(tickets, reverse=True):
9            graph[src].append(dst)
10
11        stack = ["JFK"]
12        itinerary = []
13
14        while stack:
15            curr = stack[-1]
16            if graph[curr]:
17                stack.append(graph[curr].pop())
18            else:
19                itinerary.append(stack.pop())
20
21        return itinerary[::-1]
22