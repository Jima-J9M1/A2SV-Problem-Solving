# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = [[]]
        self.dfs(root, "",res)
        ans = 0
        for ele in res[0]:
            ans += int(ele,2)
        
        return ans
    def dfs(self,curNode, binary, res):
        if not curNode:
            return 
        
        if not curNode.left and not curNode.right:
            binary += str(curNode.val)
            res[0].append(binary)
            return
            
        
        self.dfs(curNode.left, binary + str( curNode.val) , res)
        self.dfs(curNode.right, binary +  str( curNode.val), res)
        