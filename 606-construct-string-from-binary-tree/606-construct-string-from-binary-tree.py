# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        path = [""]
        self.dfs(root, path)
        ans = path[0][:-1]
        
        return ans
        
    def dfs(self, node, path):
        if node.left == None and node.right == None:
            path[0] += str(node.val)
            path[0] += ")"
            return 
        
        path[0] += str(node.val)

        if node.left:
            path[0] += "("
            left = self.dfs(node.left, path)
        
        else:
            path[0] += "("
            path[0] += ')'
            
        if node.right:
            path[0] += "("
            right = self.dfs(node.right, path)
        # else:
            # path[0] += ')'
            
        path[0] += ")"
        return 
        
        
            
        
        
        