# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)]
        d = 0
        height_dict = {None: 0}

        while stack:
            node, visited = stack.pop()

            if node:
                if visited:
                    left_height = height_dict[node.left]
                    right_height = height_dict[node.right]
                    d = max(d, left_height + right_height)
                    height_dict[node] = max(left_height, right_height) + 1
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
            else:
                height_dict[node] = 0

        return d