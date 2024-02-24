from collections import defaultdict
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        mid_y = len(matrix) // 2
        mid_x = len(matrix[0]) // 2
        visit = defaultdict(set)
        return self.recursion(matrix, mid_y, mid_x, target, visit)

    def recursion(self, matrix, y, x, target, visit):
        if self.out_of_range(matrix, y, x) or x in visit[y]:
            return False
        if matrix[y][x] == target:
            return True
        y_y = y
        x_x = x
        visit[y].add(x)
        if matrix[y][x] < target:
            y_y += 1
            x_x += 1
        else:
            y_y -= 1
            x_x -= 1
        result_y = self.recursion(matrix, y_y, x, target, visit)
        result_x = self.recursion(matrix, y, x_x, target, visit)
        return True if result_y or result_x else False

    def out_of_range(self, matrix, y, x):
        return False if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]) else True