# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = [0]
        self.traversal(root, None, None, res)
        
        return res[0]
        
    def traversal(self, node, grandPa, parent, res):
        if not node:
            return
        
        if grandPa and grandPa.val % 2 == 0:
            res[0] += node.val
            
            
            
        
        self.traversal(node.left, parent, node, res)
        self.traversal(node.right, parent, node, res)
        
        
        