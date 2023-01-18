class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        directions = [[0,-1],[-1,0],[1,0],[0,1]]
        row_col = []
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        #find zero and find T directions of zero element with directoins list and update with zero         
        for row in range(row_len):
            
            for col in range(col_len):
                
                new_row = row
                new_col = col
                
                
                if matrix[row][col] == 0:
                    left = 0
                    
                    while left < len(directions):
                        row_pos = directions[left][0]
                        col_pos = directions[left][1]
                        
                        new_row += row_pos
                        new_col += col_pos

                        if 0 <= new_row < row_len and 0 <= new_col < col_len:
                            row_col.append([new_row,new_col])
                            continue

                        left += 1
                        new_row = row
                        new_col = col
                        

        for index in range(len(row_col)):
            row = row_col[index][0]
            col = row_col[index][1]

            matrix[row][col] = 0
                

                        
                    
            