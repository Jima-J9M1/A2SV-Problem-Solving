# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bfs(self, node, tar):
        level = 1
        queue = deque()
        queue.append(node)
        answer = []
        
        if tar == 0:
            answer.append(node.val)
            return answer
        
        while queue:
            length = len(queue)
            for jim in range(length):
                temp = queue.popleft()
                if temp.left:
                    queue.append(temp.left)
                    if level == tar:
                        answer.append(temp.left.val)
                if temp.right:
                    queue.append(temp.right)
                    if level == tar:
                        answer.append(temp.right.val)
            if level == tar:
                break
            level += 1
        return answer
    
    def dfs(self, node, target):
        if not node:
            return 0
        
        if node.val == target:
            return 1
        
        left = self.dfs(node.left, target)
        right = self.dfs(node.right, target)
        
        if left:
            self.dict[node] = (left, True)
            return left + 1
        elif right:
            self.dict[node] = (right, False)
            
            return right + 1
        else:
            return 0

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.dict = {}
        self.dfs(root, target.val)
        abs_answer = []
        abs_answer.extend(self.bfs(target, k))
        for node in self.dict:
            if self.dict[node][0] == k:
                abs_answer.append(node.val)
                continue
            if self.dict[node][1]:
                if node.right:
                    result = self.bfs(node.right, k - self.dict[node][0] - 1)
                    abs_answer.extend(result)
            elif node.left:
                result = self.bfs(node.left, k - self.dict[node][0] - 1)
                abs_answer.extend(result)
                
        return abs_answer
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    