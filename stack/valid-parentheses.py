class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in s:
            if stack and i in brackets:
                cur = stack.pop()
                if cur != brackets[i]:
                    return False
            else:
                stack.append(i)
            

        return len(stack) == 0
            
        