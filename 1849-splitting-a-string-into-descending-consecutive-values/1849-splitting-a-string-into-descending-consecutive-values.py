class Solution:
    def splitString(self, s: str) -> bool:
        self.check = []
        
        ans = self.backTracking(0,s)
        
        return ans
       
        
    def backTracking(self,idx,s):


        if len(s) <= idx:
            return len(self.check) >= 2


        for i in range(idx,len(s)):

            val = int(s[idx : i + 1])
            

            if len(self.check) == 0 or val == self.check[-1] - 1:

                self.check.append(val)
                if self.backTracking(i + 1, s):
                    
                    return True

                self.check.pop()


        return False

        
        
                    
                
            
            
        