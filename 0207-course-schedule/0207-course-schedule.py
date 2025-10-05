class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i:[] for i in range(numCourses)}
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            graph[pre].append(crs)
            in_degree[crs] += 1
                
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        visited_count = 0

        while queue:
            cur = queue.popleft()
            visited_count += 1

            for csr in graph[cur]:
                in_degree[csr] -= 1

                if in_degree[csr] == 0:
                    queue.append(csr)

        return visited_count == numCourses


        

        # print(graph)
        # print(queue)

        # return True