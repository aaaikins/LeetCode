class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visit = set()
        rows, cols = len(isConnected), len(isConnected[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or isConnected[r][c] == 0
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c] == 1 and (r, c) not in visit:
                    provinces += 1
                    dfs(r, c)
        return provinces
        