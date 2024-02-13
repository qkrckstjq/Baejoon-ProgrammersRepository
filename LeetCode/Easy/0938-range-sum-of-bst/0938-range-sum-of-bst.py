# Definition for a binary tree node.
# low와 high의 사이의 값을 가진 노드라면 양쪽 자식 모두 탐색
# low보다 작다면 오른쪽 탐색
# hight보다 크다면 왼쪽 탐색
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        result = 0
        
        while stack:
            cur_node = stack.pop()
            if cur_node == None:
                continue
            state = self.get_state(cur_node.val, low, high)
            if state == 0:
                result += cur_node.val
                stack.append(cur_node.left)
                stack.append(cur_node.right)
            if state == 1:
                stack.append(cur_node.right)
            if state == 2:
                stack.append(cur_node.left)
                
        return result
            
    def get_state(self, num, low, high):
        if low <= num <= high:
            return 0
        if num < low:
            return 1
        if num > high:
            return 2