class Solution:
    def splitString(self, s: str) -> bool:
        numb = [[]]
        
        return self.checkString(s,numb,0)
        
        
    def checkString(self, s, numb, idx):
        
        if len(s) <= idx:
            return len(numb[0]) >= 2
        
        for i in range(idx, len(s)):
            val = int(s[idx: i + 1])
            if len(numb[0]) == 0 or val == numb[0][-1] - 1:
                
                numb[0].append(val)
                if self.checkString(s, numb, i + 1):
                    return True
                
                numb[0].pop()
            
        return False