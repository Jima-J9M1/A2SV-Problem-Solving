# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        average_list = []
        
        
        while queue:
            len_node = len(queue)
            average_sum = 0
            
            for __ in range(len_node):
                
                node = queue.popleft()
                average_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            average_list.append(average_sum / len_node)
            
        
        return average_list
            
            
            
        