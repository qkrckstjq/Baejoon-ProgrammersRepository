from collections import defaultdict
class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        memo = set()
        visit = set()
        require_graph = defaultdict(list)
        for target, require in prerequisites:
            require_graph[target].append(require)

        courses = list(require_graph.keys())
        for vertex in courses:
            if vertex in memo:
                continue
            elif self.has_cycle(require_graph, memo, visit, vertex):
                return False
        return True

    def has_cycle(self, graph, memo, visit, node):
        if node in memo:
            return False
        if node in visit:
            return True
        visit.add(node)
        for require in graph[node]:
            if self.has_cycle(graph, memo, visit, require):
                return True
        visit.remove(node)
        memo.add(node)
        return False

test = Solution()
# print(test.canFinish(7, [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]))
print(test.canFinish(3, [[1,0],[1,2],[0,1]]))