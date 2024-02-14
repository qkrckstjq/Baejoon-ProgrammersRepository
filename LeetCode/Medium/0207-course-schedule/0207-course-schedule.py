from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        memo = set()
        visit = set()
        require_graph = defaultdict(list)
        for target, require in prerequisites:
            require_graph[target].append(require)

        for vertex in range(numCourses):
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
