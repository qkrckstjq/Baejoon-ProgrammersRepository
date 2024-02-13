# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    max_len = 0
    memo = {}
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recursion_tree(root)
        return self.max_len
        
    def recursion_tree(self, root):
        if root is None:
            return 0
        if root in self.memo:
            return self.memo[root]
            
        left_len = self.recursion_tree(root.left)
        right_len = self.recursion_tree(root.right)
        # print("현재 루트", root)
        # print("현재 left",left_len)
        # print("현재 right",right_len)
        # print("현재 max_len", self.max_len)
        self.memo[root] = left_len + right_len + 1
        self.max_len = max(left_len + right_len, self.max_len)
        return max(left_len, right_len) + 1
        
            
        