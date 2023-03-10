# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []
        self.inorder(root)
        
        count = Counter(self.arr)
        
        max_val = max(count.values())
        res = sorted(count, key= lambda x: count[x], reverse=True)
        ans = []
        
        
        for i in range(len(res)):
            
            if count[res[i]] == max_val:
                ans.append(res[i])
                print(res[i])
                
        return ans
    
    def inorder(self,root):
        
        if root is None:
            return 
        
        
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)