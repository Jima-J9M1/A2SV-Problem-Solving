# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        def dfs(curr,maxp,minp):
            
            
            if not curr:
                return
            
            
            maxp = max(maxp,curr.val)
            minp = min(minp,curr.val)
            
            self.best = max(self.best,abs(maxp-minp))
            
            dfs(curr.left,maxp,minp)
            dfs(curr.right,maxp,minp)
            
        
        dfs(root,-float('inf'),float('inf'))
        return self.best