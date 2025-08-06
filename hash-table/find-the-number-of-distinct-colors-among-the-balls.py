class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        def overZero(hashmap):
            count = 0 
                        
            for key in hashmap:
                if hashmap[key] > 0:
                    count += 1 
                        
            return count
        balltoColor = defaultdict(int)    #O(n) space complexity
        colorToFreq = defaultdict(int)    #O(n) space complexity 
        
        res = []
        
        for ball, color in queries:  #O(n^2) time_complexity 
            if ball in balltoColor:
                #get prev color of ball
                oldColor = balltoColor[ball]
                
                #decrement that color because we will change it 
                colorToFreq[oldColor] -= 1
                
                #update color of ball
                balltoColor[ball] = color
                
                # increment new color freq by 1
                colorToFreq[color] += 1
                
                
            else:
                balltoColor[ball] = color
                colorToFreq[color] += 1
            
            res.append(overZero(colorToFreq))
            
        return res