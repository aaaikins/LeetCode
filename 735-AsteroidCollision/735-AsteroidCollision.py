# Last updated: 1/28/2026, 6:52:00 PM
1class Solution:
2    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
3        stack = []
4
5        for ast in asteroids:
6            while stack and ast < 0 and stack[-1] > 0:
7                if stack[-1] == abs(ast):
8                    ast = 0
9                    stack.pop()
10                elif stack[-1] > abs(ast):
11                    ast = 0
12                else:
13                    stack.pop()
14
15            if ast:
16                stack.append(ast)
17        
18        return stack