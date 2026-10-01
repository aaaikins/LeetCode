# Last updated: 10/1/2026, 4:07:40 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        bracketsMap = {")": "(", "}":"{", "]":"["}
4        stack = []
5
6        for ch in s:
7            if ch in bracketsMap:
8                if stack:
9                    top = stack.pop()
10                    if top != bracketsMap[ch]:
11                        return False
12                else:
13                    stack.append(ch)
14            else:
15                stack.append(ch)
16        
17        return len(stack) == 0