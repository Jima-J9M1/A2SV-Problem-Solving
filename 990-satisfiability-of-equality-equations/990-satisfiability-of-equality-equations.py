class Solution:
    def find(self, equation):
        if equation != self.rep[equation]:
            self.rep[equation] = self.find(self.rep[equation])
            
        return self.rep[equation]
    
    def union(self, equ1,equ2):
            
        parent_1 = self.find(equ1)
        parent_2 = self.find(equ2)
        
        if parent_1 != parent_2:
            if self.size[parent_1] > self.size[parent_2]:
                self.size[parent_1] += self.size[parent_2]
                self.rep[parent_2] = parent_1
            else:
                self.size[parent_2] += self.size[parent_1]
                self.rep[parent_1] = parent_2
                
        
        return 1
    
    def equationsPossible(self, equations: List[str]) -> bool:
        self.rep = {chr(i + 97) : chr(i + 97) for i in range(26)}
        self.size = defaultdict(int)
        
        self.equality = defaultdict(str)
        
        for ele in equations:
            if ele[1:-1] == "==":
                check = self.union(ele[0],ele[-1])
             
        for ele in equations:
            
            if ele[1:-1] == "!=":
                
                rep_a = self.find(ele[0])
                rep_b = self.find(ele[-1])
                if rep_a == rep_b:
                    return False
        
        return True
                
            
            
            
            
            
            
            
            
            
        
        
        