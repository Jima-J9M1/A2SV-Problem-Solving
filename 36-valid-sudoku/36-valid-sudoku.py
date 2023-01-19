class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        count_row = []
        count_col = []
        for row in range(len(board)):
            row_count = 0
            
            
            for col in range(len(board[0])):
                if board[row][col].isdigit():
                    if board[row].count(board[row][col]) > 1:
                        return False
                
                
        for col in range(len(board[0])):
            
            col_counter = defaultdict(int)
            col_count = 0
            
            for row in range(len(board)):
                
                if board[row][col].isdigit():

                    col_counter[board[row][col]] += 1
                    if col_counter[board[row][col]] > 1:
                        return False
        

        
        for row in range(0, 9, 3):
            
            for col in range(0, 9, 3):
                j = col
                i = row
                count_cell = defaultdict(int)
                
                for new_row in range(3):
                    
                    for new_col in range(3):
                        
                        
                        if board[i][j].isdigit():
                            count_cell[board[i][j]] += 1
                            
                            if count_cell[board[i][j]] > 1:
                                return False
                        
                            
                        j += 1
                    i += 1
                    j = col
        
        
                        
                        
                # else:
                #     col_count += 1
                
            # count_col.append(col_count)
        
#         if (min(count_col) == 9 and min(count_row) == 9) or (max(count_col) < 9 and max(count_row) < 9):
#             return True
#         else:
#             return False


        return True