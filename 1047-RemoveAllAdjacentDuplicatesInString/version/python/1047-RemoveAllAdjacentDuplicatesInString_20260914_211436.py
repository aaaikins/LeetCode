# Last updated: 9/14/2026, 9:14:36 PM
1class Solution:
2    def removeDuplicates(self, s: str) -> str:
3        stack = []
4
5        for ch in s:
6            if stack:
7                if stack[-1] == ch:
8                    stack.pop()
9                else:
10                    stack.append(ch)
11            else:
12                stack.append(ch)
13        
14
15        return "".join(stack)