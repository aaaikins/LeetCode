class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)

        for course, prereq in prerequisites:
            courseMap[course].append(prereq)

        visited = set()
        fully_processed = set()

        def dfs(course):
            if course in visited: 
                return False
            if course in fully_processed:
                return True

            visited.add(course)
            for pre in courseMap[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            fully_processed.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

        