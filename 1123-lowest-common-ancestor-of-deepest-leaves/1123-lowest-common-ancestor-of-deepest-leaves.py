# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        max_level = [float("-inf")]
        self.deepest(root, 0, max_level)
        
        lowestAncestor = [[]]
        ans = self.lowestCommonAncestor(root, 1, max_level, [], lowestAncestor)
        
        return ans
    
    
    def deepest(self, root, level, max_level):
        if not root:
            max_level[0] = max(max_level[0], level)
            return 
        
        left = self.deepest(root.left, level + 1, max_level)
        right = self.deepest(root.right, level + 1, max_level)
        
        return 
    
    def lowestCommonAncestor(self, cur, level, max_level, result, lowestAncestor):
        
        if cur and level == max_level[0]:
            return cur
            
        if not cur:
            return None
        
        left = self.lowestCommonAncestor(cur.left, level + 1, max_level, result + [cur.val], lowestAncestor)
        right = self.lowestCommonAncestor(cur.right, level + 1, max_level, result + [cur.val], lowestAncestor)
        
        if left == None:
            return right
        
        if right == None:
            return left
        
        return cur
        
        
        
        