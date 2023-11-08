# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        dict_ = defaultdict(list)
        
        
        def dfs(root, row, col):
            
            if not root:
                return
            
            dict_[col].append((row, root.val))
            

            dfs(root.left, row + 1, col - 1 )
            dfs(root.right, row + 1, col + 1)
            
            
            return
        
        
        dfs(root, 0, 0)
        
        
        res = []
        for key in sorted(dict_):
            sorted_list = sorted(dict_[key])
            
            ans = []
            for ele in sorted_list:
                ans.append(ele[1])
            res.append(ans)\
            
            
        return res
            
            
            