class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = self.recString(n)
        return ans[k - 1]
    
    def recString(self,n):
        
        if n == 1:
            return "0"
        
        ans = self.recString(n - 1) 
        
        res = ""
        
        for i in range(len(ans)):
            if ans[i] == "0":
                res += "1"
            else:
                res += "0"
                
        ans += "1" + res[::-1]
        
        return ans
    
