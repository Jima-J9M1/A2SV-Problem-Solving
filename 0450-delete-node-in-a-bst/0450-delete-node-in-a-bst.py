# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        
        def dfs(cur_node, key):
            
            if not cur_node:
                return cur_node
            
            if cur_node.val > key:
                cur_node.left = dfs(cur_node.left, key)
                
            elif cur_node.val < key:
                cur_node.right = dfs(cur_node.right, key)
                
                
                
            else:
                
                if not cur_node.left:
                    return cur_node.right
                
                elif not cur_node.right:
                    return cur_node.left
                
                
                temp = inorderSuccessor(cur_node.right)
                
                cur_node.val = temp.val
                
                
                cur_node.right = dfs(cur_node.right, temp.val)
                
                
            return cur_node
        
        
        def inorderSuccessor(node):
            cur = node
            
            while (cur.left):
                cur = cur.left
                
            return cur
        
        
        
        node = dfs(root, key)
        
        
        return node