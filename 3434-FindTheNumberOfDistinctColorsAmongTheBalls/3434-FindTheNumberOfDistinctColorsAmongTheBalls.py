# Last updated: 12/18/2025, 1:49:58 PM
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        balltoColor = defaultdict(int)    #O(n) space complexity
        colorToFreq = defaultdict(int)    #O(n) space complexity 
        visit = set()

        res = []
        
        for ball, color in queries:  #O(n^2) time_complexity 
            if ball in balltoColor:
                #get prev color of ball
                oldColor = balltoColor[ball]
                
                #decrement that color because we will change it 
                colorToFreq[oldColor] -= 1
                if colorToFreq[oldColor] == 0:
                    visit.remove(oldColor)
                #update color of ball
                balltoColor[ball] = color
                
                # increment new color freq by 1
                colorToFreq[color] += 1
                visit.add(color)
                
            else:
                balltoColor[ball] = color
                colorToFreq[color] += 1
                visit.add(color)
            
            res.append(len(visit))
            
        return res