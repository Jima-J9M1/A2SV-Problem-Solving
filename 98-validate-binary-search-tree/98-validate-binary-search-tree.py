# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.BTS(root, [float ("+inf")])
        
    def BTS(self, curr, prev):
        
        if not curr:
            return True
        
        left = self.BTS(curr.left, prev)
        
        if prev[0] != float ("+inf") and prev[0] >= curr.val:
            return False
        
        prev[0] = curr.val
        
        right = self.BTS(curr.right, prev)
                
        return right and left
    
        
        