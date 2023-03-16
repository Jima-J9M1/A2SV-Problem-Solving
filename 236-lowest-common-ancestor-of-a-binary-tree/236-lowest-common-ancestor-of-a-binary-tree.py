# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.dfs(root, p, q)
        
        
    def dfs(self, root,node1,node2):
        if not root:
            return 
        
        if root == node1 or root == node2:
            return root
        
        left = self.dfs(root.left, node1, node2)
        right = self.dfs(root.right, node1, node2)
        
        if (left == None):
            return right
        if (right == None):
            return left
        
        return root
#         descendant = [[]]
        
#         self.dfs(root, p , q, [], descendant)
        
#         ptr1 = 0
#         ptr2 = 0
#         while (ptr1 < len(descendant[0][0]) and ptr2 < len(descendant[0][1])) and descendant[0][0][ptr1].val == descendant[0][1][ptr2].val:
#             ptr1 += 1
#             ptr2 += 1
        
#         return descendant[0][0][ptr1 - 1]
        
        
#     def dfs(self, curr, node1, node2, anscestor,descendant):
        
#         if not curr or len(descendant[0]) == 2:
#             return
        
#         anscestor.append(curr)
#         if curr.val == node1.val:
#             descendant[0].append(anscestor[:])
#         elif curr.val == node2.val:
#             descendant[0].append(anscestor[:])
            
        
#         self.dfs(curr.left,node1, node2, anscestor[:], descendant)
#         self.dfs(curr.right, node1, node2, anscestor[:], descendant)
#         anscestor.pop()
        
#         return 

