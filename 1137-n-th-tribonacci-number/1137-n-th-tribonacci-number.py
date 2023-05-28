class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        result = self.trib(n,memo)
        
        return result
    
    
    def trib(self,n,memo):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        
        if n in memo:
            return memo[n]
        
        t = self.trib(n - 1, memo) + self.trib(n - 2, memo) + self.trib(n - 3, memo)
        memo[n] = t
        
        return memo[n]
        
        
        
#         BOTTOM UP APPROACH 
#         tribonacci = {0:0}
#         for i in range(1, n + 1):
#             if i <= 2:
#                 trib = 1
#             else:
#                 trib = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i - 3]
                
#             tribonacci[i] = trib
            
#         return tribonacci[n]