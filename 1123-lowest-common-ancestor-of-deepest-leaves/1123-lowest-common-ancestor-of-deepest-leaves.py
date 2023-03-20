# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        max_level = [float("-inf")]
        self.deepest(root, 0, max_level)
        
        
        ans = self.lowestCommonAncestor(root, 1, max_level)
        
        return ans
    
    '''
    @param: root -> current node
    @param: level -> determine the level of the current node
    @param: max_level -> maximum depth of the tree
    
    '''
    def deepest(self, root, level, max_level):
        if not root:
            max_level[0] = max(max_level[0], level)
            return 
        
        left = self.deepest(root.left, level + 1, max_level)
        right = self.deepest(root.right, level + 1, max_level)
        
        return 
    
    '''
    @param: root -> current node
    @param: level -> determine the level of the current node
    @param: max_level -> maximum depth of the tree
    '''
    def lowestCommonAncestor(self, cur, level, max_level):
        
        # return the current node if the level of the current node is equal to the maximum node
        if cur and level == max_level[0]:
            return cur
            
        if not cur:
            return None
        
        left = self.lowestCommonAncestor(cur.left, level + 1, max_level)
        right = self.lowestCommonAncestor(cur.right, level + 1, max_level)
        
        # if the left node is invalid based on the maximu level return the valid one which is right
        if left == None:
            return right
        
        # if the right node is invalid based on the maximu level return the valid one which is left
        if right == None:
            return left
        
        #if both side is valid which means the lowest common ancestor is the parent node, return the parent node
        return cur
        
        
        
        