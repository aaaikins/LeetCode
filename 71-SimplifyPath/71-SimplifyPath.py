# Last updated: 9/20/2026, 8:00:39 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        path = path.split("/")
4
5        stack = []
6
7        for part in path:
8            if part == '' or part == '.':
9                continue
10            if part == "..":
11                if stack:
12                    stack.pop()
13            else:
14                stack.append(part)
15        
16        return "/" + "/".join(stack)
17