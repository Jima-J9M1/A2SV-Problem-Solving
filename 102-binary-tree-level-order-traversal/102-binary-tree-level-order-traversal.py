# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return 
        
        queue = deque([root])
        level_order = []
        
        while queue:
            len_order = len(queue)
            level = []
            for _ in range(len_order):
                
                node = queue.popleft()
                
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            level_order.append(level)
            
        return level_order
                
        
        
        