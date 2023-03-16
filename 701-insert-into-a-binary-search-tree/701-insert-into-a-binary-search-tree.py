# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        return self.dfs(root, val)
    
    def dfs(self, node,val):

        if not node:
            new_node = TreeNode(val)
            return new_node

        if node.val > val:
            node.left = self.dfs(node.left, val)

        elif node.val < val:
            node.right = self.dfs(node.right, val)


        return node
            