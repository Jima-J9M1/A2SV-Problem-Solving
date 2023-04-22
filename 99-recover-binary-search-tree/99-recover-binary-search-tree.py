# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        self.traversal(root, res)
        res.sort()
        self.dfs(root, res, [0])
        
        
    def traversal(self, node,res):
        if not node:
            return
        
        
        self.traversal(node.left,res)
        res.append(node.val)
        self.traversal(node.right,res)
        
        
        return
    
    def dfs(self, node,res, indx):
        if not node:
            return
        
        
        self.dfs(node.left,res, indx)
        node.val = res[indx[0]]
        indx[0] = indx[0] + 1
        
        self.dfs(node.right,res, indx)
        
        
        return
        
        