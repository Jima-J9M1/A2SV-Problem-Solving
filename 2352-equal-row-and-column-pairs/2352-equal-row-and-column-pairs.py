class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        col_grid = []
        length = len(grid)
        count = 0
        
        
        for indx in range(length):
            new_val = []
            
            for j in range(length):
                new_val.append(grid[j][indx])
                
            col_grid.append(new_val)
            
        for indx in range(length):
            
            for j in range(length):
                if grid[indx] == col_grid[j]:
                    count += 1
        
        return count