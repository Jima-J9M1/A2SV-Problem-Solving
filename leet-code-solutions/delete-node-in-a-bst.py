# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        
        def findRightMin(node):
            
            while node.left != None:
                node = node.left
                
                
            return node
            
            
        def dNode(cur_node, key):
            if not cur_node:
                return 
            
            if cur_node.val == key:
                if not cur_node.left and not cur_node.right:
                    return None
                
                elif not cur_node.left and cur_node.right:
                    return cur_node.right
                    
                elif not cur_node.right and cur_node.left:
                    return cur_node.left
                
                
                else:
                    min_node = findRightMin(cur_node.right)
                    cur_node.val = min_node.val
                    min_node.val = key 
                    
                    
                    
            cur_node.left = dNode(cur_node.left, key)
            cur_node.right = dNode(cur_node.right, key)
            
            
            return cur_node
        
        val = dNode(root, key)
        
        return val
        
        