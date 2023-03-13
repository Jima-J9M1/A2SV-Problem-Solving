# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        descent = [[]]
        self.BTS(root,descent, p, q)
        
        return descent[0]
    
    '''
    Function BTS -> Binary Tree Search
    @param: root -> hold current node
    @param: node1 -> represent input p
    @param: node2 -> represent input q
    @param: descent -> the variable that hold the descent node(passed by reference)
    '''
    def BTS(self, root, descent, node1 ,node2):
        if not root:
            return 
        
        #if either one of the input node is equal with the current node the descent will be the current noode 
        if node1.val == root.val or node2.val == root.val:
            descent[0] = root
            return 
        
        #hold the descent if the current node is greater and less than either of the input node
        if node1.val > root.val and node2.val < root.val:
            descent[0] = root
            return
        
        if node1.val < root.val and node2.val > root.val:
            descent[0] = root
            return 
            
        
    
        self.BTS(root.left, descent, node1, node2)
        self.BTS(root.right, descent, node1, node2)