# Last updated: 5/12/2026, 6:11:50 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        brackets_map = {')': '(', ']':'[', '}':'{'}
4
5        stack = []
6
7        for b in s:
8            if b in brackets_map:
9                if not stack or stack[-1] != brackets_map[b]:
10                    return False
11                stack.pop()
12            else:
13                stack.append(b)
14
15        return len(stack) == 0
16