class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        
        
        knight_move = {
            0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            6:[0,1,7],
            7:[6,2],
            8:[1,3],
            9:[2,4]
        }
        
        dp = [[1]*(n + 1) for _ in range(10)]
    
        for i in range(1, n + 1):
            for j in range(10):
                if j == 5:
                    continue
                    
                ans = 0
                for neighbor in knight_move[j]:
                    ans += dp[neighbor][i - 1]
                
                dp[j][i] = ans
                
        res = 0
        
        for key in knight_move:
            res += dp[key][n - 1]
        
        return res % (10 ** 9 + 7)
#         def dp(num, size, memo):
#             if size == 0:
#                 return 1
            
#             if (num, size) in memo:
#                 return memo[(num, size)]
            
#             ans = 0
#             for neighbor in knight_move[num]:
#                 ans += dp(neighbor, size - 1, memo)
                
                
#             memo[(num, size)] = ans
            
            
        
#             return memo[(num, size)]
        
#         ans = 0
#         memo = {}
        
#         for key in knight_move:
#             ans += dp(key, n - 1, memo)
        
        
#         return ans % (10**9 + 7)
            