class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            elif token == '*':
                stack.append(stack.pop() * stack.pop())
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/ a))
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            else:
                stack.append(int(token))
            print(stack)
        
        return stack.pop()
        