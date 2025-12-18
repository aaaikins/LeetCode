# Last updated: 12/18/2025, 1:50:26 PM
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        minLen = float('inf')
        visited = set()

        l, r = 0, 0

        while r < len(cards):
            while cards[r] in visited:
                minLen = min(minLen, r - l + 1)
                visited.remove(cards[l])
                l += 1

            visited.add(cards[r])
            # cur_len = r-l + 1
            r += 1
            
        
        return minLen if minLen != float('inf') else -1