# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root_node = TreeNode(preorder[0])
        right = 1
        
        for indx in range(1, len(preorder)):
            self.addNode(preorder[indx], root_node)
        
        return root_node
    
    
    def addNode(self, val, rootNode):
        if not rootNode:
            new_node = TreeNode(val)
            return new_node
            
            
        if val < rootNode.val:
            rootNode.left = self.addNode(val,rootNode.left)
        else:
            rootNode.right = self.addNode(val, rootNode.right)
        print(rootNode, val)
            
        return rootNode