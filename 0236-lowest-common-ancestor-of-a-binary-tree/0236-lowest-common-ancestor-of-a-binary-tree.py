# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
        
        
    def dfs(self, root,node1,node2):
        if not root:
            return 
        
        if root == node1 or root == node2:
            return root
        
        left = self.dfs(root.left, node1, node2)
        right = self.dfs(root.right, node1, node2)
        
        if (left == None):
            return right
        if (right == None):
            return left
        
        return root