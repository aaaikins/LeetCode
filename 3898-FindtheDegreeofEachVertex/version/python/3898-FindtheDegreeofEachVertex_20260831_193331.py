# Last updated: 8/31/2026, 7:33:31 PM
1class Solution:
2    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
3        degrees = [sum(row) for row in matrix] 
4        
5        return degrees
6