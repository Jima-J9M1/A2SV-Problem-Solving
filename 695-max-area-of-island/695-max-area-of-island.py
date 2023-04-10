class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions  = [[-1,0], [0, -1], [1, 0], [0, 1]]
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        max_val = 0
        
        def isbound(row,col):
            return (0 <= row < len(grid) and (0 <= col < len(grid[0])))
        
        def dfs(row, col,count):
            if grid[row][col] == 0:
                return count
            
            count[0] += 1
            visited[row][col] = True
            
            for new_row, new_col in directions:
                new_row += row
                new_col += col
                
                if isbound(new_row, new_col) and not visited[new_row][new_col]:
                    dfs(new_row, new_col, count)
                    
            return count[0] 
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                
                if grid[row][col] == 1:
                    
                    # print(visited)
                    if not visited[row][col]:
                        ans = dfs(row, col, [0])
                        max_val = max(ans, max_val)
        
        return max_val
                        
                    
                    
                    