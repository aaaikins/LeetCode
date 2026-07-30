# Last updated: 7/29/2026, 8:31:36 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        """
4        mapping = { ")": "(", "}": "{", "]":"["}
5       
6       s = "([])"
7
8        stack = [(, ]
9        for c in s:
10            if stack and c in mapping:
11                top = stack[-1]
12                if top == mapping[c]: 
13                    stack.pop()
14                else:
15                    return False
16            else:
17                stack.append(c)
18
19        return len(stack) == 0
20
21        """
22        
23        mapping = { ")": "(", "}": "{", "]":"["}
24
25        stack = []
26        for c in s:
27            if stack and  c in mapping:
28                top = stack[-1]
29                if top == mapping[c]:
30                    stack.pop()
31                else: 
32                    return False
33            
34            else:
35                stack.append(c)
36            
37        return len(stack) == 0
38
39
40
41