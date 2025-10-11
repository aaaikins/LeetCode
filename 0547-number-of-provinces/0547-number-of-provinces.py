class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        visit = set()
        provinces = 0

        def dfs(city):
            for neighbor in range(rows):
                if isConnected[city][neighbor] == 1 and neighbor not in visit:
                    visit.add(neighbor)
                    dfs(neighbor)


        for city in range(rows):
            if city not in visit:
                provinces += 1
                visit.add(city)
                dfs(city)

        return provinces