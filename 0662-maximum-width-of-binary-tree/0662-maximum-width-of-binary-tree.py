# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        nodes = defaultdict(list)
        def dfs(node, level, value):
            if not node:
                return
            nodes[level].append(value)
            dfs(node.left, level + 1, value * 2)
            dfs(node.right, level + 1, value * 2 + 1)
        
        dfs(root, 0, 1)
        ans = 0
        
        for interval in nodes.values():
            ans = max(ans, interval[-1] - interval[0] + 1)
        return ans
                
                