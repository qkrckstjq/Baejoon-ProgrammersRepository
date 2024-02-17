# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_balance(root) == -1:
            return False
        return True
        
    def get_balance(self, node):
        if node is None:
            return 0
        node_left = self.get_balance(node.left)
        node_right = self.get_balance(node.right)
    
        if node_left == -1 or node_right == - 1:
            return -1
        bf = node_left - node_right
        if bf < -1 or bf > 1:
            return -1
        return max(node_left, node_right) + 1
        