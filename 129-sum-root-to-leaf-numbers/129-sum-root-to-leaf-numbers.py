# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = self.dfs(root, "")
        
        return int(ans)
    def dfs(self, curNode, path):
        if not curNode:
            return 0
        
        if not curNode.left and not curNode.right:
            return path + str(curNode.val)
        
        left = self.dfs(curNode.left, path + str(curNode.val))
        right = self.dfs(curNode.right, path + str(curNode.val))
 
        return str(int(left) + int(right))
    