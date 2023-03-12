# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.dic = defaultdict(list)
        
        self.travers(root, 0)
        res = self.dic.values()
        
        return res
        
    def travers(self, root,level):
        
        if not root:
            return 
        
        self.dic[level].append(root.val) 
        self.travers(root.left, level + 1)
        self.travers(root.right, level + 1)
        
        
        
        
        