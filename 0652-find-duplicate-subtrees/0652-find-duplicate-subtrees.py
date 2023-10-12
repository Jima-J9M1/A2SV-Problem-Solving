# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        res = []
        _dict = defaultdict(int)
        
        def dfs(node):
            if not node:
                return " "
            
            st = str(node.val) + " "+ dfs(node.left) + " "+ dfs(node.right)
            
            if _dict[st] == 1:
                res.append(node)
                
            _dict[st] += 1
            
            
            return st
        
        
        dfs(root)
        
        return res
        
        
            
            