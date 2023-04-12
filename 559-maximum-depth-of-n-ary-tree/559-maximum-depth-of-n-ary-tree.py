"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        max_val = [0]
        
        self.dfs(root, 1, max_val)
        return max_val[0]
        
    def dfs(self,node, level, max_val):
        
        
        for child in node.children:
            self.dfs(child, level + 1, max_val)
            
        max_val[0] = max(level, max_val[0])
    