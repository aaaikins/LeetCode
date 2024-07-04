class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s.lower() if char.isalnum()]
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
        