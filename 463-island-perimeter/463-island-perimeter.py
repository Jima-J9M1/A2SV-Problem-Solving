class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, -1), (1,0), (0, 1)]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid)) ]
        perimeter = 0

        rows = len(grid)
        cols = len(grid[0])
        
        
    
    
        
    
    
        def isbound(new_row, new_col):
            if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
                return True
        
        
        
        def dfs(visited,row, col):
            if grid[row][col] == 0:
                
                return 1
            
            ans = 0
            for row_direction, col_direction in directions:

                visited[row][col] = True
                new_row = row + row_direction
                new_col = col + col_direction

                if isbound(new_row, new_col) and not visited[new_row][new_col]:
                    ans += dfs(visited, new_row, new_col)

                elif not isbound(new_row, new_col):
                    ans += 1
            
            return ans
                
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    
                    return dfs(visited, row, col)
                    
                    
        
        
        