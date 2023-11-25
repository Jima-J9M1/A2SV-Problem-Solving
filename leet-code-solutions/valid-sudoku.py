class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for r in range(9):
            row_set = set()
            col_set = set()
            for c in range(9):
                if board[c][r] == "." and board[r][c] == ".":
                    continue
                
                if board[c][r] in col_set or board[r][c] in row_set:
                    return False
                
                if board[r][c] != ".":
                    row_set.add(board[r][c])
                    
                if board[c][r] != ".":
                    col_set.add(board[c][r])
                
        
        r,c = 0, 0
        for i in range(3):
            for j in range(3):
                grid_set = set()
                for k in range(r,r + 3):
                    for s in range(c, c + 3):
                        if board[k][s] == ".":
                            continue
                            
                        if board[k][s] in grid_set:
                            return False
                        
                        grid_set.add(board[k][s])
                        
                        
                c += 3
                
            r += 3
            c = 0
                        
        
        return True
                    
            
                        
                