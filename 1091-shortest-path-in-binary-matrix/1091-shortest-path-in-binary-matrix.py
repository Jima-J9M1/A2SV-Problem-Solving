class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = [[1]*len(grid[0]) for i in range(len(grid))]

        directions = [[1,1],[0,1],[1,0],[-1,1],[1,-1],[0,-1],[-1,0],[-1,-1]]
        level = 1
        queue = deque([[0,0]])
        n = len(grid)
        
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        def isbound(grid, row, col):
            return ((0 <= row < len(grid) ) and (0 <= col < len(grid[0])))
        
        
        while queue:
            
            len_level = len(queue)
            
            for __ in range(len_level):
                row, col = queue.popleft()
                
                
                if row == n - 1 and col == n - 1:
                    return level
                    
                
                for new_row, new_col in directions:
                    
                    new_row += row
                    new_col += col 
                    
                   
                        
                    if isbound(grid, new_row, new_col) and visited[new_row][new_col] and grid[new_row][new_col] == 0:
                        
                        queue.append([new_row, new_col])
                        visited[new_row][new_col] = False
                        
                        
                        
            level += 1
            
                        
                        
                
        return -1
                        
            
                        
                        
                        
                        
                        
            
        
        
        