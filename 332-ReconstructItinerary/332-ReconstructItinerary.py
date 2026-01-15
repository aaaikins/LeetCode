# Last updated: 1/15/2026, 12:43:20 PM
1class Solution:
2    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
3
4        tickets.sort(reverse=True)
5        graph = defaultdict(list)
6        
7        for start, end in tickets:
8            graph[start].append(end)
9        
10        itinerary = []
11
12        def dfs(start):
13            
14            while graph[start]:
15                next_des = graph[start].pop()
16                dfs(next_des)
17            itinerary.append(start)
18                
19        dfs("JFK")
20        return itinerary[::-1]