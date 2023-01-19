class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        len_row = len(grid) - 2
        len_col = len(grid[0]) - 2
        
        count = 0
        
        for row in range(len_row):
            
            for col in range(len_col):
                digonal_sum = {}
                digonal_sum[row - col] = 0
                check_sum = sum(grid[row][col:col+3])    
                res = set()
                checker = set()
                flag = True
                
                
                #Check if the row are equal with check_sum                  
                for i in range(row, row + 3):
                    row_sum = 0
                    
                    for j in range(col, col + 3):
                        if 0 < grid[i][j] <= 9:
                            if (i - j) in digonal_sum:
                                digonal_sum[i - j] += grid[i][j]

                                
                            # if i == j:
                            #     digonal_sum += grid[i][j]
                            row_sum += grid[i][j]

                            if grid[i][j] in checker:
                                flag = False
                                break
                            checker.add(grid[i][j])
                        else:
                            flag = False
                            break
                    
                    res.add(row_sum)

                res.add(digonal_sum[row - col])
                
                if flag:
                    #Check if the column sum are equal with check sum 
                    
                    for i in range(col, col + 3):
                        col_sum = 0

                        for j in range(row, row + 3):
                            col_sum += grid[j][i]
                        res.add(col_sum)
                        
    
                    if len(res) == 1:
                        count += 1
        
        return count
                        
                         
                        