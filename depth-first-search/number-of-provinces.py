class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visit = set()
        n = len(isConnected)
        def dfs(start):
            visit.add(start)
            for end in range(n):
                if isConnected[start][end] and end not in visit:
                    dfs(end)

        for start in range(n):
            if start not in visit:
                provinces += 1
                dfs(start)

        return provinces
        