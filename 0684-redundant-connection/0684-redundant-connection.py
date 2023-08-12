class Solution:
    def represetative(self,rep, x):
        while rep[x] != x:
            x = rep[x]
            
        return rep[x]
    
    def union(self, rep,x,y):
        rep_x = self.represetative(rep, x)
        rep_y = self.represetative(rep, y)
        
        if rep_x == rep_y:
            return [x, y]
        
        rep[rep_x] = rep_y
        
        return False
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        rep = {i : i for i in range(1, len(edges) + 1)}
        
        
        ans = []
        for v1, v2 in edges:
            ans = self.union(rep, v1,v2)
            if ans:
                break
        return ans