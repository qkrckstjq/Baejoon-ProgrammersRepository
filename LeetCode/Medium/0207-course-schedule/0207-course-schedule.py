from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites) -> bool:
        visited = set()
        memo = set()
        require_graph = defaultdict(list)
        for target, require in prerequisites:
            require_graph[target].append(require)

        for node in range(numCourses):
            if node not in memo and self.has_cycle(node, require_graph, visited, memo):
                return False
        return True

    def has_cycle(self, start_node, require_graph, visited, memo):
        if start_node in memo:
            return False
        if start_node in visited:
            return True
        
        visited.add(start_node)
        for require in require_graph[start_node]:
            if self.has_cycle(require, require_graph, visited, memo):
                return True
        visited.remove(start_node)
        memo.add(start_node)
        return False