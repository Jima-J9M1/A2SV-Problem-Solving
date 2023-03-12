# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        mode = [[]]
        
        self.traverse(root, mode, [float('-inf')], [0], [1])
        
        return mode[0]
        
    '''
    @param -> curr describe the current node
    @param -> mode store the frequent value in the tree
    @param -> prev indicate the previous node of the tree
    @cur_freq -> the current frequency of the node
    @freq -> maximum frequency of the node
    '''
    def traverse(self, curr, mode, prev, cur_freq,  freq):
        if not curr:
            return 
        
        self.traverse(curr.left, mode, prev, cur_freq, freq)
        #if the previous node is float and the current node value equal with the prevous node increase the current frequency
        
        if prev[0] == float('-inf') or curr.val == prev[0]:
            cur_freq[0] += 1    
            
        else:
            #if the current node is not equal with the previous one reset the current node
            cur_freq[0] = 1
        
        #add the current node to the mode list if the current node frequncy equal with the maximum frequncy node
        if cur_freq[0] == freq[0]:
            
                mode[0].append(curr.val)
        
        #if the current node has large frequency than the maximum frquency stored  change the maximum frequency to the current frequency. Reset the mode list to the current value 
        if cur_freq[0] > freq[0]:
            
                mode[0] = [curr.val]
                freq[0] = cur_freq[0]
        
        #change the previous node value to the current node val 
        prev[0] = curr.val
        self.traverse(curr.right, mode, prev, cur_freq, freq)
        
        
        
        
        
        
        
        
        
#         self.arr = []
#         self.inorder(root)
        
#         count = Counter(self.arr)
        
#         max_val = max(count.values())
#         res = sorted(count, key= lambda x: count[x], reverse=True)
#         ans = []
        
        
#         for i in range(len(res)):
            
#             if count[res[i]] == max_val:
#                 ans.append(res[i])
#                 print(res[i])
                
#         return ans
    
#     def inorder(self,root):
        
#         if root is None:
#             return 
        
        
#         self.inorder(root.left)
#         self.arr.append(root.val)
#         self.inorder(root.right)