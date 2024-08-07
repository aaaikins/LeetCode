class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [word for word in s.lower() if word.isalnum()]
        
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -=1
        
        return True
        