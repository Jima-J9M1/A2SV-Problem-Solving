# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            new_node = TreeNode(val)
            return new_node
        
        def dfs(cur_node):
            if not cur_node:
                new_node = TreeNode(val)
                return new_node
            
            
            if cur_node.val > val:
                cur_node.left = dfs(cur_node.left)
                
            else:
                cur_node.right = dfs(cur_node.right)
                
                
            return cur_node
        
        
        
        dfs(root)  
        
        return root