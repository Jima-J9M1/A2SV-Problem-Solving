# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.target = target.val
        self.k = k
        self.ans = []
        
        if k == 0:
            return [target.val]
        
        self.parentNodes(root,[])
        
        
        
        
        return self.ans
    
    
    #find the parent node distance from the target node is less than or equal to the a k distance
    def parentNodes(self, root, arr):
        if root is None:
            return 
        
        #find the node val that statisfy the condition of the k distance from target val
        #store the parent node to the arr which used to travers to the backward
        if root.val != self.target:
            arr.append(root)
            self.parentNodes(root.left,arr)
            self.parentNodes(root.right,arr)
            
            if arr:
                arr.pop()
                
        else:
            
            #calculate the node if the k distance is less than zero
            k = self.k
            

            #calculate the node chalid
            self.DistanceNode(root.left, k - 1 , None)
            self.DistanceNode(root.right, k - 1, None)
            
            avoid = root
            
            # calculate the backtracking of parent and avoid used to disclude the visited node
            while arr and k >= 0:
                k -= 1
                node = arr.pop()
                
                self.DistanceNode(node, k, avoid)
                avoid = node
                
            
            
        #find the distance between the node's
    def DistanceNode(self,root, k, avoid):
        
        if not root:
            return 
        
        if k == 0:
            self.ans.append(root.val)
            
        elif k > 0:
            k -= 1
            if root.left != avoid:
                self.DistanceNode(root.left , k, None)

            if root.right != avoid:
                self.DistanceNode(root.right ,k, None)
            
            
            
            