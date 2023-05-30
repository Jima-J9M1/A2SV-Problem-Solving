class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [(0,1),(1,0)]
        memo = {}
        ans = self.dp(0,0, m,n, memo)
        
        return ans
        
    def isbound(self, row,col,m,n):
        return ((0 <= row < m) and (0 <= col < n))
    
    def dp(self, row, col, m,n,memo):
        if row == m - 1 and col == n - 1:
            return 1
        
        if (row,col) not in memo:
            new_row = row + 1
            new_col = col + 1
            
            bottom = 0
            right = 0
            
            if self.isbound(new_row, col,m,n):
                bottom = self.dp(new_row, col, m, n, memo)
                
            if self.isbound(row, new_col,m,n):
                right = self.dp(row, new_col, m, n, memo)
                
            memo[(row,col)] = bottom + right
            
        return memo[(row,col)]