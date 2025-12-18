# Last updated: 12/18/2025, 1:50:30 PM
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sec = 0
        i = 0
        while tickets[k] > 0:
            if tickets[i] != 0:
                tickets[i] -= 1
                sec += 1
                i += 1
            else:
                i += 1   
            if i == len(tickets):
                i = 0

        return sec
        