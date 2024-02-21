from collections import defaultdict

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        stack = [(len(matrix) // 2, len(matrix[0]) // 2)]
        visit = defaultdict(set)
        while stack:
            cur_y, cur_x = stack.pop()
            cur_value = matrix[cur_y][cur_x]
            visit[cur_y].add(cur_x)
            if cur_value == target:
                return True
            if cur_value < target:
                next_y = cur_y + 1
                next_x = cur_x + 1
                if not cur_x in visit[next_y] and self.is_possible(matrix, next_y, cur_x):
                    stack.append((next_y, cur_x))
                if not next_x in visit[cur_y] and self.is_possible(matrix, cur_y, next_x):
                    stack.append((cur_y, next_x))
            if cur_value > target:
                next_y = cur_y - 1
                next_x = cur_x - 1
                if not cur_x in visit[next_y] and self.is_possible(matrix, next_y, cur_x):
                    stack.append((next_y, cur_x))
                if not next_x in visit[cur_y] and self.is_possible(matrix, cur_y, next_x):
                    stack.append((cur_y, next_x))
            
        return False
    
    def is_possible(self, matrix, y, x):
        return True if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]) else False
    