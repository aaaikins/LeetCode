class Solution:
    def longestPalindrome(self, s: str) -> str:

        def isPalindrome(s):
            l, r = 0, len(s) - 1

            while l < r:
                if s[l] != s[r]:
                    return False
                else:
                    l +=1
                    r -= 1
            return True
        l, r = 0, len(s) - 1
        # print(isPalindrome(s[l:r+1]))

        maxStr = ''
        while l <= r:
            if s[l] == s[r]:
                if isPalindrome(s[l:r+1]):
                    if (r-l+1) > len(maxStr):
                        maxStr = s[l:r+1]

            l += 1
            r -= 1

        return maxStr
        