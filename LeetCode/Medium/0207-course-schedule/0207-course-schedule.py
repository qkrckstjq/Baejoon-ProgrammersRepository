from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visited = [0] * numCourses

        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == -1:
                return True

            visited[course] = 1
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            visited[course] = -1
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True