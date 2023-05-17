class Solution:
    def find(self, node):
        if node == self.rep[node]:
            return node
        
        return self.find(self.rep[node])
        
        
        
    
    def union(self, start, dest):
        parent_start = self.find(start)
        parent_des = self.find(dest)
        
        if parent_start == parent_des:
            return
        
        self.rep[parent_start] = parent_des
        
        
        
    
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.rep = {i : i for i in range(n)}
        
        for start, end in edges:
            self.union(start,end)
        
        parent_source = self.find(source)
        parent_des = self.find(destination)
        
        return parent_source == parent_des
        
        
        
        
    