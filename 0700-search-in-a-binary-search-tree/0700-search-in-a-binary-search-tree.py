# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(cur_node):
            if not cur_node:
                return None
            
            if cur_node.val == val:
                return cur_node
            
            if cur_node.val > val:
                left = dfs(cur_node.left)
                if left:
                    return left
                
            if cur_node.val < val:
                right = dfs(cur_node.right)
                if right:
                    return right
                
                
            return None
        
        
        node = dfs(root)
        
        
        return node
                
            