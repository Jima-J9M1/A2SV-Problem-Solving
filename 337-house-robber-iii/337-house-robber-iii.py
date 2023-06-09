# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        
        def dp(node, state):
            if not node:
                return 0
            if (node,state) in memo:
                return memo[(node,state)]
            
            if not state:
                robe_left = dp(node.left, True)
                robe_right = dp(node.right, True)
                
            
            nrobe_left = dp(node.left, False)
            nrobe_right = dp(node.right, False)
            
            if not state:
                memo[(node,state)]= max(robe_left + robe_right + node.val, nrobe_left + nrobe_right)
                return max(robe_left + robe_right + node.val, nrobe_left + nrobe_right)
            
            memo[(node,state)]=nrobe_left + nrobe_right
            return memo[(node,state)]
            
        money = dp(root, False)
        
        return money
        
        
        
        