# Last updated: 7/29/2026, 7:21:02 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        mapping = {')': '(', '}': '{', ']': '['}
4        stack = []
5
6        for c in s:
7            if stack and c in mapping:
8                top = stack.pop()
9                if mapping[c] != top:
10                    return False
11            else:
12                stack.append(c)
13        
14        return not stack