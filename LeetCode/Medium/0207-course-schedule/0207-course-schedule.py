# https://www.lifencoding.com/algorithm/34?p=1
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
				
				# Input: numCourses = 3, prerequisites = [[1,0]]
				# 선수 강의 수(indegree)가 0 인것부터 그래프를 탐색한다
				
				# 그래프 초기화
        graph = defaultdict(list)
        indegree = [0] * numCourses # 강의의 선수 강의의 수를 담기 위한 리스트
        for next, pre in prerequisites:
            graph[pre].append(next)
            indegree[next] += 1

        # print(graph) # --> ({0: [1]})

				# graph    = {0: [2, 1], 1: [2]}
				# indegree = [0, 1, 2]

        
        start = [i for i in range(numCourses) if indegree[i] == 0] # 선수 강의가 0개인 노드 찾기
        stack = start
        
        while stack:
            pre = stack.pop()
            for next in graph[pre]: # 0 --> 1  //// indegree = [0, 1]
                indegree[next] -= 1   # ndegree # --> [0, 1] -> [0,0]
								# print(indegree) # ------
                if indegree[next] == 0: # 선수 강의가 0개이면 다시 큐에 넣는다
                    stack.append(next)
            
        # 위의 과정을 마쳤을 때 아직 선수 강의가 남아있는 강의가 있을 경우에는 False를 리턴
        for course in indegree:
            if course != 0:
                return False
        
        return True

