# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        zigzag = True
        queue = deque([root])
        zigzag_list = []
        
        if not root:
            return 
        
        
        while queue:
            len_level = len(queue)
            level = []
            for _ in range(len_level):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            if zigzag:
                zigzag_list.append(level)
                zigzag = False
                
            else:
                reverse_list = level[::-1]
                zigzag_list.append(reverse_list)
                
                zigzag = True
        
        return zigzag_list
        