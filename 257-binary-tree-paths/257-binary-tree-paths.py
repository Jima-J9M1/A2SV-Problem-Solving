# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.left_res = []

    
        def rightAndLeft(root,str_val):
            
            
            str_val.append(str(root.val))

            if not root.left and not root.right:
                self.left_res.append("".join(str_val))
                return
            
            if root.left:
                rightAndLeft(root.left,str_val.copy() + ["->"] )
            
            if root.right:
                rightAndLeft(root.right, str_val.copy() + ["->"])
            
        
        rightAndLeft(root,[])
        return self.left_res
            
            