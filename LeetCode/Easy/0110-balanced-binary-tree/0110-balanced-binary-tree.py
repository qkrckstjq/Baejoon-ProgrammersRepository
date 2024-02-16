# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return True if self.get_height(root) != -1 else False
    
    def get_height(self, node):
        if node is None:
            return 0
        left = self.get_height(node.left)
        right = self.get_height(node.right)
        
        if abs(left - right) > 1:
            return -1
        if left == -1 or right == -1:
            return -1
        return max(left, right) + 1