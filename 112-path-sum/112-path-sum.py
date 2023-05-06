# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, 0, targetSum)
    
    def dfs(self, root, add, target):
        if not root:
            return False
        if not root.left and not root.right:
            
            if add+root.val == target:
                return True
            
            return False
        
        
            
        
        add += root.val
        left = self.dfs(root.left, add, target)
        
        
        right = self.dfs(root.right, add, target)
        
        return left or right