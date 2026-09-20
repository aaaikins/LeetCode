# Last updated: 9/20/2026, 7:56:40 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        path = path.split("/")
4
5        print(path)
6
7        stack = []
8
9        for dr in path:
10            if dr == '' or dr == '.':
11                continue
12            if dr == "..":
13                if stack:
14                    stack.pop()
15            else:
16                stack.append(dr)
17        
18        return "/" + "/".join(stack)
19