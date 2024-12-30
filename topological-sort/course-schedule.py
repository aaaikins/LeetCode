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
            
            for pre in courseMap[crs]:
                if not dfs(pre):
                    return False
            return True

        for course in courseMap:
            if not dfs(course):
                return False
        return True

        