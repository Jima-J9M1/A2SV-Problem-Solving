# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = [[]]
        count = [[]]
        self.dfs(root, val,[0],k)
        
        return val[0]
    
    #inorder traversal 
    def dfs(self, root, val, count, k):
        if not root:
            return 0
        
        # find the smallest number to the left 
        self.dfs(root.left, val, count,k)
        
        # count the value of the root based on increasing 
        count[0] += 1
        
        #check if the element is the kth smallest element in the tree assign it to the val
        if count[0] == k:
            val[0] = root.val
        
        #travers to the right of the tree to find the elements based on the increment
        self.dfs(root.right, val, count, k)
            
        
        return count[0]
    
        
        