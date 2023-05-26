class Solution:
    def climbStairs(self, n: int) -> int:
        memo = dict()
        res = self.dp(n, memo)
        
        return res
    def dp(self,n, memo):
        if n == 1:
            return 1
        if n == 0:
            return 1
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.dp(n - 1, memo) + self.dp(n - 2, memo)
        return memo[n]
        