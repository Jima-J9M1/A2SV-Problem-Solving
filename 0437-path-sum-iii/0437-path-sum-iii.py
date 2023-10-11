# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        hashmap = defaultdict(int, {0:1})
        ans = self.dfs(root,0, hashmap, targetSum)
        
        return ans
    
    def dfs(self, curNode, prefix_sum, hashmap, targetSum):
        if not curNode:
            return 0
        
        
        prefix_sum += curNode.val
        path = hashmap[prefix_sum - targetSum]
        
        hashmap[prefix_sum] += 1
        left = 0
        right = 0
        
        left += self.dfs(curNode.left,prefix_sum ,hashmap, targetSum)
        right += self.dfs(curNode.right, prefix_sum, hashmap, targetSum)
        
        hashmap[prefix_sum] -= 1
        
        return path + left + right