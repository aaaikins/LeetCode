class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)

        for course, prereq in prerequisites:
            courseMap[course].append(prereq)

        visited = set()

        def dfs(crs):
            if crs in visited: 
                return False
            if crs not in visited:
                return True

            visited.add(crs)
            for pre in courseMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            return True

        for course in courseMap:
            if not dfs(course):
                return False
        return True

        