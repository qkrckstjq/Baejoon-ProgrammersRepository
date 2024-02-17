# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         max_len = {'max' : 0}
#         self.find_max_len(root, max_len)
#         return max_len['max']
    
#     def find_max_len(self, node, max_len):
#         if node is None:
#             return 0
#         left_len = self.find_max_len(node.left, max_len)
#         right_len = self.find_max_len(node.right, max_len)
#         max_len['max'] = max(max_len['max'], left_len + right_len)
#         return max(self.find_max_len(node.left, max_len), self.find_max_len(node.right, max_len)) + 1
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_len = {'max': 0}
        self.find_max_len(root, max_len)
        return max_len['max']
    
    def find_max_len(self, node, max_len):
        if node is None:
            return 0
        left_len = self.find_max_len(node.left, max_len)
        right_len = self.find_max_len(node.right, max_len)
        max_len['max'] = max(max_len['max'], left_len + right_len)
        return max(left_len, right_len) + 1