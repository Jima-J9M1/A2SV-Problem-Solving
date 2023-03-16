# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        descendant = [[]]
        
        self.dfs(root, p , q, [], descendant)
        
        ptr1 = 0
        ptr2 = 0
        while (ptr1 < len(descendant[0][0]) and ptr2 < len(descendant[0][1])) and descendant[0][0][ptr1].val == descendant[0][1][ptr2].val:
            ptr1 += 1
            ptr2 += 1
        
        return descendant[0][0][ptr1 - 1]
        
        
    def dfs(self, curr, node1, node2, anscestor,descendant):
        
        if not curr or len(descendant[0]) == 2:
            return
        
        anscestor.append(curr)
        if curr.val == node1.val:
            descendant[0].append(anscestor[:])
        elif curr.val == node2.val:
            descendant[0].append(anscestor[:])
            
        
        self.dfs(curr.left,node1, node2, anscestor[:], descendant)
        self.dfs(curr.right, node1, node2, anscestor[:], descendant)
        anscestor.pop()
        
        return 