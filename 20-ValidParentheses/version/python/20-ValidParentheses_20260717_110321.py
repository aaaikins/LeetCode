# Last updated: 7/17/2026, 11:03:21 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        brackets = {
4            ")": "(",
5            "}": "{",
6            "]": "["
7        }
8
9        stack = []
10
11        for c in s:
12            if stack:
13                if c in brackets and stack[-1] == brackets[c]:
14                    stack.pop()
15                else:
16                    stack.append(c)
17            else:
18                stack.append(c)
19
20        
21        return len(stack) == 0
22        