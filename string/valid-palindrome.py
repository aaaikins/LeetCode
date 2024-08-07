class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [word.lower() for word in s if word.isalnum()]
        
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -=1
        
        return True
        