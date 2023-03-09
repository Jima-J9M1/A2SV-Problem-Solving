class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        #if the number is negative then calculate the power of the abs of the number and return one over the result of the postivie number 
        if n < 0 :
            return 1/self.power(x,-1*n)
        
        return self.power(x,n)
            
    
    def power(self,x,n):
        
        #if the power of the number is zero which return one         
        if n == 0:
            return 1
        
        #if the power is odd value then calculate with even value and mutiply by one x
        if n % 2 == 1:
            
            ans = self.power(x, n // 2)
            return ans * ans * x
        
        else:
            
            ans = self.power(x, n // 2)
            
            return ans*ans
        
        