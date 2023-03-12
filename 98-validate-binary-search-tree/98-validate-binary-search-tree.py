# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.BTS(root, [float ("+inf")])
        
    #validate binary search tree with inorder traversal
    '''
    @param: curr -> the current node of the tree
    @param: prev -> the previous node of the tree
    
    '''
    def BTS(self, curr, prev):
        #if the current is none return true 
        if not curr:
            return True
        
        left = self.BTS(curr.left, prev)
        #the previous node different and if prevous value is greater than the current value the return false 
        if prev[0] != float ("+inf") and prev[0] >= curr.val:
            return False
        #assign the current value to the previous value
        prev[0] = curr.val
        
        #travres to the right 
        right = self.BTS(curr.right, prev)
         
        #return boolean value using and opperatoin
        return right and left
    
        
        