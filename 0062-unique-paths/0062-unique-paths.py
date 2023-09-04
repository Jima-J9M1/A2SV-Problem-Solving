class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Goal: Is to reaturn the number of unique paths from starting cell to end cell
        #Approach:build the unique path starting from the end to the starting
        #        Build Grid -> which has (m + 1) and (n + 1) we need to set with 0's another below row and right column to form  unique path
        #        Form time complexity I use catching with memo or @cache
        #        Check the bounder of each row and column with function bound()
        
        
        grid = [[1]*n]*m
        
        for row in range(1,m):
            for col in range(1, n):
                grid[row][col] = grid[row - 1][col] + grid[row][col - 1]
                
        
        return grid[-1][-1]
        
#         if n == 1 and m == 1:
#             return 1
        
#         def bound(row, col):
#             return (0 <= row < m) and (0 <= col < n)
        
        
#         grid = [[0] * (n + 1) for _ in range(m + 1)]
#         memo = {}
#         def dp(grid, row, col):
#             if row == m - 1and col == n - 1:
#                 return 1
#             if (row, col) in memo:
#                 return memo[(row, col)]
#             ncol = col + 1
#             nrow = row + 1
#             if bound(nrow, col):
#                 down = dp(grid, nrow, col)
#                 grid[nrow][col] = down
#             if bound(row, ncol):
#                 right = dp(grid, row, ncol)
#                 grid[row][ncol] = right
                
#             grid[row][col] = grid[row][ncol] + grid[nrow][col]
#             memo[(row, col)] = grid[row][col]
#             return memo[(row, col)]
        
#         dp(grid, 0, 0)
        
        return grid[0][0]
        
        
        
        