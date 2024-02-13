class Solution:
    def dfs_cycle(self, graph, vertex, visited, visit):
        if vertex in visit:
            return True
        
        if vertex in visited:
            return False
        
        visited.add(vertex)
        visit.add(vertex)
        
        if vertex in graph:
            for next_vertex in graph[vertex]:
                if self.dfs_cycle(graph, next_vertex, visited, visit):
                    return True
        
        visit.remove(vertex)
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        
        for vertex, require_vertex in prerequisites:
            if vertex in graph:
                graph[vertex].append(require_vertex)    
            else:
                graph[vertex] = [require_vertex]
        
        visited = set()
        
        for vertex in graph.keys():
            if self.dfs_cycle(graph, vertex, visited, set()):
                return False
        return True