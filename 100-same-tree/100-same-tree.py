# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.equalTree(p,q)
    
    def equalTree(self,node1,node2):
        if node1 is None and node2 is None:
            return True
        
        if node1 is None or node2 is None or node1.val != node2.val:
            return False

        left = self.equalTree(node1.left,node2.left)
        right = self.equalTree(node1.right,node2.right)
        
        return left and right