class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        if len(grid) == 3:
            max_val = float ("-inf")
            
#             for row in range(3):
#                 for col in range(3):
#                     max_val = max(max_val,grid[row][col])
                    
#             return [[max_val]]
        
        maxLocal = []
        len_row = math.ceil(len(grid) - 2)
        len_col = math.ceil(len(grid[0]) - 2)
        
        
        for row in range(len_row):
            
            grid_3 = []
            
            for col in range(len_col):
                max_val = float ("-inf")
                
                for i in range(row, row + 3):
                    
                    for j in range(col ,col + 3):
                        max_val = max(max_val,grid[i][j])
                grid_3.append(max_val)

                
            maxLocal.append(grid_3)
        
        return maxLocal