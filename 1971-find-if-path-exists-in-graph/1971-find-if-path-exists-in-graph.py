class Solution:
    def find(self, node):
        if node == self.rep[node]:
            return node
        
        ret = self.find(self.rep[node])
        self.rep[node] = ret
        return ret
        
        
        
    
    def union(self, start, dest):
        parent_start = self.find(start)
        parent_des = self.find(dest)
        
        
        if parent_start != parent_des:
            if self.size[parent_start] > self.size[parent_des]:
                self.rep[parent_des] = parent_start
                
            elif self.size[parent_start] < self.size[parent_des]:
                self.rep[parent_start] = parent_des
                
            else:
                self.rep[parent_des] = parent_start
                self.size[parent_start] += 1
                     
#         if parent_start == parent_des:
#             return
        
#         self.rep[parent_des] = parent_start'
        
        
        
    
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.rep = {i : i for i in range(n)}
        self.size = [0] * n
        
        for start, end in edges:
            self.union(start,end)
        
        parent_source = self.find(source)
        parent_des = self.find(destination)
        
        return parent_source == parent_des
        
        
        
        
    