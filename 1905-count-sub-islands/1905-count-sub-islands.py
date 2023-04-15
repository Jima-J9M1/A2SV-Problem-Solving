class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [[-1,0], [0,-1], [1,0], [0,1]]
        visited_1 = [[1 for __ in range(len(grid1[0]))] for __ in range(len(grid1))]
        visited_2 = [[1 for __ in range(len(grid1[0]))] for __ in range(len(grid1))]
        
        
        
        def isbound(grid, row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid, visited, row, col):
            if grid[row][col] == 0:
                return
            visited[row][col] = False
            
            for new_row, new_col in directions:
                new_row += row
                new_col += col 
            
                if isbound(grid,new_row, new_col) and visited[new_row][new_col]:
                    dfs(grid, visited,new_row, new_col)
                    
            return 
        
        def dfs_2(grid, visited_1, visited_2, row, col, ans):            
            if grid[row][col] == 0:
                return
            
            if visited_1[row][col]:
                ans[0] = False
            
            visited_2[row][col] = False
            
            for new_row, new_col in directions:
                new_row += row
                new_col += col 
                if isbound(grid,new_row, new_col) and visited_2[new_row][new_col]:
                    
                    dfs_2(grid, visited_1, visited_2, new_row,new_col,ans)
                    
            
 
        
        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if grid1[row][col] == 1 and visited_1[row][col]:
                    dfs(grid1, visited_1, row, col)
        count = 0
       
        
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] == 1 and visited_2[row][col]:
                    ans = [True]
                    dfs_2(grid2, visited_1, visited_2, row, col,ans)
                    if ans[0]:
                        count += 1
                    
        return count
            
        
        
        