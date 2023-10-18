class Solution:
    def find(self, rep, word):
        root = word
        
        while root != rep[root]:
            root = rep[root]
            
        while word != root:
            parent = rep[word]
            rep[word] = root
            word = parent
            
        return root
        
    def union(self, rep, ch1, ch2):
        rep_ch1 = self.find(rep, ch1)
        rep_ch2 = self.find(rep, ch2)
        
        if rep_ch1 == rep_ch2:
            return 
        
        if rep_ch1 < rep_ch2:
            rep[rep_ch2] = rep_ch1
            
        else:
            rep[rep_ch1] = rep_ch2
            
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {i:i for i in range(26)}
        n = len(s1)
        
        for i in range(n):
            if s1[i] != s2[i]:
                s1_num = ord(s1[i]) - ord('a')
                s2_num = ord(s2[i]) - ord('a')
                self.union(rep, s1_num, s2_num)
                
                
        ans = ""
        for i in range(len(baseStr)):
            ord_num = ord(baseStr[i]) - ord('a')
            rep_val = self.find(rep, ord_num)
            ans += chr(rep_val + ord('a'))
            
        
        
        return ans
        
        
        
        
        
        
        
        
        