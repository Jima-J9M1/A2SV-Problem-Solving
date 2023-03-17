# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hashmap = defaultdict(int, {0:1})
        ans = self.dfs(root, 0, hashmap, targetSum)
        
        return ans
        
    def dfs(self, curr, prefx_sum, hashmap, target):
        
        if not curr:
            return 0
        
        prefx_sum += curr.val
        
        path = hashmap[prefx_sum - target]
        
        hashmap[prefx_sum] += 1
        
        path += self.dfs(curr.left, prefx_sum, hashmap, target) + self.dfs(curr.right, prefx_sum, hashmap, target)
        
        hashmap[prefx_sum] -= 1
        
        
        return path