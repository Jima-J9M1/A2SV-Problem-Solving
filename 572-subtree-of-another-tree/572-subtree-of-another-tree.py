# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.ans = False
        
        self.dfs(root, subRoot)
        return self.ans
    
    def dfs(self,root,subRoot):
        if root is None:
            return 
        
        if root.val == subRoot.val:
            if self.compare(root, subRoot):
                self.ans = True
                
        self.dfs(root.left,subRoot)
        self.dfs(root.right , subRoot)
            
            
            
    def compare(self,root_left,root_right):
        
        if root_left is None and root_right is None:
            return True
        
        if root_left is None or root_right is None or root_left.val != root_right.val:
            return False
        
        left = self.compare(root_left.left, root_right.left)
        right = self.compare(root_left.right,root_right.right)
        
        return left and right