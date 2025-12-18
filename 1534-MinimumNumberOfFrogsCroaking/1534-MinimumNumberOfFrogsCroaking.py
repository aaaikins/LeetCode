# Last updated: 12/18/2025, 1:50:46 PM
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croaks = {'c': 0, 'r':0,'o':0, 'a': 0, 'k': 0}
        cur_frog, max_frog = 0, 0

        for c in croakOfFrogs:
            croaks[c] += 1
            if c == 'c':
                cur_frog += 1  # New frog starts croaking
                max_frog = max(max_frog, cur_frog)
            elif c == 'r' and croaks['r'] > croaks['c']:
                return -1
            elif c == 'o' and croaks['o'] > croaks['r']:
                return -1
            elif c == 'a' and croaks['a'] > croaks['o']:
                return -1
            elif c == 'k':
                if croaks['k'] > croaks['a']:
                    return -1
                cur_frog -= 1

        if croaks['c'] == croaks['r'] == croaks['o'] == croaks['a'] == croaks['k']:
            return max_frog
        else:
            return -1