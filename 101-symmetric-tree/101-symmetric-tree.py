# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.bfs(root.left , root.right)
    
    def bfs(self, node_left, node_right):
        if node_left is None and node_right is None:
            return True
        
        if node_left is None or node_right is None or node_left.val != node_right.val:
            return False
        
        left = self.bfs(node_left.left, node_right.right)
        right = self.bfs(node_left.right, node_right.left)
        
        return left and right