class Solution:
    def find(self, node):
        if node == self.rep[node]:
            return node
        
        ans = self.find(self.rep[node])
        self.rep[node] = ans
        
        return ans
    
    
    def union(self, v1,v2):
        parent_v1 = self.find(v1)
        parent_v2 = self.find(v2)
        
        if parent_v1 != parent_v2:
            if self.size[parent_v1] > self.size[parent_v2]:
                self.rep[parent_v2] = parent_v1
                
            elif self.size[parent_v2] > self.size[parent_v1]:
                self.rep[parent_v1] = parent_v2
                
            else:
                self.rep[parent_v2] = parent_v1
                self.size[parent_v1] += 1
                
        else:
            return True
        
        return False
                
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        self.rep = {i : i for i in range(1,len(edges) + 1)}
        self.size = [0] * (len(edges) + 1)
        
        for start,end in edges:
            boolean = self.union(start, end)
            
            if boolean:
                return [start, end]