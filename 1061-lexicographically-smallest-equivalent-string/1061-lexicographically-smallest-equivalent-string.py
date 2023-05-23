class Solution:
    def find(self, str1):
        if str1 == self.rep[str1]:
            return str1
        
        par_str = self.find(self.rep[str1])
        self.rep[str1] = par_str
        
        return par_str
    
    def union(self, str1, str2):
        parent_1 = self.find(str1)
        parent_2 = self.find(str2)
        
        if parent_1 > parent_2:
            self.rep[parent_1] = parent_2
        else:
            self.rep[parent_2] = parent_1
            
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.rep = {chr(i + 97) : chr(i + 97) for i in range(26)}
        

        for i in range(len(s1)):
            self.union(s1[i], s2[i])
            
        s = []
        for ele in baseStr:
            s.append(self.find(ele))
            
            
            
        return "".join(s)
        
            