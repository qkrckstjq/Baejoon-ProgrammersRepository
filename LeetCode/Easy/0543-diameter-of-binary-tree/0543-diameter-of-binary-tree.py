# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    height = {}
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        stack = [root]
        
        while stack:
            cur_node = stack.pop()
            cur_node_diameter = self.get_diameter(cur_node)
            max_diameter = max(cur_node_diameter, max_diameter)
            
            if cur_node.left is not None:
                stack.append(cur_node.left)
            if cur_node.right is not None:
                stack.append(cur_node.right)
        return max_diameter
    
    def get_diameter(self, root):
        if root is None:
            return 0
        left_len = self.get_max_depth(root.left)
        right_len = self.get_max_depth(root.right)
        return left_len + right_len
        
    
    def get_max_depth(self, node):
        if node is None:
            return 0
        
        if node in self.height:
            return height[node]
        
        result = 0
        diameter = 0
        stack = [[node, diameter]]
        while stack:
            cur = stack.pop()
            cur_node = cur[0]
            cur_diameter = cur[1]
            diameter = max(diameter, cur_diameter)
            if cur_node.left is not None:
                stack.append([cur_node.left, cur_diameter + 1])
            if cur_node.right is not None:
                stack.append([cur_node.right, cur_diameter + 1])
        self.height[node] = diameter
        return diameter + 1