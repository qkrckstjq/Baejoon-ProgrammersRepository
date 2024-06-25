from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        queue = deque()
        queue.append([root, 0])
        while queue:
            cur_node, depth = queue.popleft()
            if cur_node:
                cur_val = cur_node.val
                if depth < len(answer):
                    answer[depth] = cur_val
                else:
                    answer.append(cur_val)
            
            if cur_node:
                if cur_node.left:
                    queue.append([cur_node.left, depth + 1])
                if cur_node.right:
                    queue.append([cur_node.right, depth + 1])
                
        return answer