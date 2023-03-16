# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        best = [0]
        self.dfs(root,float("+inf"), float("-inf"), best)
        
        return best[0]
    
    def dfs(self,cur, min_val,max_val, best):
        if not cur:
            return 
        
        max_val = max(max_val, cur.val)
        min_val = min(min_val, cur.val)
        
        best[0] = max(best[0], max_val - min_val)
        
        self.dfs(cur.left, min_val, max_val, best)
        self.dfs(cur.right, min_val, max_val, best)
        
        return 
        