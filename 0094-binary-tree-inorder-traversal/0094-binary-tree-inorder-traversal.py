# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        
        ans = []
        def dfs(cur_node):
            if not cur_node:
                return
            
            dfs(cur_node.left)
            ans.append(cur_node.val)
            dfs(cur_node.right)
            
            
            return 
            
            
        dfs(root)
        return ans