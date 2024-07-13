class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        i = 0
        j = 1
        maxLength = 0
        if len(s) <= 1:
            return len(s)

        while j < len(s):
            visited.add(s[i])
            while s[j] in visited:
                visited.remove(s[i])
                i +=1
            visited.add(s[j])
            maxLength = max(maxLength, len(visited))
            j += 1
        return maxLength