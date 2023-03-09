class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            return 1/self.power(x,-1*n)
        return self.power(x,n)
            
    
    def power(self,x,n):
        
        if n == 0:
            return 1
        
        if n % 2 == 1:
            ans = self.power(x, n // 2)
            return ans * ans * x
        else:
            ans = self.power(x, n// 2)
            return ans*ans
        
        