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
        
        def dp(num, size, memo):
            if size == 0:
                return 1
            
            if (num, size) in memo:
                return memo[(num, size)]
            
            ans = 0
            for neighbor in knight_move[num]:
                ans += dp(neighbor, size - 1, memo)
                
                
            memo[(num, size)] = ans
            
            
        
            return memo[(num, size)]
        
        ans = 0
        memo = {}
        
        for key in knight_move:
            ans += dp(key, n - 1, memo)
        
        
        return ans % (10**9 + 7)
            