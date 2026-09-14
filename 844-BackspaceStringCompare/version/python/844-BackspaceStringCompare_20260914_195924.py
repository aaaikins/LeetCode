# Last updated: 9/14/2026, 7:59:24 PM
1class Solution:
2    def backspaceCompare(self, s: str, t: str) -> bool:
3        # if len(s) != len(t):
4        #     return False
5
6        def helper(strs):
7            stack = []
8            for i in range(len(strs)):
9                
10                if strs[i] == "#":
11                    if stack:
12                        stack.pop()
13                else:
14                    stack.append(strs[i])
15                
16            return "".join(stack)
17        
18        print(helper(s))
19        print(helper(t))
20        return helper(s) == helper(t)
21